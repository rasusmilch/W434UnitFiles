# CANRxTest

## Declaration

```ats
function CANRxTest(Name: string; Controller: integer; RxIdentifier: integer; CallbackFunction: tfunction; Timeout: ttime = 0s; Text: string = ''; File: string = ''): integer;
```

## Call pattern

```ats
CANRxTest('Name', <Controller>, $<RxIdentifier>, <callbackfunction>, <Timeout>s, 'Text', 'File');
```

## Description

Receives data from a CAN bus and tests whether they are right or wrong.

## Metadata

- Category: CAN bus
- Code: 2816
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string` — Custom name for the test
- `Controller`: `integer` — Number of the controller
; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `RxIdentifier`: `integer` — Identifier whose data shall be tested
; Allowed values: CAN_AllIdentifiers
- `CallbackFunction`: `tfunction` — At this place the name of a function (callback function) must be passed.; This function mus be defined in the ATS program above this function call.
; The header of the function must be defined as follows:
; function can_test1(Name: string; Controller: integer; Identifier: integer;; DataLength: integer; Data: tarray; var Pass: boolean; var Fail: boolean): void;

- `Timeout`: `ttime = 0s` — Time after whicht the test will be counted as failed (Is ignored if AutoStart is enabled)
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

   //...

   CANRxTest('Test 1', 1, CAN_AllIdentifiers, can_test1, 10s);

   //...

end;
```

## Example notes

In the example is tested whether the second byte of a received data frame has the value $10.

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

## See also

`CANControllerInit`, `CANControllerStart`, `CANGetError`, `CANISO15765TxRxTest`, `CANTxRxTest`
