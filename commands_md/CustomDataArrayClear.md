# CustomDataArrayClear

## Declaration

```ats
function CustomDataArrayClear(Array: integer = ALL): void;
```

## Call pattern

```ats
CustomDataArrayClear(<Array>);
```

## Description

Sets one or all custom data arrays to 0

## Metadata

- Category: Global data
- Code: 269834
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Array`: `integer = ALL` — Allowed values: 1..8; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8

## Example

```ats

CustomDataArrayClear();

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

`CustomDataArrayWriteByte`, `CustomDataArrayWriteWord`, `CustomDataArrayWriteDWord`, `CustomDataArrayWriteString`, `CustomDataArrayReadByte`, `CustomDataArrayReadWord`, `CustomDataArrayReadDWord`, `CustomDataArrayReadString`
