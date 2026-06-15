# UISetTEWindowState

## Declaration

```ats
function UISetTEWindowState(WindowState: integer): void;
```

## Call pattern

```ats
UISetTEWindowState(WINDOWSTATE_?);
```

## Description

Defines TE main window state.

If the window was minimized into the taskbar notification area it can be restored by clicking the icon with the right mouse button while pressing the "Alt" key.


## Metadata

- Category: Userinterface Access
- Code: 263984
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `WindowState`: `integer` — WINDOWSTATE_MAXIMIZED: For maximizing the window to the screen
; WINDOWSTATE_MINIMIZED: For minimizing the window into the taskbar
; WINDOWSTATE_SYSTEMTRAY: For minimizing the window into the taskbar notification area
; WINDOWSTATE_NORMAL: For setting the normal window state
; Allowed values: WINDOWSTATE_NORMAL, WINDOWSTATE_MAXIMIZED, WINDOWSTATE_MINIMIZED, WINDOWSTATE_SYSTEMTRAY

## Example

```ats
UISetTEWindowState(WINDOWSTATE_SYSTEMTRAY);
IsolationTestLV();
IsolationTestHV();
UISetTEWindowState(WINDOWSTATE_NORMAL);
```
