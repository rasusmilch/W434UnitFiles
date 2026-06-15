# CANControllerSetAcceptanceFilter

## Declaration

```ats
function CANControllerSetAcceptanceFilter(Controller: integer; Code: integer; Mask: integer): boolean;
```

## Call pattern

```ats
CANControllerSetAcceptanceFilter(<Controller>, <Code>, <Mask>);
```

## Description

The function sets an acceptance filter for the passed controller.
This causes that all incoming CAN messages whose identifiers do not fit the filter are rejected on the hardware layer of the controller.

## Metadata

- Category: CAN bus
- Code: 270595
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Controller`: `integer` — Number of the controller; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `Code`: `integer` — The code sets the bit pattern of the identifier; Allowed values: CAN_AcceptanceCode_All, CAN_AcceptanceCode_None
- `Mask`: `integer` — The mask determines which bits are relevant for the comparison. (1 = relevant, 0 = ignore); Allowed values: CAN_AcceptanceMask_All, CAN_AcceptanceMask_None

## Return value

The function returns TRUE if it was successfully executed, otherwise FALSE.

## Example

```ats
CANControllerSetAcceptanceFilter(1, $00000100, $FFFFFF00);
```

## Example notes

The example sets a filter which lets only pass CAN frames with the identifieres $100 to $1FF.

## See also

`CANControllerStart`, `CANGetError`, `CANRxTest`, `CANTxRxTest`
