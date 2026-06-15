# RS232SetTimeout

## Declaration

```ats
function RS232SetTimeout(Port: integer; DataTimeout: ttime; CharTimeout: ttime): boolean;
```

## Call pattern

```ats
RS232SetTimeout(Port, <DataTimeout>ms, <CharTimeout>ms);
```

## Description

Sets the data- and character-timeout for the RS232-Port "Port".

## Metadata

- Category: RS232
- Code: 267014
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Port`: `integer` — Allowed values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
- `DataTimeout`: `ttime`
- `CharTimeout`: `ttime`

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
if (RS232SetTimeout(1, 5s, 100ms))
begin
   UIWriteNormal('Timeout set');
end
else
begin
   ErrorCode = RS232GetError();
   UIWriteNormal(StrAdd('Error code: ', ErrorCode));
end;
```

## See also

`RS232Close`, `RS232GetError`, `RS232Open`, `RS232ReceiveString`, `RS232SendString`, `RS232SetConfig`, `RS232SetParity`
