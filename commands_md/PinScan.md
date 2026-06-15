# PinScan

## Declaration

```ats
function PinScan(Name: string; Pin: tpin; List: tcreatearray; FindAll: boolean = TRUE): integer;
```

## Call pattern

```ats
PinScan('Name', "Pin", List);
```

## Description

Searches with low voltage all other pins which are connected with Pin.

## Metadata

- Category: Electrical testing
- Code: 1029
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin`: `tpin`
- `List`: `tcreatearray`
- `FindAll`: `boolean = TRUE` — If FALSE is passed for this parameter only one pin will be searched.; Allowed values: TRUE, FALSE

## Return value

The function returns the number of found pins.

## Example

```ats
Count = PinScan('PinScan1', "Pin1", List);
for Counter = 1 to Count do
begin
   PinName = PinGetData(List[Counter], PIN_AnyName);
   UIWriteNormal(PinName);
end;
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_Name` | `string` | Name |
| `RES_Result` | `integer` | Result |
| `RES_ManualTest` | `boolean` | Manual test |
| `RES_Pin` | `integer` | High pin |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_ExtVoltageFound` | `boolean` | External voltage found |
| `RES_ExtVoltagePin1` | `integer` | Pin1 with external voltage |
| `RES_ExtVoltagePin2` | `integer` | Pin2 with external voltage |
| `RES_ExtVoltageValue` | `real` | Value of the external voltage |
| `RES_ExtVoltagePrefix` | `string` | Prefix of the external voltage |
| `RES_Autostart` | `boolean` | Autostart |
| `RES_Value` | `real` | Measured value in Ohm (if no pin found) |
| `RES_Prefix` | `string` | Prefix of the measured value (if no pin found) |
| `RES_LVVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_LVThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_LVTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_LVTwait` | `real` | Parameter: Wait time in seconds |
| `RES_LVTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_LVAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_LVCurrentLimit` | `real` | Parameter: Maximum current in Ampere |
| `RES_LVTmeasReduction` | `boolean` | Parameter: Measurement time reduction (Dwelltime bypass) |
| `RES_ErrorPinCount` | `integer` | Number of pins with error |
| `RES_ErrorPins[ ]` | `integer` | Addresses of the pins with error |
| `RES_Arcs[ ]` | `boolean` | Flag whether an arc occured |
| `RES_Values[ ]` | `real` | Measured values in Ohm |
| `RES_Prefixes[ ]` | `string` | Prefix for the measured values |
| `RES_OriginalPin` | `integer` | Address of the programmed pin |

## See also

`ParamIsolationLV`
