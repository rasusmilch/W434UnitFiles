# CUPExecuteCommand

## Declaration

```ats
function CUPExecuteCommand(Program: string; Command: string; CommandParameters: tstringarray; Timeout: ttime; ResultData: tcreatearray): integer;
```

## Call pattern

```ats
CUPExecuteCommand('CEETIS_CUP_?', '<Command>', ['CommandParameter1', 'CommandParameter2', ...], <Timeout>s, ResultData]);
```

## Description

The function makes a custom utitliy program to execute a command.
During the execution of the command the current script in CEETIS will pause.
The data that has to be passed in "Command" and "CommandParameters" varies according to the used program and command.
The commands which are suppoted by a particular custom utility program can be found in the manual of that program.

Custom utility programs are optional and are not included in normal delivery.

## Metadata

- Category: Custom Utility Programs
- Code: 270848
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Program`: `string` — Name of the utility program
- `Command`: `string` — Command
- `CommandParameters`: `tstringarray` — Parameters for the command
- `Timeout`: `ttime` — Duration for waiting for an answer from the utulity program
- `ResultData`: `tcreatearray` — Result data from the utility program

## Return value

In the case of an error one of the following constants will be returned.

CUP_Result_ProgramNotFound: The utility program was not found.

CUP_Result_ProgramNotStarted: The utility program could not b executed.

CUP_Result_CommandSendError: The command could not be sent to the utility program.

CUP_Result_CommandTimeout: The utility program did not answer within the given time.
CUP_Result_NotACUP: The specifeid program is not a CUP

## Example

```ats
CommandResult = CUPExecuteCommand('CEETIS_CUP_001', 'run program',
                   ['C:\Program Files\Microsoft Office\OFFICE11\WINWORD.exe',
                    '"C:\Program Files\Microsoft Office\OFFICE11\1031\PROTTPLN.DOC"'],
                   600s, ResultData);
if (CommandResult > 0)
begin
   for Zaehl = 1 to CommandResult do
   begin
      UIWriteWarning(StrAdd(StrAdd(Zaehl, ': '), ResultData[Zaehl]));
   end;
end
else
begin
   FailCounterCount(FAILCOUNTER_Others);
   switch (CommandResult)
   begin
      case CUP_Result_ProgramNotFound: begin
         UIWriteError('Program not found');
      end;
      case CUP_Result_ProgramNotStarted: begin
         UIWriteError('Program could not be started');
      end;
      case CUP_Result_CommandSendError: begin
         UIWriteError('Command could not be sent');
      end;
      case CUP_Result_CommandTimeout: begin
         UIWriteError('Command timed out');
      end;
      case CUP_Result_NotACUP: begin
         UIWriteError('Not a CUP');
      end;
      default: begin
         UIWriteError('Unknown error');
      end;
   end;
end;
```
