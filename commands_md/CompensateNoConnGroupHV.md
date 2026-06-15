# CompensateNoConnGroupHV

## Declaration

```ats
function CompensateNoConnGroupHV(Name: string; HighGroupName: string; HighGroup: tpinarray; LowGroupName: string; LowGroup: tpinarray): void;
```

## Call pattern

```ats
CompensateNoConnGroupHV('Name', 'HighGroupName', HighGroup, 'LowGroupName', LowGroup);
```

## Description

If the resistance of the adaption adulerates a HV isolation measurement this adaption resistance must be compensated.
This is achieved by executing a compensation measurement for every HV isolation test.
With this function a compensation measurement for NoConnGroupHV functions can be done.
A compensation measurement is needed for every NoConnGroupHV function.

Notice 1: The compensation does only work if the test system is equipped with a SinglePoint matrix.

Notice 2: All connectors which are connected to the pins to be tested must be in the same state during the compensation as during the test.

Notice 3: The same measurement parameters must be used for the compensation as for the test.

Some parameters are adjusted by CEETIS for this test step. Theses are:

Wait time: At least 200ms

Measurement time: At least 2s

Measurement time reduction off

Measurement tim factor for search: 1

Automatic ranging enabled

## Metadata

- Category: Compensation
- Code: 271872
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `HighGroupName`: `string`
- `HighGroup`: `tpinarray`
- `LowGroupName`: `string`
- `LowGroup`: `tpinarray`

## Example

```ats
if (NOT CompensationValuesHVLoaded())
begin
   UIInfoDialog('Disconnect UUT');
   CompensateNoConnGroupHV('Compensation', 'My High Group', ["1", "3"], 'My Low Group', ["2", "4"]);
   CompensationValuesHVSave();
   UIInfoDialog('Connect UUT');
end;
NoConnGroupHV('Test', 'My High Group', ["1", "3"], 'My Low Group', ["2", "4"]);
```

## See also

`CompensationValuesHVLoaded`, `CompensationValuesHVSave`, `NoConnGroupHV`
