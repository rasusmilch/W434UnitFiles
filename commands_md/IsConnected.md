# IsConnected

## Declaration

```ats
function IsConnected(Pin1: tpin; Pin2: tpin): integer;
```

## Call pattern

```ats
IsConnected("Pin1", "Pin2");
```

## Description

Checks whether there is a connection between Pin1 and Pin2.

## Metadata

- Category: Electrical testing
- Code: 268032
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Pin1`: `tpin`
- `Pin2`: `tpin`

## Return value

Possible values:

TESTSTEP_Passed, TESTSTEP_Failed, TESTSTEP_Invalid.

## Example

```ats
Connected = IsConnected("Pin1", "Pin2");
if (Connected == TESTSTEP_Passed)
begin
   UIWriteNormal('Connected');
end
else
begin
   UIWriteNormal('Not connected');
end;
```

## See also

`ConnectionTest`, `ParamContinuity`, `WireTest`
