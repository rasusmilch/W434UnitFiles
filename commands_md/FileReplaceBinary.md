# FileReplaceBinary

## Declaration

```ats
function FileReplaceBinary(Handle: integer; OldText: string; NewText: string; ReplaceAll: boolean = FALSE; CaseSensitive: boolean = FALSE): integer;
```

## Call pattern

```ats
FileReplaceBinary(Handle, 'OldText', 'NewText');
```

## Description

Replaces occurences of 'OldText' in the binary file specified by the handle "Handle" with 'NewText', returning the number of replacements.

ReplaceAll: specifies if all occurences of 'OldText' are replaced or only the first one.

CaseSensitive: specifies if the search for 'OldText' is case sensitive.

## Metadata

- Category: File Access
- Code: 263711
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`
- `OldText`: `string`
- `NewText`: `string`
- `ReplaceAll`: `boolean = FALSE`
- `CaseSensitive`: `boolean = FALSE`

## Example

```ats
Handle = FileOpenBinary('c:\Testdatei.bin');
if (Handle <> 0)
begin
   Date = DTDate();
   DateString = DTDateString(Date);
   FileReplaceBinary(Handle, '#Datum#', DateString);
   FileSaveAsBinary(Handle, 'C:\TestMitDatum.bin');
   FileCloseBinary(Handle);
end;
```

## See also

`FileCloseBinary`, `FileCopyToPrinter`, `FileOpenBinary`, `FileSaveAsBinary`, `FileSaveBinary`
