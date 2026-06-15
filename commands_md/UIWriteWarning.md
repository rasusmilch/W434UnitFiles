# UIWriteWarning

## Declaration

```ats
function UIWriteWarning(Text: string): void;
```

## Call pattern

```ats
UIWriteWarning('Text');
```

## Description

Writes a text in warning color to the output field of the test environment.

## Metadata

- Category: Userinterface Access
- Code: 263960
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
UIWriteWarning('Hello world');
```

## See also

`UIClearScreen`, `UIWriteError`, `UIWriteNormal`
