# CANISO15765TxRxTest

## Declaration

```ats
function CANISO15765TxRxTest(Name: string; Controller: integer; TargetAddress: integer; Priority: integer; TxData: tintegerarray; Timeout: ttime; CallbackFunction: tfunction): integer;
```

## Call pattern

```ats
CANISO15765TxRxTest('Name', <Controller 1-8>, <TargetAddress $00-$FE>, <Priority 1-7>, [<TxData>], <Timeout>ms, <callbackfunction>);
```

## Description

Transmits data on the CAN bus by using the ISO15765 protocol. Afterwards the reply is received and tested whether it is right or wrong.

Autostart for CAN is ignored for this function.

## Metadata

- Category: CAN bus
- Code: 2818
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string` — Custom name for the test
- `Controller`: `integer` — Number of the controller
; The extended mode must be set for this controller.
; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `TargetAddress`: `integer` — Address of the device to which the message shall be sent. ($00 - $FE)
- `Priority`: `integer` — Priority of the message (0-7); Allowed values: 0, 1, 2, 3, 4, 5, 6, 7
- `TxData`: `tintegerarray` — Data to be sent
- `Timeout`: `ttime` — Maximum time the test system waits for a reply.
- `CallbackFunction`: `tfunction` — At this place the name of a function (callback function) must be passed.; This function mus be defined in the ATS program above this function call.
; The header of the function must be defined as follows:
; function iso15765_test1(Name: string; Controller: integer; Address: integer; Priority: integer; DataLength: integer; Data: tarray; var Pass: boolean; var Fail: boolean): void;
; The name of the callback function can be chosen freely.


## Return value

The function returns:

TESTSTEP_Passed, if the test passed

TESTSTEP_Failed, if an error was detected

TESTSTEP_Invalid, if the result of the test is invalid

TESTSTEP_NotExecuted, if the test was not executed

## Example

```ats
function kwp2000_tester_present(Name: string; Controller: integer; Address: integer;
            Priority: integer; DataLength: integer; Data: tarray;
            var Pass: boolean; var Fail: boolean): void;
begin
   if ((DataLength >= 1) AND (Data[1] == $7E))
   begin
      Pass = TRUE;
   end
   else
   begin
      Fail = TRUE;
   end;
end;

function main(): void;
begin
   UIClearScreen();

   CANControllerInit(1, CAN_Mode_Extended, CAN_Speed_250k);
   CANISO15765SetAddress($F9);
   CANControllerStart(1);
   CANISO16765TxRxTest('KWP2000 Tester present', 1, $FE, 3, [$3E, $01],
      10s, kwp2000_tester_present);
   CANControllerStop(1);
end;
```

## Example notes

The example sents the data $3E and $01 to the address $FE.
Afterwards it is tested whether the first data byte of the reply has the value $7E.

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_Name` | `string` | Name |
| `RES_Result` | `integer` | Result |
| `RES_ManualTest` | `boolean` | Manual test |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_Controller` | `integer` | CAN controller |
| `RES_Timeout` | `real` | Time in s after whicht the test will be counted as failed |
| `RES_ErrorCode` | `integer` | Errorcode |
| `RES_TargetAddress` | `integer` | Address of the device to which the message was sent. |
| `RES_TxPriority` | `integer` | Priority of the transmitted message |
| `RES_RxDataLength` | `integer` | Number of received data bytes |
| `RES_RxData[]` | `integer` | Received data bytes |
| `RES_RxDataAvailable` | `boolean` | Received data available |
| `RES_TxIdentifier` | `integer` | Identifier which was transmitted |
| `RES_TxDataLength` | `integer` | Number of data bytes that were transmitted |
| `RES_TxData[]` | `integer` | Data that was transmitted |

## See also

`CANControllerInit`, `CANControllerStart`, `CANGetError`, `CANISO15765SetTesterAddress`, `CANISO15765TxRx`, `CANTxRxTest`
