# UIScreenOutputAllowed

## Declaration

```ats
function UIScreenOutputAllowed(TeststepPassed: boolean): boolean;
```

## Call pattern

```ats
UIScreenOutputAllowed(TRUE|FALSE);
```

## Description

The function determines, depending on the passed value and the settings in the "Output" menu, whether screen output is allowed or not.

## Metadata

- Category: Userinterface Access
- Code: 263983
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `TeststepPassed`: `boolean`

## Return value

The function returns TRUE if screen output is allowed, otherwise FALSE.

## Example

```ats
Allowed = UIScreenOutputAllowed(TRUE);
if (Allowed)
begin
   UIWriteNormal('Passed');
end;
```

## See also

`UIWriteError`, `UIWriteNormal`, `UIWriteWarning`
