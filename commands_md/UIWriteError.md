# UIWriteError

## Declaration

```ats
function UIWriteError(Text: string): void;
```

## Call pattern

```ats
UIWriteError('Text');
```

## Description

Writes a text in error color to the output field of the test environment.

## Metadata

- Category: Userinterface Access
- Code: 263961
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
UIWriteError('Hello world');
```

## See also

`UIClearScreen`, `UIWriteNormal`, `UIWriteWarning`
