# RS232Open

## Declaration

```ats
function RS232Open(Port: integer; Baudrate: integer; DataBits: integer; Parity: integer; StopBits: integer; RtsCts: boolean; XonXoff: boolean): boolean;
```

## Call pattern

```ats
RS232Open(Port, Baudrate, DataBits, RS232_Parity?, RS232_<StopBits>, RtsCts, XonXoff);
```

## Description

Opens the RS232-Port "Port" and configures it.

## Metadata

- Category: RS232
- Code: 267008
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
COMPortNumber = 1;
SendData = 'Some data';
IsSuccess = RS232Open(COMPortNumber, 9600, 8, RS232_ParityNone, 1, TRUE, FALSE);
if (IsSuccess)
begin
   IsSuccess = RS232SendString(COMPortNumber, SendData);
   if (IsSuccess)
   begin
      Data = '';
      IsSuccess = RS232ReceiveString(COMPortNumber, Data);
      if (IsSuccess)
      begin
         UIWriteNormal(StrAdd('Received data: ', Data));
      end;
   end;
end;
if (NOT IsSuccess)
begin
   ErrorCode = RS232GetError();
   switch (ErrorCode)
   begin
      case RS232_Error_NotOpen: begin
         Text = 'Port not open';
      end;
      case RS232_Error_InvalidConfig: begin
         Text = 'Invalid configuration';
      end;
      case RS232_Error_Timeout: begin
         Text = 'Timeout';
      end;
      case RS232_Error_InvalidPort: begin
         Text = 'Invalid port';
      end;
      default: begin
         Text = 'Unknown error';
      end;
   end;
   UIWriteError(StrAdd('Error code: ', Text));
end;
RS232Close(COMPortNumber);
```

## See also

`RS232Close`, `RS232GetError`, `RS232ReceiveString`, `RS232SendString`, `RS232SetConfig`, `RS232SetParity`, `RS232SetTimeout`
