# UIMediaDialogOk

## Declaration

```ats
function UIMediaDialogOk(Text: string; Filename: string; Repeat: boolean=FALSE): void;
```

## Call pattern

```ats
UIMediaDialogOk('Text', 'Filename', Repeat);
```

## Description

Shows an information pop-up window with an OK button.

## Metadata

- Category: Userinterface Access
- Code: 263967
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
UIMediaDialogOk('Information', '.\Images\CEETIS_SplashScreen.jpg');
```

## See also

`UIMediaDialogClose`, `UIMediaDialogCustom`, `UIMediaDialogOkCancel`, `UIMediaDialogOpen`, `UIMediaDialogYesNo`, `UIMediaDialogYesNoCancel`
