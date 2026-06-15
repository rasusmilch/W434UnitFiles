# TCPDisconnect

## Declaration

```ats
function TCPDisconnect(Handle: integer): void;
```

## Call pattern

```ats
TCPDisconnect(Handle);
```

## Description

The function disconnects the TCP/IP connection which is specified by the passed value.

## Metadata

- Category: TCP/IP Communication
- Code: 271361
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`

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

`TCPConnect`
