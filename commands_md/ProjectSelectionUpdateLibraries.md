# ProjectSelectionUpdateLibraries

## Declaration

```ats
function ProjectSelectionUpdateLibraries(SourceLocation: string): boolean;
```

## Call pattern

```ats
ProjectSelectionUpdateLibraries('SourceLocation');
```

## Description

The function copies the libraries which are specified by the passed location to the active location.
Afterwards the new data is loaded and will be used for the next tests.

This functionality can be used to update the local libraries with the data from a server.

## Metadata

- Category: Project Selection
- Code: 264966
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Project selection program
- Count result: no
- Archive allowed: no

## Parameters

- `SourceLocation`: `string`

## Return value

The function returns TRUE if the libraries were updated, otherwise FALSE.

## Example

```ats
ProjectSelectionUpdateLibraries('Server');
```
