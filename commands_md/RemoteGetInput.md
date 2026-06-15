# RemoteGetInput

## Declaration

```ats
function RemoteGetInput(Card: integer; StateResult: tcreatearray): integer;
```

## Call pattern

```ats
RemoteGetInput(Card, ListVariable);
```

## Description

Returns the state of the ports of a remote card.

## Metadata

- Category: Remote Interface Access
- Code: 268800
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Card`: `integer` — Number of the remote card.
- `StateResult`: `tcreatearray` — Allowed values: integer, integer, integer, integer, integer, integer, integer, integer

## Return value

The return value of the function is the number of ports.
The values in the StateResult array are ON or OFF.
The states of the ports are stored in the array in increasing order, beginning with the first port stored at the first array position.

## Example

```ats
Count = RemoteGetInput(1, States);
for Port = 1 to Count do
begin
   Text = StrAdd('Port ', Port);
   Text = StrAdd(Text, ': ');
   if (States[Port] == ON)
   begin
      Text = StrAdd(Text, 'ON');
   end
   else
   begin
      Text = StrAdd(Text, 'OFF');
   end;
   UIWriteNormal(Text);
end;
```

## See also

`RemoteSetOutput`
