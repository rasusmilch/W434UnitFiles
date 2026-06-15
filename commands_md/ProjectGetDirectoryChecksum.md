# ProjectGetDirectoryChecksum

## Declaration

```ats
function ProjectGetDirectoryChecksum(Directory: string; WithSubdirectories: boolean; var Checksum: string; ProjectCheckSums: tcreatearray; FileNameFilter: string = '*'): integer;
```

## Call pattern

```ats
ProjectGetDirectoryChecksum('Directory', TRUE|FALSE, Checksum, ProjectCheckSums);
```

## Description

Calculates a total checksum for all projects in the specified directory.

The checksums of the cats-file, the cnetlist-file and the parameter file of every project are used to calculate this checksum.

## Metadata

- Category: Project Data
- Code: 268309
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Directory`: `string` — Folder, in which the projects are located
- `WithSubdirectories`: `boolean` — If TRUE is passed for WithSubDirectories the subdirectories will be included.
- `var Checksum`: `string` — Variable, in which a total checksum f�r all projects will be returned
- `ProjectCheckSums`: `tcreatearray` — List variable, in which the filenames and the checksums of the projects will be returned
- `FileNameFilter`: `string = '*'` — Filter for the project filenames without extension. E.g. '*' or 'a*'

## Return value

Number of items in the list

## Example

```ats
Checksum = '';
Count = ProjectGetDirectoryChecksum('.\Projects', TRUE, Checksum, ChecksumList, '*');
UIWriteNormal(Checksum);
for Index = 1 to Count do
begin
   Line = ChecksumList[Index, 1] + ': ' + ChecksumList[Index, 2];
   UIWriteNormal(Line);
end;
```
