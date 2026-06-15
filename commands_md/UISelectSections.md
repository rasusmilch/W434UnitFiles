# UISelectSections

## Declaration

```ats
function UISelectSections(ResetSections: boolean): void;
```

## Call pattern

```ats
UISelectSections(TRUE|FALSE);
```

## Description

Shows a window for enabling and disabling of the sections.
If the current project doesn't have sections, the window won't be displayed.

If the window is closed with the "Cancel" button the test will be aborted.

## Metadata

- Category: Userinterface Access
- Code: 263991
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ResetSections`: `boolean` — If TRUE is passed the settings will be resetted to the base state befor the window is displayed.; Allowed values: TRUE, FALSE

## Example

```ats
UISelectSections(TRUE);
```
