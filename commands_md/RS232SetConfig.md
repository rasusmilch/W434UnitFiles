# RS232SetConfig

## Declaration

```ats
function RS232SetConfig(Port: integer; Baudrate: integer; DataBits: integer; Parity: integer; StopBits: integer; RtsCts: boolean; XonXoff: boolean): boolean;
```

## Call pattern

```ats
RS232SetConfig(Port, Baudrate, DataBits, RS232_Parity?, StopBits, RtsCts, XonXoff);
```

## Description

Configures the RS232-Port "Port".

## Metadata

- Category: RS232
- Code: 267010
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Port`: `integer` — Allowed values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
- `Baudrate`: `integer` — Allowed values: 75, 110, 134, 150, 300, 600, 1200, 1800, 2400, 4800, 7200, 9600, 14400, 19200, 38400, 57600, 115200, 128000
- `DataBits`: `integer` — Allowed values: 4, 5, 6, 7, 8
- `Parity`: `integer` — Allowed values: RS232_ParityNone, RS232_ParityOdd, RS232_ParityEven, RS232_ParityMark, RS232_ParitySpace
- `StopBits`: `integer` — Allowed values: RS232_OneStopBit, RS232_OneFiveStopBits, RS232_TwoStopBits
- `RtsCts`: `boolean` — Allowed values: TRUE, FALSE
- `XonXoff`: `boolean` — Allowed values: TRUE, FALSE

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
if (RS232SetConfig(1, 9600, 8, RS232_ParityNone, 1, TRUE, FALSE))
begin
   UIWriteNormal('Configuration for COM1 set');
end
else
begin
   ErrorCode = RS232GetError();
   UIWriteNormal(StrAdd('Error code: ', ErrorCode));
end;
```

## See also

`RS232Close`, `RS232GetError`, `RS232Open`, `RS232ReceiveString`, `RS232SendString`, `RS232SetParity`, `RS232SetTimeout`
