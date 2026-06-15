# GlobalDataDeleteSection

## Declaration

```ats
function GlobalDataDeleteSection(Section: string = 'CEETIS'): void;
```

## Call pattern

```ats
GlobalDataDeleteSection('Section');
```

## Description

Deletes the passed section with all keys and data from the global data list.

## Metadata

- Category: Global data
- Code: 269828
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Section`: `string = 'CEETIS'`

## Example

```ats
GlobalDataWrite('MyKey 1', 'MyValue 1', 'MySection');
GlobalDataWrite('MyKey 2', 'MyValue 2', 'MySection');
GlobalDataDeleteSection('MySection');
KeyCount = GlobalDataGetKeys(Keys);
UIWriteNormal(KeyCount);
```

## See also

`GlobalDataClear`, `GlobalDataDeleteKey`, `GlobalDataGetKeys`, `GlobalDataRead`, `GlobalDataWrite`
