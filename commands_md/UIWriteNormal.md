# UIWriteNormal

## Declaration

```ats
function UIWriteNormal(Text: string): void;
```

## Call pattern

```ats
UIWriteNormal('Text');
```

## Description

Writes a text in normal color to the output field of the test environment.

## Metadata

- Category: Userinterface Access
- Code: 263959
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
UIWriteNormal('Hello world');
```

## See also

`UIClearScreen`, `UIWriteError`, `UIWriteWarning`
