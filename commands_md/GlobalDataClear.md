# GlobalDataClear

## Declaration

```ats
function GlobalDataClear(): void;
```

## Call pattern

```ats
GlobalDataClear();
```

## Description

Clears all global data.

## Metadata

- Category: Global data
- Code: 269827
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

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

`GlobalDataDeleteKey`, `GlobalDataDeleteSection`, `GlobalDataGetKeys`, `GlobalDataRead`, `GlobalDataWrite`
