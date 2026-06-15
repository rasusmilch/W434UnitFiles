# ProjectGetCounterValue

## Declaration

```ats
function ProjectGetCounterValue(Counter: integer): integer;
```

## Call pattern

```ats
ProjectGetCounterValue(Counter);
```

## Description

Returns the current value of a project counter.

## Metadata

- Category: Project Data
- Code: 268298
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Counter`: `integer` — The custom counters can be accessed by using the values 1 - 8.; Allowed values: PROJECTCOUNTER_Test, PROJECTCOUNTER_Pass, PROJECTCOUNTER_Fail, 1, 2, 3, 4, 5, 6, 7, 8

## Return value

Returns -1 if the counter does not exist.

## Example

```ats
TestCount = ProjectGetCounterValue(PROJECTCOUNTER_Test);
UIWriteNormal(TestCount);
```

## See also

`ProjectGetFilename`, `ProjectGetName`, `ProjectSetCounterValue`
