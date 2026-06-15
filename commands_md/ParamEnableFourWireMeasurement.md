# ParamEnableFourWireMeasurement

## Declaration

```ats
function ParamEnableFourWireMeasurement(OnOff: boolean): void;
```

## Call pattern

```ats
ParamEnableFourWireMeasurement(ON|OFF);
```

## Description

The four wire measurement can be switched on and off with this function.
The four wire measurement can only be enabled it the software feature "4 wire measurement" is active.
A four wire measurement can only executed on pins that are accordingly adapted and tagged in the pintable.

## Metadata

- Category: Parameters
- Code: 266250
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `OnOff`: `boolean` — Allowed values: ON, OFF

## Example

```ats
ParamEnableFourWireMeasurement(OFF);
WireTest('Wire1', "1", "2");
ParamEnableFourWireMeasurement(ON);
```

## See also

`ResistorTest`, `WireTest`
