# LocalText

## Declaration

```ats
function LocalText(Text: string): string;
```

## Call pattern

```ats
LocalText('Text');
```

## Description

Returns a localized text in the language which is set in CEETIS.

## Metadata

- Category: Localized Texts
- Code: 267776
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
UIWriteNormal(LocalText('27#Continuity test'));
```
