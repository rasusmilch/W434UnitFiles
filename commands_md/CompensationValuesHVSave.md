# CompensationValuesHVSave

## Declaration

```ats
function CompensationValuesHVSave(): void;
```

## Call pattern

```ats
CompensationValuesHVSave();
```

## Description

This function saves the measured compensation values to a files which has the same name as the project file and the extension ".hvcompval".

## Metadata

- Category: Compensation
- Code: 271874
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

`CompensateNoConnGroupHV`, `CompensationValuesHVLoaded`, `NoConnGroupHV`
