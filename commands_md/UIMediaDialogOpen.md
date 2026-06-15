# UIMediaDialogOpen

## Declaration

```ats
function UIMediaDialogOpen(Text: string; Filename: string; Repeat: boolean=FALSE): void;
```

## Call pattern

```ats
UIMediaDialogOpen('Text', 'Filename', Repeat);
```

## Description

Opens a non-modal media pop-up window.

## Metadata

- Category: Userinterface Access
- Code: 263968
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`
- `Filename`: `string` — File picker parameter
- `Repeat`: `boolean=FALSE` — Allowed values: TRUE, FALSE

## Example

```ats
UIMediaDialogOpen('Information', '.\Images\CEETIS_SplashScreen.jpg');
DTWait(3s);
UIMediaDialogClose();
```

## See also

`UIMediaDialogClose`, `UIMediaDialogCustom`, `UIMediaDialogOk`, `UIMediaDialogOkCancel`, `UIMediaDialogYesNo`, `UIMediaDialogYesNoCancel`
