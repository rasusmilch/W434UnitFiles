# GlobalDataGetKeys

## Declaration

```ats
function GlobalDataGetKeys(Keys: tcreatearray; Section: string = 'CEETIS'): integer;
```

## Call pattern

```ats
GlobalDataGetKeys(Keys, 'Section');
```

## Description

Fills the passed variable "Keys" with a list of all key names within the passed section of the global data list.

## Metadata

- Category: Global data
- Code: 269826
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Keys`: `tcreatearray`
- `Section`: `string = 'CEETIS'`

## Return value

Returns the number of the key names in the list.

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

`GlobalDataClear`, `GlobalDataDeleteKey`, `GlobalDataDeleteSection`, `GlobalDataRead`, `GlobalDataWrite`
