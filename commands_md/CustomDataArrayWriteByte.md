# CustomDataArrayWriteByte

## Declaration

```ats
function CustomDataArrayWriteByte(Array: integer; Position: integer; Value: integer): void;
```

## Call pattern

```ats
CustomDataArrayWriteByte(<Array>, <Position>, <Value>);
```

## Description

Writes one byte to the custom data array

## Metadata

- Category: Global data
- Code: 269835
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Array`: `integer` — Allowed values: 1..8; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `Position`: `integer` — Allowed values: 1..128
- `Value`: `integer` — Allowed values: $00..$FF

## Example

```ats
CustomDataArrayClear(1);

CustomDataArrayWriteByte(1, 1, 255);
CustomDataArrayWriteWord(1, 2, 65535);
CustomDataArrayWriteDWord(1, 4, 131071);
CustomDataArrayWriteString(1, 8, 'Hello world');

Value = CustomDataArrayReadByte(1, 1);
UIWriteNormal(Value);
Value = CustomDataArrayReadWord(1, 2);
UIWriteNormal(Value);
Value = CustomDataArrayReadDWord(1, 4);
UIWriteNormal(Value);
Value = CustomDataArrayReadString(1, 8, 11);
UIWriteNormal(Value);
```

## See also

`CustomDataArrayClear`, `CustomDataArrayWriteWord`, `CustomDataArrayWriteDWord`, `CustomDataArrayWriteString`, `CustomDataArrayReadByte`, `CustomDataArrayReadWord`, `CustomDataArrayReadDWord`, `CustomDataArrayReadString`
