# ProjectSetCounterValue

## Declaration

```ats
function ProjectSetCounterValue(Counter: integer; Value: integer): boolean;
```

## Call pattern

```ats
ProjectSetCounterValue(Counter, Value)
```

## Description

Sets project counter to value.

## Metadata

- Category: Project Data
- Code: 268306
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Counter`: `integer` — The custom counters can be accessed by using the values 1 - 8.; Allowed values: PROJECTCOUNTER_Pass, PROJECTCOUNTER_Fail, 1, 2, 3, 4, 5, 6, 7, 8
- `Value`: `integer` — Value greater/equal 0.

## Return value

Returns TRUE if counter is changed else returns FALSE.

## Example

```ats
ProjectSetCounterValue(PROJECTCOUNTER_Pass, 5);
```

## See also

`ProjectCounterGetValue`
