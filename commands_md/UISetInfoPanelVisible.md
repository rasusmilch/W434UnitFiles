# UISetInfoPanelVisible

## Declaration

```ats
function UISetInfoPanelVisible(Visible: boolean): void;
```

## Call pattern

```ats
UISetInfoPanelVisible(TRUE|FALSE);
```

## Description

Specifies whether the panel is visible or not.

## Metadata

- Category: Userinterface Access
- Code: 263956
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Visible`: `boolean` — Allowed values: TRUE, FALSE

## Example

```ats
UISetInfoPanelVisible(FALSE);
DTWait(3s);
UISetInfoPanelVisible(TRUE);
```

## See also

`UIResetInfoPanel`, `UISetInfoPanelHeight`
