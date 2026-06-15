# ParamSetWireTestOptimization

## Declaration

```ats
function ParamSetWireTestOptimization(OnOff: boolean): void;
```

## Call pattern

```ats
ParamSetWireTestOptimization(ON|OFF);
```

## Description

Enables or disables the WireTest optimization.

## Metadata

- Category: Parameters
- Code: 266251
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `OnOff`: `boolean`

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

`ParamGetWireTestOptimization`, `WireTest`
