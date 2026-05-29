# Static review: CEETIS ATS units vs extracted command docs
## Inputs checked
- `multipin_highvoltage(3).ats` — primary review target.
- `NortechUtil_RS(3).ats`, `NortechUtil(3).ats`, `NortechTestStart_RS(3).ats`, `rs232_functions(3).ats` — dependency/context review.
- `commands_md.zip` — extracted CEETIS built-in command documentation.

## Method
Static review only. I did not run CEETIS or execute the ATS files. I parsed the command markdown to compare return types, call signatures, and available built-in alternatives, then inspected the ATS unit files for call-flow, stale-list, return-value, and workflow issues.

## Built-in command facts used from the extracted docs
- `NoConnAllLV / NoConnAllHV / NoConnAllDB`: Declared as returning `boolean`, not `integer`/`TESTSTEP_*`. They test whether one pin is not connected to any other pin; HV/DB variants are not executed if the pin belongs to a grounded network.
- `NoConnGroupLV / NoConnGroupHV / NoConnGroupDB`: Declared as returning `boolean`; test high group vs low group. Splices and virtual pins passed in the groups are ignored.
- `WireTest`: Declared as returning `integer` and returns `TESTSTEP_Passed`, `TESTSTEP_Failed`, `TESTSTEP_Invalid`, or `TESTSTEP_NotExecuted`.
- `NWCreatePinlist`: Returns the number of found pins and accepts only documented component constants: Wire, Switch, Resistor, Capacitor, Diode, ZDiode, CTwist, RLCCombination, VariableResistor.
- `MiscCreateList`: Creates a one-dimensional array only if it does not already exist. It does not clear/recreate an existing list.
- `MiscAddLists / MiscSubtractLists`: Return the number of items in the result list.
- `MiscListFromString`: Returns the number of parsed elements.
- `PinsInRange`: Returns pins in a range, but docs warn it cannot be used when the project works with adapter cables from the adapter cable library.
- `TestWires, IsolationGroupTestLV/HV, DielectricBreakdownGroupTest`: Available built-in automatic/group tests; the group isolation/breakdown docs say they are only adequate for small UUTs and respect run-parameter exclusions.
- `ReportWriteMeasurementParameters`: Available for writing active measurement parameters for continuity, LV, HV, and DB command groups.

## Highest-priority findings

### HIGH: Boolean no-connect return values are treated like TESTSTEP integer status codes
Location: `multipin_highvoltage(3).ats`: 711-763

The wrappers `no_conn_all_lv_guard`, `no_conn_all_hv_guard`, and `no_conn_all_db_guard` are declared `integer`, call `NoConnAllLV/HV/DB`, and compare the result to `TESTSTEP_Passed` and `TESTSTEP_NotExecuted`. The extracted docs declare those built-ins as `boolean`. If CEETIS internally maps TRUE/FALSE to integers, pass/fail may appear to work by accident, but `TESTSTEP_NotExecuted` detection is not supported by the documented return type. This can mark guards as tested when the underlying no-connect command was skipped or failed.

Recommendation: Change these wrappers to return `boolean` and compare `Result == FALSE`, or use a documented integer-returning command if one exists for this exact use. Do not compare `NoConnAll*` results against `TESTSTEP_*` unless CEETIS vendor docs explicitly guarantee those constants for these commands.

### HIGH: `no_conn_db_current()` calls the HV guard, not a DB/current guard
Location: `multipin_highvoltage(3).ats`: 1640-1662, especially line 1654

`no_conn_db_current()` is named and documented as dielectric-breakdown/current related, but it calls `no_conn_all_hv_guard()`. That runs `NoConnAllHV`, not `NoConnAllDB`. This is probably a copy/paste defect. The comment also says `run HV DB current test`, which is internally inconsistent.

Recommendation: Decide whether this routine is HV current-threshold isolation or dielectric breakdown. If DB, call `no_conn_all_db_guard()` after setting `ParamDielectricBreakdown`. If HV current-threshold isolation, rename it to `no_conn_hv_current_list` or similar and document that it is HV-current mode, not DB.

### HIGH: HV/DB parameter changes happen after the populated-contact pass
Location: `multipin_highvoltage(3).ats`: 1495-1524, 1568-1597, 1771-1803

`no_conn_hv_current_populated()`, `no_conn_hv_populated()`, and `no_conn_db_populated()` run the populated-pin pass first, then call `ParamIsolationHVCurrent`, `ParamIsolationHV`, or `ParamDielectricBreakdown`, then run the unpopulated-pin pass. If `Tmeas`/`Twait` are intended for the whole function, the first half uses whatever parameters were already active.

