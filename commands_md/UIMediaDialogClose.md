# UIMediaDialogClose

## Declaration

```ats
function UIMediaDialogClose(): void;
```

## Call pattern

```ats
UIMediaDialogClose();
```

## Description

Closes a media pop-up window which was opened with UIMediaDialogOpen.

## Metadata

- Category: Userinterface Access
- Code: 263969
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
UIMediaDialogOpen('Information', '.\Images\CEETIS_SplashScreen.jpg');
DTWait(3s);
UIMediaDialogClose();
```

## See also

`UIMediaDialogCustom`, `UIMediaDialogOk`, `UIMediaDialogOkCancel`, `UIMediaDialogOpen`, `UIMediaDialogYesNo`, `UIMediaDialogYesNoCancel`
