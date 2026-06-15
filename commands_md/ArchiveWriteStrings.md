# ArchiveWriteStrings

## Declaration

```ats
function ArchiveWriteStrings(Text: string; Strings: tstringarray): void;
```

## Call pattern

```ats
ArchiveWriteStrings('Text', ['String1', 'String2', ...]);
```

## Description

Writes the passed texts into the archive file.

## Metadata

- Category: Data to Archive
- Code: 3072
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: yes

## Parameters

- `Text`: `string`
- `Strings`: `tstringarray`

## Example

```ats
ArchiveWriteStrings('Text', ['String1', 'String2']);
```
