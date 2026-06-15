# MeasureVoltageCurve

## Declaration

```ats
function MeasureVoltageCurve(Pin1: tpin; Pin2: tpin; TimeList: tcreatearray; VoltageList: tcreatearray; MaxVoltage: tvoltage; Tmeas: ttime; Ttrigger: ttime):integer;
```

## Call pattern

```ats
MeasureVoltageCurve("Pin1", "Pin2", TimeList, VoltageList, <MaxVoltage>V, <Tmeas>s, <Ttrigger>s);
```

## Description

This function starts a time triggered voltage measurement.

W454 and W444: Maximum 32767 measurements

W434: Maximum 8191 measurements

## Metadata

- Category: Electrical testing
- Code: 268043
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `TimeList`: `tcreatearray` — Contains the time stamps of the single measurements.
- `VoltageList`: `tcreatearray` — Contains the measured voltage values in volts.
- `MaxVoltage`: `tvoltage` — Maximum expected voltage
- `Tmeas`: `ttime` — Total measurement time
- `Ttrigger`: `ttime` — Time interval for the single measurements.

## Return value

The function returns the number of the measurement values. 

A return value of 0 means that an error (e.g. range overflow) occurred during the measurement.

## Example

```ats
Count = MeasureVoltageCurve("1", "2", TimeList, VoltageList, 10V, 1.5s, 150ms);
Str = StrAdd('Number of measurements = ',Count);
UIWriteNormal(Str);
for Data = 1 to Count do
begin
   Str = StrAdd(TimeList[Data], '   ');
   Str = StrAdd(Str, VoltageList[Data]);
   UIWriteNormal(Str);
end;
```

## See also

`UICurvesToImage`, `UICurveToImage`, `UIDefineCurve`
