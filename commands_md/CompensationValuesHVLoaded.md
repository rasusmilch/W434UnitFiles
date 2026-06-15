# CompensationValuesHVLoaded

## Declaration

```ats
function CompensationValuesHVLoaded(): boolean;
```

## Call pattern

```ats
CompensationValuesHVLoaded();
```

## Description

This function returns TRUE, if compensation values for the HV isolation test were loaded, otherwise FALSE.

## Metadata

- Category: Compensation
- Code: 271873
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

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

`CompensateNoConnGroupHV`, `CompensationValuesHVSave`, `NoConnGroupHV`
