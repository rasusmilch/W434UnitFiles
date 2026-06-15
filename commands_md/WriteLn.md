# WriteLn

## Declaration

```ats
function WriteLn(Text: string): void;
```

## Call pattern

```ats
WriteLn('Text');
```

## Description

Writes a text into the report and adds a CarriageReturn/LineFeed.

## Metadata

- Category: Report output
- Code: 262145
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Report generation program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
WriteLn('Hello world');
```

## See also

`Write`
