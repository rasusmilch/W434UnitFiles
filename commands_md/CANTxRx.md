# CANTxRx

## Declaration

```ats
function CANTxRx(Name: string; Controller: integer; TxIdentifier: integer; TxData: tintegerarray; ExpectedIdentifiers: tintegerarray; Period: ttime; ReceivedData: tcreatearray; Text: string = ''; File: string = ''): integer;
```

## Call pattern

```ats
CANTxRx('Name', <Controller 1-8>, $<TxIdentifier>, [<TxData>], [$<RxIdentifier1>, $<RxIdentifier2>...], <Period>ms, ReceivedData, 'My text', '.\Images\MyFile.jpg');
```

## Description

The function sends a data fram on the CAN bus. Afterwards it receives data frames for a specified period of time.

## Metadata

- Category: CAN bus
- Code: 270601
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string` — Custom name
- `Controller`: `integer` — Number of the controller; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `TxIdentifier`: `integer` — Identifier to be sent
- `TxData`: `tintegerarray` — Data to be sent
- `ExpectedIdentifiers`: `tintegerarray` — Identifiers whose data frames shall be received
; If an empty list is passed all identifiers will be accepted.
- `Period`: `ttime` — Period in which data will be received after the transmission
- `ReceivedData`: `tcreatearray` — Variable in which the received data will be returned as a two dimensional array.
- `Text`: `string = ''` — Text which will be displayed during the reception
- `File`: `string = ''` — File which will be displayed during the reception; File picker parameter

## Return value

The return value of the function is the number of the received data frames.

The data is returned in ReceivedData as a two dimensional array.
The first index is the number of the data frame.
Single parts of the data frame can be accessed with the second index.

CAN_RX_DATA_Identifier: Identifier of the data frame (Example: ReceivedData[FrameIndex, CAN_RX_DATA_Identifier])

CAN_RX_DATA_TimeStamp: Time stamp of the data frame (Example: ReceivedData[FrameIndex, CAN_RX_DATA_TimeStamp])

CAN_RX_DATA_Rtr: Flag that indicates a remote frame. TRUE = Remote frame, FALSE = no remote frame (Example: ReceivedData[FrameIndex, CAN_RX_DATA_Rtr])

CAN_RX_DATA_DataLength: Number of data bytes (Example.: ReceivedData[FrameIndex, CAN_RX_DATA_DataLength])

CAN_RX_DATA_FirstBytePosition: First data byte (Example.: ReceivedData[FrameIndex, CAN_RX_DATA_FirstBytePosition])

Note: The index of the last data byte can be calculated with "CAN_RX_DATA_FirstBytePosition + ReceivedData[FrameIndex, CAN_RX_DATA_DataLength] - 1"

## Example

```ats
ReceivedFrames = CANTxRx('My Tx/Rx', 1, $100, [$10, $20], [$101, $201], 5s, ReceivedData);
if (ReceivedFrames == 0)
begin
   UIWriteWarning('No frames received');
end
else
begin
   for FrameIndex = 1 to ReceivedFrames do
   begin
      Identifier = StrAdd('$', FormatIntToHex(ReceivedData[FrameIndex, CAN_RX_DATA_Identifier], 8));
      TimeStamp = FormatTime(ReceivedData[FrameIndex, CAN_RX_DATA_TimeStamp]);
      if (ReceivedData[FrameIndex, CAN_RX_DATA_Rtr])
      begin
         Rtr = 'RTR';
      end
      else
      begin
         Rtr = '   ';
      end;
      DataLength = ReceivedData[FrameIndex, CAN_RX_DATA_DataLength];
      if (ReceivedData[FrameIndex, CAN_RX_DATA_Rtr])
      begin
         ByteString = StrAdd('DLC: ', DataLength);
      end
      else
      begin
         ByteString = '';
         for BytePosition = 1 to DataLength do
         begin
            Byte = StrAdd('$', FormatIntToHex(ReceivedData[FrameIndex, BytePosition], 2));
            ByteString = StrAdd(ByteString, Byte);
            ByteString = StrAdd(ByteString, ' ');
         end;
      end;
      Line = StrAdd('CANTxRx ', Identifier);
      Line = StrAdd(Line, ' ');
      Line = StrAdd(Line, TimeStamp);
      Line = StrAdd(Line, ' ');
      Line = StrAdd(Line, Rtr);
      Line = StrAdd(Line, ' ');
      Line = StrAdd(Line, ByteString);
      UIWriteNormal(Line);
   end;
end;
```

## Example notes

In this example the identifier $100 with the data bytes $10 and $20 is sent on the CAN bus first.

Afterwards the function waits for 5s for data. If data frames with the identifiers $101 or $201 are received during this period they will be displayed on the screen.

## See also

`CANRtrRx`, `CANTx`, `CANTxRxTest`
