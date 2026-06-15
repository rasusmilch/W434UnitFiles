# UnplugCheck

## Declaration

```ats
function UnplugCheck(PinsToCheck: integer = UNPLUGCHECK_All; Voltage: tvoltage=PARAM_UseDefault; Threshold: tresistance=PARAM_UseDefault; Trise: ttime=PARAM_UseDefault; Twait: ttime=PARAM_UseDefault; Tmeas: ttime=PARAM_UseDefault; ILimit: tcurrent=PARAM_UseDefault): boolean;
```

## Call pattern

```ats
UnplugCheck(UNPLUGCHECK_All|UNPLUGCHECK_Named|UNPLUGCHECK_Used);
```

## Description

The function checks whether the UUT was disconnected from the test system.

The default values of the parameters are:

U=4V, Threshold=100kOhm, Trise=20ms, Twait=0ms, Tmeas=0ms, Ilimit=20mA

## Metadata

- Category: Miscellaneous
- Code: 268045
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test start program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `PinsToCheck`: `integer = UNPLUGCHECK_All` — Allowed values: UNPLUGCHECK_All, UNPLUGCHECK_Named, UNPLUGCHECK_Used
- `Voltage`: `tvoltage=PARAM_UseDefault` — Voltage that is used for the check.
- `Threshold`: `tresistance=PARAM_UseDefault` — Threshold up to which a connection will be detected.
- `Trise`: `ttime=PARAM_UseDefault` — Maximum rise time
- `Twait`: `ttime=PARAM_UseDefault` — Wait time
- `Tmeas`: `ttime=PARAM_UseDefault` — Measurement time
- `ILimit`: `tcurrent=PARAM_UseDefault` — Maximum current if a connection exists.

## Return value

The return value is TRUE if no connection was detected, otherwise FALSE.

## Example

```ats
UnplugCheckEnabled = ProjectGetTestEndSettings(TESTEND_UnplugCheck);
if (UnplugCheckEnabled)
begin
   do
   begin
      Unplugged = UnplugCheck(UNPLUGCHECK_All);
   while (NOT Unplugged);
end;
```

## See also

`UnplugCheckPin`
