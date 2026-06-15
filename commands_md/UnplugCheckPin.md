# UnplugCheckPin

## Declaration

```ats
function UnplugCheckPin(Pin: tpin; Silent: boolean=TRUE; Voltage: tvoltage=PARAM_UseDefault; Threshold: tresistance=PARAM_UseDefault; Trise: ttime=PARAM_UseDefault; Twait: ttime=PARAM_UseDefault; Tmeas: ttime=PARAM_UseDefault; ILimit: tcurrent=PARAM_UseDefault): tpin;
```

## Call pattern

```ats
UnplugCheckPin("Pin", TRUE|FALSE, <Voltage>V, <Threshold>Ohm, <Trise>ms, <Twait>ms, <Tmeas>ms, <Ilimit>mA);
```

## Description

Checks whether the passed pin is connected to any other pin of the test system.

The default values of the parameters are:

U=4V, Threshold=100kOhm, Trise=20ms, Twait=0ms, Tmeas=0ms, Ilimit=20mA

## Metadata

- Category: Miscellaneous
- Code: 268044
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test start program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Pin`: `tpin` — Pin to be checked.
- `Silent`: `boolean=TRUE` — TRUE: If a connection is detected, the function terminates and returns the found pin.
; FALSE: A window with the connection will be shown and the test sytsem will wait for the removal of the connection.; Allowed values: TRUE, FALSE
- `Voltage`: `tvoltage=PARAM_UseDefault` — Voltage that is used for the check.
- `Threshold`: `tresistance=PARAM_UseDefault` — Threshold up to which a connection will be detected.
- `Trise`: `ttime=PARAM_UseDefault` — Maximum rise time
- `Twait`: `ttime=PARAM_UseDefault` — Wait time
- `Tmeas`: `ttime=PARAM_UseDefault` — Measurement time
- `ILimit`: `tcurrent=PARAM_UseDefault` — Maximum current if a conenction is detected.

## Return value

If a connection was detected and not removed the address of the found pin will be returned.
If no connection was detected the function will return PINADDRESS_None.

## Example

```ats
PinCount = PinGetCount() - 1;
Found = FALSE;
for Pin = 1 to PinCount do
begin
   FoundPin = UnplugCheckPin(Pin, FALSE);
   if (FoundPin <> PINADDRESS_None)
   begin
      UIWriteNormal(StrAdd('Unplug check: ', PinGetData(FoundPin, PIN_AnyName)));
      Found = TRUE;
   end;
end;
if (Found)
begin
   UIWriteWarning('UUT not removed');
end;
```

## See also

`UnplugCheck`
