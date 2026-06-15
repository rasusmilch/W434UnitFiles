# ProjectGetSectionCount

## Declaration

```ats
function ProjectGetSectionCount(): integer;
```

## Call pattern

```ats
ProjectGetSectionCount();
```

## Description

Returns the number of sections in the current project.

## Metadata

- Category: Project Data
- Code: 268300
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

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

`ProjectGetFilename`, `ProjectGetName`, `ProjectGetSectionName`, `ProjectSectionEnabled`
