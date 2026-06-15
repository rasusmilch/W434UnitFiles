# ParamGetWireTestOptimization

## Declaration

```ats
function ParamGetWireTestOptimization(): boolean;
```

## Call pattern

```ats
ParamGetWireTestOptimization();
```

## Description

Returns whether the WireTest optimization is enabled or disabled.

## Metadata

- Category: Parameters
- Code: 266252
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
OptimizationOn = ParamGetWireTestOptimization();
ParamSetWireTestOptimization(OFF);
//...
//...
if (OptimizationOn)
begin
   ParamSetWireTestOptimization(ON);
end;
```

## See also

`ParamSetWireTestOptimization`, `WireTest`