Recommendation: Move the relevant `Param...` call before the first populated pass, then optionally call `ReportWriteMeasurementParameters()` immediately after. If the split is intentional, rename/comment it clearly as two different test configurations.

### HIGH: `strip_list_empty_string()` can use stale/uninitialized list data
Location: `multipin_highvoltage(3).ats`: 133-176

The function initializes `StrippedList` only when the valid pin happens to be at `Index == 1`. If the first parsed entry is empty/unnamed and a later entry is valid, the `else` path calls `MiscAddLists(StrippedList, StrippedList, PinListSingle)` before `StrippedList` has been seeded. If all entries are empty, it still reaches `MiscListToString(StrippedList, ';')`. Also, `MiscCreateList` does not recreate an already-existing list, so repeated calls can retain stale content unless every element is overwritten.

Recommendation: Use a `CreatedList` boolean like `get_named_pin_list_all()`. Seed on the first valid pin, not on `Index == 1`. Return `''` if no valid pins were found. Avoid using the same list as both result and input to `MiscAddLists` until confirmed safe.

### HIGH: Several helper functions declare return values but never assign `Result`
Location: `NortechUtil_RS(3).ats`: 128, 1432, 1496, 1564, 1632; `rs232_functions(3).ats`: 240, 336, 440, 471, 484, 497, 514, 533

Functions such as `probe_test_4wire()`, the switch-test helpers, `rs232_send_cmd()`, `timer_send_cmd()`, `timer_set()`, `timer_start()`, `timer_stop()`, `timer_pause()`, `timer_finish()`, and `timer_set_errors()` declare `integer` or `boolean` returns but do not set `Result`. Callers that use these results will get undefined/stale values.

Recommendation: Either change these to `void` or set `Result` deterministically on every path. For communication helpers, use `FALSE` by default and only set `TRUE` when open/send/receive behavior succeeds by the intended definition.

### HIGH: `timer_set()` calls `timer_disp_str()` with shifted arguments
Location: `rs232_functions(3).ats`: 440-462, especially line 459

`timer_disp_str()` signature is `(Message, Line=0, Debug=FALSE, Reopen=FALSE)`. `timer_set()` calls `timer_disp_str('Invalid', Debug, Reopen)`, so `Debug` is passed as `Line`, and `Reopen` is passed as `Debug`. That is a subtle type/order bug and will also suppress or mis-route debug behavior.

Recommendation: Change to `timer_disp_str('Invalid', 0, Debug, Reopen);`.

### MEDIUM: `get_component_netlist_primary()` and `_both()` discard the cleaned string
Location: `multipin_highvoltage(3).ats`: 231-246 and 388-403

Both functions call `strip_list_empty_string(Result);` but do not assign the return value back to `Result`. The comments assume in-place normalization, but the helper is declared as returning a string. This means the clean-up is ignored.

Recommendation: Use `Result = strip_list_empty_string(Result, Debug);` in both functions.

### MEDIUM: Accumulator lists are seeded with a dummy/stale element
Location: `multipin_highvoltage(3).ats`: 297-345 and 455-503

`get_netlist_primary_all()` and `get_netlist_both_all()` call `MiscCreateList(PrimaryPins, 1)` / `MiscCreateList(BothPins, 1)` before merging real lists. Since `MiscCreateList` does not recreate an existing list, this can preserve old contents. Even on first use, it creates a one-element list before real data exists; the later strip function is then relied on to hide the dummy.

Recommendation: Use a `CreatedList` flag. On the first non-empty source list, assign/copy it as the accumulator. Only call `MiscAddLists()` after the accumulator is valid.

### MEDIUM: Component enumeration is hardcoded as `0 to 8` instead of documented constants
Location: `multipin_highvoltage(3).ats`: 303-325 and 461-483

The built-in docs list allowed component constants for `NWCreatePinlist`; they do not guarantee that component identifiers are contiguous integers `0..8`. The code also separately handles `COMPONENT_VariableResistor`, suggesting uncertainty about the range.

Recommendation: Replace numeric loops with an explicit documented component list: `COMPONENT_Wire`, `COMPONENT_Switch`, `COMPONENT_Resistor`, `COMPONENT_Capacitor`, `COMPONENT_Diode`, `COMPONENT_ZDiode`, `COMPONENT_CTwist`, `COMPONENT_RLCCombination`, and `COMPONENT_VariableResistor`.

