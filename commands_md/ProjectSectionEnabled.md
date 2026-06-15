# ProjectSectionEnabled

## Declaration

```ats
function ProjectSectionEnabled(Section: string): boolean;
```

## Call pattern

```ats
ProjectSectionEnabled('Section');
```

## Description

Returns TRUE if the section "Section" is enabled, otherwise FALSE.

## Metadata

- Category: Project Data
- Code: 268299
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Section`: `string`

## Example

```ats
if (ProjectSectionEnabled('Section 1'))
begin
   //run tests for this section
end;
```

## See also

`ProjectGetFilename`, `ProjectGetName`, `ProjectGetSectionCount`, `ProjectGetSectionName`
