# RemoteSetOutput

## Declaration

```ats
function RemoteSetOutput(Card: integer; State: tintegerarray): void;
```

## Call pattern

```ats
RemoteSetOutput(Card, State);
```

## Description

Sets the state of the ports of a remote card.
The values in the array represent the intended state of the ports in increasing order, beginning with the first port at the first array position.

## Metadata

- Category: Remote Interface Access
- Code: 268801
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Card`: `integer` — Number of the remote card.
- `State`: `tintegerarray` — Contains the states of the ports.
; The values can be ON, OFF or IGNORE.

## Example

```ats
RemoteSetOutput(1, [ON, OFF, IGNORE, ON, OFF, IGNORE, ON, OFF]);
```

## See also

`RemoteGetInput`
