# ProjectGetSectionName

## Declaration

```ats
function ProjectGetSectionName(Index: integer): string;
```

## Call pattern

```ats
ProjectGetSectionName(Index);
```

## Description

Returns the name of the section with index "Index".

## Metadata

- Category: Project Data
- Code: 268301
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Index`: `integer`

## Example

```ats
Count = ProjectGetSectionCount();
for Section = 1 to Count do
begin
   Name = ProjectGetSectionName(Section);
   Enabled = ProjectSectionEnabled(Name);
   if (Enabled)
   begin
      State = 'enabled';
   end
   else
   begin
      State = 'disabled';
   end;
   Line = StrAdd(Name, ': ');
   Line = StrAdd(Line, State);
   UIWriteNormal(Line);
end;
```

## See also

`ProjectGetFilename`, `ProjectGetName`, `ProjectGetSectionCount`, `ProjectSectionEnabled`
