# PrintTextFile

## Declaration

```ats
function PrintTextFile(File: string; Printer: string = ''; FontSize: integer = 10; LeftMargin: tlength = 20mm; TopMargin: tlength = 20mm; RightMargin: tlength = 20mm; BottomMargin: tlength = 20mm; Portrait: boolean = TRUE): boolean;
```

## Call pattern

```ats
PrintTextFile('File', 'Printer', <LeftMargin>mm, <TopMargin>mm, <RightMargin>mm, <BottomMargin>mm, TRUE|FALSE);
```

## Description

Sends the specified file to a printer.

## Metadata

- Category: Printing and Archiving
- Code: 265733
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `File`: `string` — Name of the file to be printed.
- `Printer`: `string = ''` — If no printer is passed the default printer will be used.
; If a LPT or COM port ist passed instead of a printer, the file will be copied to this interface.; In this case all following parameters will be ignored.
- `FontSize`: `integer = 10` — Font size in points.
- `LeftMargin`: `tlength = 20mm`
- `TopMargin`: `tlength = 20mm`
- `RightMargin`: `tlength = 20mm`
- `BottomMargin`: `tlength = 20mm`
- `Portrait`: `boolean = TRUE` — Printing portrait (TRUE) or landscape (FALSE).; Allowed values: TRUE, FALSE

## Return value

The function returns TRUE if printer and file exist, otherwise FALSE:

## Example

```ats
PrintTextFile('.\Test.txt', '', 10, 12mm, 12mm, 12mm, 12mm, TRUE);
```
