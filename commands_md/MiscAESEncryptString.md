# MiscAESEncryptString

## Declaration

```ats
function MiscAESEncryptString(Data, KeyWord: string; KeyLength, AESMode, OutputFormat: integer; UsePadding, UseUniCode: boolean; InitializationVector: string = ''): string;
```

## Call pattern

```ats
MiscAESEncryptString('Data', 'KeyWord', AES_KeyLength_?, AES_Mode_?, AES_OutputFormat_?, TRUE|FALSE, TRUE|FALSE);
```

## Description

Encrypts a string with the AES algorithm

## Metadata

- Category: Miscellaneous
- Code: 266522
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data`: `string`
- `KeyWord`: `string`
- `KeyLength`: `integer` — Allowed values: AES_KeyLength_128, AES_KeyLength_192, AES_KeyLength_256
- `AESMode`: `integer` — Allowed values: AES_Mode_ECB, AES_Mode_CBC, AES_Mode_OFB, AES_Mode_CTR
- `OutputFormat`: `integer` — Allowed values: AES_OutputFormat_BASE64, AES_OutputFormat_HEXA, AES_OutputFormat_BASE64URL, AES_OutputFormat_BASE32
- `UsePadding`: `boolean` — Allowed values: TRUE, FALSE
- `UseUniCode`: `boolean` — Allowed values: TRUE, FALSE
- `InitializationVector`: `string = ''`

## Example

```ats
   Value = 'Hello World';
   Value = MiscAESEncryptString(Value, '01234567890123456789012345678901', AES_KeyLength_256, AES_Mode_CBC, AES_OutputFormat_BASE64, TRUE, TRUE);
   UIWriteNormal(Value);
   Value = MiscAESDecryptString(Value, '01234567890123456789012345678901', AES_KeyLength_256, AES_Mode_CBC, AES_OutputFormat_BASE64, TRUE, TRUE);
   UIWriteNormal(Value);
```

## See also

`MiscAESDecryptString`
