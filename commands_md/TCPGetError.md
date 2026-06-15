# TCPGetError

## Declaration

```ats
function TCPGetError(): integer;
```

## Call pattern

```ats
TCPGetError();
```

## Description

Returns the error code of the last TCP operation.

## Metadata

- Category: TCP/IP Communication
- Code: 271366
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Return value

Possible values:

TCP_Error_None, TCP_Error_InvalidHandle, TCP_Error_NotConnected, TCP_Error_Timeout, TCP_Error_SendingFailed, TCP_Error_HostNotFound, TCP_Error_CanNotConnect

## Example

```ats
Found = TCPPing('www.weetech.de');
if (Found)
begin
   Handle = TCPConnect('www.weetech.de', 80);
   if (Handle > 0)
   begin
      TCPSetTimeout(Handle, 5s);
      Success = TCPSendString(Handle, StrAdd('GET /de/firma/index.html HTTP/1.0', CHAR_CRLF));
      if (Success)
      begin
         TCPSendString(Handle, StrAdd('Host: www.weetech.de', CHAR_CRLF));
         TCPSendString(Handle, CHAR_CRLF);
         Data = '';
         TCPReceiveString(Handle, Data);
         UIWriteNormal(Data);
      end;
      if (NOT Success)
      begin
         ErrorCode = TCPGetError();
         switch (ErrorCode)
         begin
            case TCP_Error_NotConnected: begin
               ErrorText = 'Not connected';
            end;
            case TCP_Error_SendingFailed: begin
               ErrorText = 'Sending failed';
            end;
            default: begin
               ErrorText = 'Unknown error';
            end;
         end;
         UIWriteError(StrAdd('TCP error: ', ErrorText));
      end;
      TCPDisconnect(Handle);
   end
   else
   begin
      UIWriteError('Not connected');
   end;
end
else
begin
   UIWriteError('Server not found');
end;
```

## See also

`TCPConnect`, `TCPDisconnect`, `TCPPing`, `TCPReceiveString`, `TCPSendString`
