# ConnectJacksToMatrix

## Declaration

```ats
function ConnectJacksToMatrix(Front: boolean; Back: boolean = FALSE): void;
```

## Call pattern

```ats
ConnectJacksToMatrix(ON|OFF);
```

## Description

The function connects the "Extern" jacks to the matrix bus or removes this connection.

The connection is automatically removed by a test step (e.g. WireTest).


## Metadata

- Category: Generators
- Code: 270099
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Front`: `boolean` — If ON is passed the front jacks will be connected to the matrix.
; They can be disconnected by passing OFF.
; W454, W484, W434 only Force, W444 only Force; Allowed values: ON, OFF
- `Back`: `boolean = FALSE` — If ON is passed the rear plugs will be connected to the matrix.
; They can be disconnected by passing OFF.
; W484; Allowed values: ON, OFF

## Example

```ats
PinSetHighLow("1", "2");
ConnectJacksToMatrix(ON);
//Do something
ConnectJacksToMatrix(OFF);
```

## See also

`PinSetHighLow`, `SetJacksEnabled`
