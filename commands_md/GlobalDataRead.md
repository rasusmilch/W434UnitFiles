# GlobalDataRead

## Declaration

```ats
function GlobalDataRead(Key: string; Default: string; Section: string = 'CEETIS'): string;
```

## Call pattern

```ats
GlobalDataRead('Key', 'Default', 'Section');
```

## Description

Returns the value of "Key" in the section "Section" of the global data list.

## Metadata

- Category: Global data
- Code: 269825
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Key`: `string`
- `Default`: `string`
- `Section`: `string = 'CEETIS'`

## Return value

The value of "Default" is returned if section or key do not exists.

## Example

```ats
GlobalDataWrite('MyKey 1', 'MyValue 1');
GlobalDataWrite('MyKey 2', 'MyValue 2');
GlobalDataWrite('MyKey 3', 'MyValue 3');
GlobalDataWrite('MyKey 4', 'MyValue 4');
GlobalDataDeleteKey('MyKey 3');
KeyCount = GlobalDataGetKeys(Keys);
for Zaehl = 1 to KeyCount do
begin
   Value = GlobalDataRead(Keys[Zaehl], '');
   Line = StrAdd(Keys[Zaehl], ': ');
   Line = StrAdd(Line, Value);
   UIWriteNormal(Line);
end;
GlobalDataClear();
```

## See also

`GlobalDataClear`, `GlobalDataDeleteKey`, `GlobalDataDeleteSection`, `GlobalDataGetKeys`, `GlobalDataGetOrderNumber`, `GlobalDataGetSerialNumber`, `GlobalDataWrite`
