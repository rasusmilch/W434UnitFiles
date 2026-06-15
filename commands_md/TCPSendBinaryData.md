# TCPSendBinaryData

## Declaration

```ats
function TCPSendBinaryData(Handle: integer; Data: tintegerarray): boolean;
```

## Call pattern

```ats
TCPSendBinaryData(Handle, Data);
```

## Description

The function sends binary data over the TCP/IP connection which is specified by the passed handle.

## Metadata

- Category: TCP/IP Communication
- Code: 271367
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`
- `Data`: `tintegerarray`

## Return value

The function returns TRUE if the data was successfully sent, otherwise FALSE.

## Example

```ats
Found = TCPPing('www.weetech.de');
if (Found)
begin
   Handle = TCPConnect('www.weetech.de', 80);
   if (Handle > 0)
   begin
      TCPSetTimeout(Handle, 5s);
      Success = TCPSendBinaryData(Handle, [0, 1, 2, 3]);
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

`TCPConnect`, `TCPDisconnect`, `TCPGetError`, `TCPPing`, `TCPSendString`, `TCPReceiveBinaryData`
