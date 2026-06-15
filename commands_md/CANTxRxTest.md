# CANTxRxTest

## Declaration

```ats
function CANTxRxTest(Name: string; Controller: integer; TxIdentifier: integer; TxData: tintegerarray; RxIdentifier: integer; Timeout: ttime; CallbackFunction: tfunction; Text: string = ''; File: string = ''): integer;
```

## Call pattern

```ats
CANTxRxTest('Name', <Controller 1-8>, $<TxIdentifier>, [<TxData>], $<RxIdentifier>, <Timeout>ms, <callbackfunction>, 'Text', 'File');
```

## Description

Transmits data on the CAN bus. Afterwards the reply is received and tested whether it is right or wrong.

## Metadata

- Category: CAN bus
- Code: 2817
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string` — Custom name for the test
- `Controller`: `integer` — Number of the controller
; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `TxIdentifier`: `integer` — Identifier to be sent
- `TxData`: `tintegerarray` — Data to be sent
- `RxIdentifier`: `integer` — Identifier whose data shall be tested; Allowed values: CAN_AllIdentifiers
- `Timeout`: `ttime` — Time after which the test will be counted as failed (Is ignored if Autostart is enabled)
- `CallbackFunction`: `tfunction` — At this place the name of a function (callback function) must be passed.; This function must be defined in the ATS program above this function call.
; The header of the function must be defined as follows:
; function can_test1(Name: string; Controller: integer; Identifier: integer;; DataLength: integer; Data: tarray; var Pass: boolean; var Fail: boolean): void;
; The name of the callback function can be chosen freely.

- `Text`: `string = ''` — Text which will be displayed during the test
- `File`: `string = ''` — Name of the file which will be displayed during the test; File picker parameter

## Return value

The function returns:

TESTSTEP_Passed, if the test passed

TESTSTEP_Failed, if an error was detected

TESTSTEP_Invalid, if the result of the test is invalid

TESTSTEP_NotExecuted, if the test was not executed

## Example

```ats
function can_test1(Name: string; Controller: integer; Identifier: integer;
            DataLength: integer; Data: tarray;
            var Pass: boolean; var Fail: boolean): void;
begin
   if ((DataLength >= 2) AND (Data[2] == $10))
   begin
      Pass = TRUE;
   end;
end;

function main(): void;
begin
   UIClearScreen();

   CANControllerInit(1, CAN_Mode_Extended, CAN_Speed_250k);
   CANControllerStart(1);
   CANTxRxTest('Test 1', 1, $100, [$01, $02], $200, 10s, can_test1);
   CANControllerStop(1);
end;
```

## Example notes

The example sends  the identifier $100 with the data $01 and $02 on the CAN bus.
Afterwards it is tested whether the reply with identifier $200 has the value $10 in the second data byte.

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
| `RES_Text` | `string` | Text which will be displayed during the test |
| `RES_File` | `string` | Name of the file which will be displayed during the test |
| `RES_ErrorCode` | `integer` | Errorcode |
| `RES_RxIdentifier` | `integer` | Received Identifier |
| `RES_RxDataLength` | `integer` | Number of received data bytes |
| `RES_RxData[]` | `integer` | Received data bytes |
| `RES_RxDataAvailable` | `boolean` | Received data available |
| `RES_TxIdentifier` | `integer` | Identifier which was sent |
| `RES_TxDataLength` | `integer` | Number of data bytes that were sent |
| `RES_TxData[]` | `integer` | Data that was sent |

## See also

`CANControllerInit`, `CANControllerStart`, `CANGetError`, `CANISO15765TxRxTest`, `CANRtrRxTest`, `CANRxTest`
