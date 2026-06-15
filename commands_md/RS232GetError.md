# RS232GetError

## Declaration

```ats
function RS232GetError(): integer;
```

## Call pattern

```ats
RS232GetError();
```

## Description

Returns the error code of the last RS232 operation.

## Metadata

- Category: RS232
- Code: 267015
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Return value

Possible values:

RS232_Error_None, RS232_Error_NotOpen, RS232_Error_InvalidConfig, RS232_Error_Timeout, RS232_Error_InvalidPort

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

`RS232Close`, `RS232Open`, `RS232ReceiveString`, `RS232SendString`, `RS232SetConfig`, `RS232SetParity`, `RS232SetTimeout`