### MEDIUM: `get_netlist_primary()` and `get_netlist_both()` ignore `NWCreatePinlist()` count
Location: `multipin_highvoltage(3).ats`: 185-193 and 522-530

Both functions call `NWCreatePinlist()` without capturing the returned count. If no pins are found, the reused `PinList` variable may still contain prior contents, and the function can return stale data.

Recommendation: Capture the count. If zero, return `''` and do not stringify the list. Also avoid reusing a generic global `PinList` where possible.

### MEDIUM: `get_named_pin_list_all()` has an off-by-one/ground ambiguity and no empty-list guard
Location: `multipin_highvoltage(3).ats`: 599-640

The loop uses `for Index = 1 to Count - 1`. The extracted docs say `PinGetCount()` includes SystemGround, and examples conflict between `0..Count-1` and `1..Count`. This code likely excludes either system ground intentionally or the last real pin accidentally. If no named pins are found, `List` is never seeded but still stringified.

Recommendation: Verify CEETIS pin address bounds on a known project and document the chosen range. Add a `CreatedList` guard and return `''` when no named pins are found. Consider testing whether `PinCreateList(AllNamedPins, PIN_Name, '*')` can replace the manual scan.

### MEDIUM: `get_named_pin_list()` always seeds `FromPin` even if unnamed
Location: `multipin_highvoltage(3).ats`: 653-683

The function is documented as returning named pins, but it seeds the result with `FromPin` before checking the pin's name. It then calls `PinsInRange(..., IncludeFromPin=FALSE, IncludeToPin=TRUE)`. This can include an unnamed `FromPin` or a pin that should have been filtered out.

Recommendation: Use `PinsInRange(..., TRUE, TRUE)` and the same first-valid-pin seeding logic used elsewhere. Remember that `PinsInRange` is documented as incompatible with adapter-cable-library projects.

### MEDIUM: `no_conn_hv_lists()` and `no_conn_db_lists()` do not capture pass/fail
Location: `multipin_highvoltage(3).ats`: 940-970 and 1150-1180

Both group wrappers call the built-in group test and then unconditionally call `timer_fails_check()` and `set_guard_tested()`. They do not capture the boolean return from `NoConnGroupDB/HV`, so they cannot update `AllPassed`, log the exact group failure, or avoid marking a guard as tested after a skipped/failed setup.

Recommendation: Assign `TestPassed = NoConnGroup...(...)`; set aggregate status/logging based on `TestPassed`. Keep `timer_fails_check()` after failures or after the whole group depending on the timer behavior you want.

### MEDIUM: `no_conn_db_lists()` defines `PinHigh`/`PinLow` but does not use them
Location: `multipin_highvoltage(3).ats`: 940-966

`no_conn_db_lists()` calls `PinDefineList(PinHigh, HighList)` and `PinDefineList(PinLow, LowList)`, but passes `HighList` and `LowList` to `NoConnGroupDB`. `no_conn_hv_lists()` passes `PinHigh` and `PinLow`. This inconsistency is probably harmless if the inputs are already valid arrays, but it is a maintenance trap.

Recommendation: Either remove the redundant `PinDefineList()` calls or pass `PinHigh`/`PinLow` consistently.

### MEDIUM: `isolation_test_lv_guard()` skips the same option gate used elsewhere
Location: `multipin_highvoltage(3).ats`: 1880-1907

`no_conn_lv_abort()` calls `test_lv_option()` before `IsolationTestLV()`, but `isolation_test_lv_guard()` does not check whether LV isolation is available/active before calling `no_conn_lv_list()`. This makes failures later and less explicit.

Recommendation: Call `test_lv_option()` before constructing/running the LV guard list, or document that callers must do it first.

### MEDIUM: `test_wires_guard()` duplicates behavior that built-in `TestWires()` already provides
Location: `multipin_highvoltage(3).ats`: 835-906

The built-in `TestWires()` tests the wires of the netlist and returns through CEETIS's normal reporting/fail-counter behavior. The custom implementation manually enumerates networks and calls `WireTest()` per primary-secondary pair. That may be intentional for guard bookkeeping, but it increases risk of missing CEETIS edge cases and currently calls `timer_fails_check()` both inside `wire_test_guard()` and again in `test_wires_guard()`.

