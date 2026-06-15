# GenVoltageOn

## Declaration

```ats
function GenVoltageOn(StimBus: integer; Voltage: tvoltage; MaxCurrent: tcurrent): integer;
```

## Call pattern

```ats
GenVoltageOn(STIMBUS_?, <Voltage>V, <Current>mA);
```

## Description

Switch on voltage on stimbus:

The parameters for the measurement are:

If you stimulate on the U2- or U3-bus be aware that there is a 6.25 kOhm-resistor in parallel to the UUT.
In addition a fraction of the current will flow through a voltage monitoring unit.

Trise=20ms


## Metadata

- Category: Generators
- Code: 270080
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `StimBus`: `integer` — Allowed values: STIMBUS_Force, STIMBUS_U2, STIMBUS_U3
- `Voltage`: `tvoltage`
- `MaxCurrent`: `tcurrent`

## Return value

Possible values:

TRUE, FALSE, EXTVOLTAGE,Uon_RESULT_ARC

## Example

```ats
Result = GenVoltageOn(STIMBUS_Force, 100V, 10mA);

switch (Result)
begin
   case (TRUE):
   begin
      UIInfoDialog('Voltage on');
   end;
   case (FALSE):
   begin
      UIInfoDialog('Voltage < 100');
   end;
   case (EXTVOLTAGE):
   begin
      UIInfoDialog('External voltage');
   end;
   case (Uon_RESULT_Arc):
   begin
      UIInfoDialog('ARC');
   end;
   default:
   begin
      UIInfoDialog('Error');
   end;
end;

GenVoltageOff(STIMBUS_Force);
UIInfoDialog('Voltage off');
```

## See also

`GenCurrentOn`, `GenVoltageOff`
