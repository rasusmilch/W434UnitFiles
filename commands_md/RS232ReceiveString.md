# RS232ReceiveString

## Declaration

```ats
function RS232ReceiveString(Port: integer; var Data: string): boolean;
```

## Call pattern

```ats
RS232ReceiveString(Port, Data);
```

## Description

Receives a string from RS232-Port "Port" and returns it in "Data".

## Metadata

- Category: RS232
- Code: 267013
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Port`: `integer` — Allowed values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
- `var Data`: `string`

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

`RS232Close`, `RS232GetError`, `RS232Open`, `RS232SendString`, `RS232SetConfig`, `RS232SetParity`, `RS232SetTimeout`