Recommendation: For the standard netlist-wire test path, consider wrapping `TestWires()` with a fail-counter snapshot and then `set_guard_tested('CONTINUITY')`. Keep the manual path only if it is explicitly needed for a custom pairwise network behavior.

### LOW: Duplicate `check_job_whitelist()` definitions
Location: `NortechTestStart_RS(3).ats`: 12 and `NortechUtil_RS(3).ats`: 225

The same function name appears in two uploaded units. If both are loaded into one CEETIS context, the behavior depends on CEETIS name-resolution/last-loaded rules.

Recommendation: Keep one canonical implementation or rename the test-start-specific wrapper.

### LOW: `timer_check_fails()` and `timer_fails_check()` both exist
Location: `NortechUtil_RS(3).ats`: 1265 and 1827

The top comment/prototype section lists `timer_check_fails`, while `multipin_highvoltage` calls `timer_fails_check`. Both functions exist and do nearly the same thing. This is not immediately broken, but it is easy to call the wrong one or update only one.

Recommendation: Consolidate to one name and leave a temporary compatibility wrapper if older scripts call the other name.

### LOW: String/list conversion churn is high
Location: `multipin_highvoltage(3).ats`: recurring pattern

Several functions create a pin list, stringify it, split it back into a list, clean it, and stringify again. CEETIS built-ins already operate on `tpinarray`/`tcreatearray` for most of these tests. The churn increases runtime, stale-list risk, and debugging noise.

Recommendation: Keep arrays as arrays for logic. Convert to strings only at the UI/report boundary.

## Better built-in routes to consider
- **Use `TestWires()` for standard continuity-netlist validation:** If the intent is simply to run CEETIS's normal wire testing, `TestWires()` is safer than custom network enumeration. Wrap it with fail-counter snapshots and guard bookkeeping if needed.
- **Use `NoConnGroupHV/DB/LV` for class-to-class isolation:** Where the intent is 'these pins must not connect to those pins', group commands are more efficient than iterating `NoConnAll*` pin-by-pin. They are not equivalent to 'each pin must not connect to any other pin', so do not substitute blindly.
- **Use `IsolationGroupTestLV/HV` and `DielectricBreakdownGroupTest` only for matching workflows:** The docs say these are automatic group tests and only adequate for small UUTs. They also respect run-parameter exclusions. They may not cover the custom 'unpopulated fixture contact' guard intent.
- **Use `NWCreatePinlist()` return count:** It already gives a count. Avoid stringifying an empty/stale list.
- **Use `ReportWriteMeasurementParameters()` after `Param...` changes:** The calls are currently commented out in the high-voltage/DB populated helpers. Restoring them would make parameter changes audit-visible.
- **Use explicit component constants instead of numeric ranges:** The command docs define allowed component constants; use those constants to avoid enum drift.
- **Consider `PinGroupSetHighLow()` for manual matrix state setup:** If future code needs to explicitly drive pin groups before custom measurements, this built-in is relevant and validates voltage limits when voltage is provided.

## Suggested remediation order
1. Fix the return-type mismatch around `NoConnAllLV/HV/DB` wrappers.
2. Fix `no_conn_db_current()` naming/call target.
3. Move `ParamIsolationHVCurrent`, `ParamIsolationHV`, and `ParamDielectricBreakdown` before the first pass in the populated helpers, unless the split configuration is intentional.
4. Rewrite `strip_list_empty_string()` and the accumulator-building helpers to avoid stale/uninitialized lists.
5. Fix the discarded `strip_list_empty_string()` return values.
6. Fix RS232/timer functions that declare return values without setting `Result`, especially `timer_set()`'s bad `timer_disp_str()` call.
7. Replace numeric component loops with explicit component constants.
8. Add a small known-netlist validation script/project to verify pin-list helper outputs before using this in production tests.

## Unverified items
- Whether CEETIS maps `boolean` test returns to the same integer values as `TESTSTEP_*`. The docs do not state that, so I treated it as unsafe.
- Whether user-defined ATS functions support default parameters reliably across your CEETIS version. These files use defaults heavily.
- Whether `PinCreateList(..., PIN_Name, '*')` behaves as a wildcard all-named-pins query. It is a candidate simplification but needs a small CEETIS test.
- Exact pin address bounds for `PinGetCount()` in your CEETIS install. The extracted examples are inconsistent.
- Whether `MiscAddLists(ResultList, ResultList, OtherList)` is safe when the result and input are the same variable. The docs do not guarantee alias-safe behavior.
