# GenCurrentOn

## Declaration

```ats
function GenCurrentOn(StimBus: integer; Current: tcurrent; MaxVoltage: tvoltage): integer;
```

## Call pattern

```ats
GenCurrentOn(STIMBUS_?, <Current>mA, <Voltage>V);
```

## Description

Switch on current on stimbus

If you stimulate on the U2- or U3-bus be aware that there is a 6.25 kOhm-resistor in parallel to the UUT.
In addition a fraction of the current will flow through a voltage monitoring unit.


## Metadata

- Category: Generators
- Code: 270082
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `StimBus`: `integer` — Allowed values: STIMBUS_Force, STIMBUS_U2, STIMBUS_U3
- `Current`: `tcurrent`
- `MaxVoltage`: `tvoltage`

## Return value

Possible values:

TRUE, FALSE, EXTVOLTAGE

## Example

```ats
Iresult = GenCurrentOn(STIMBUS_U2, 100mA, 20V);

if (Iresult == TRUE)
begin
   UIInfoDialog('U2 on');
end;
if (Iresult == FALSE)
begin
   UIInfoDialog('U2 current < 100mA');
end;
if (Iresult == EXTVOLTAGE)
begin
   UIInfoDialog('U2 ExtVoltage');
end;

GenCurrentOff(STIMBUS_U2);
UIInfoDialog('U2 off');
```

## See also

`GenCurrentOff`, `GenVoltageOff`, `GenVoltageOn`
