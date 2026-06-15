# RS232SetParity

## Declaration

```ats
function RS232SetParity(Port: integer; Parity: integer): boolean;
```

## Call pattern

```ats
RS232SetParity(Port, RS232_Parity?);
```

## Description

Changes the parity for the RS232-Port "Port".

## Metadata

- Category: RS232
- Code: 267011
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Port`: `integer` — Allowed values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
- `Parity`: `integer` — Allowed values: RS232_ParityNone, RS232_ParityOdd, RS232_ParityEven, RS232_ParityMark, RS232_ParitySpace

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
if (RS232SetParity(1, RS232_ParitySpace))
begin
   UIWriteNormal('Parity for COM1 set');
end
else
begin
   ErrorCode = RS232GetError();
   UIWriteNormal(StrAdd('Error code: ', ErrorCode));
end;
```

## See also

`RS232Close`, `RS232GetError`, `RS232Open`, `RS232ReceiveString`, `RS232SendString`, `RS232SetConfig`, `RS232SetTimeout`
