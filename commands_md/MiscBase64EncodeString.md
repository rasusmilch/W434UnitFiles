# MiscBase64EncodeString

## Declaration

```ats
function MiscBase64EncodeString(Value: string): string;
```

## Call pattern

```ats
MiscBase64EncodeString('Value');
```

## Description

Encodes a string to Base64

## Metadata

- Category: Miscellaneous
- Code: 266530
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `string`

## Example

```ats
EncodedValue = MiscBase64EncodeString('This is a text');
UIWriteNormal(EncodedValue);
```
