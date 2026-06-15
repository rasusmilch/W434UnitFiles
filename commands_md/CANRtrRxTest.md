# CANRtrRxTest

## Declaration

```ats
function CANRtrRxTest(Name: string; Controller: integer; RequestedIdentifier: integer; RequestedDataLength: integer; Timeout: ttime; CallbackFunction: tfunction; Text: string = ''; File: string = ''): integer;
```

## Call pattern

```ats
CANRtrRxTest('Name', <Controller 1-8>, $<RequestedIdentifier>, <RequestedDataLength 0-8>, <Timeout>ms, <callbackfunction>, 'Text', 'File');
```

## Description

Requests data with a RTR frame on the CAN bus. Afterwards the reply is received and tested whether it is right or wrong.

## Metadata

- Category: CAN bus
- Code: 2819
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string` — Custom name for the test
- `Controller`: `integer` — Number of the controller; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `RequestedIdentifier`: `integer` — Requested identifier
- `RequestedDataLength`: `integer` — Requested data length; Allowed values: 0, 1, 2, 3, 4, 5, 6, 7, 8
- `Timeout`: `ttime` — Time after which the test will be counted as failed (Is ignored if AutoStart is enabled)
- `CallbackFunction`: `tfunction` — At this place the name of a function (callback function) must be passed.; This function mus be defined in the ATS program above this function call.
; The header of the function must be defined as follows:
; function can_test1(Name: string; Controller: integer; Identifier: integer;; DataLength: integer; Data: tarray; var Pass: boolean; var Fail: boolean): void;
; The name of the callback function can be chosen freely.

- `Text`: `string = ''` — Text which will be displayed during the test
- `File`: `string = ''` — Name of the file which will be displayed during the test

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
   if ((DataLength == 2) AND (Data[2] == $10))
   begin
      Pass = TRUE;
   end;
end;

function main(): void;
begin
   UIClearScreen();

   CANControllerInit(1, CAN_Mode_Extended, CAN_Speed_250k);
   CANControllerStart(1);
   CANRtrRxTest('Test 1', 1, $100, 2, 10s, can_test1);
   CANControllerStop(1);
end;
```

## Example notes

The identifier $100 with two bytes of data is requested in this example.
The function tests whether an according data frame is received and whether it contains the value $10 in the second byte.

## See also

`CANControllerInit`, `CANControllerStart`, `CANGetError`, `CANRtr`, `CANRxTest`, `CANTxRxTest`
