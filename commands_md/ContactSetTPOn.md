# ContactSetTPOn

## Declaration

```ats
function ContactSetTPOn(Pin: tpin): void;
```

## Call pattern

```ats
ContactSetTPOn("Pin");
```

## Description

Turns the Contact that is assigned to "Pin" on.

## Metadata

- Category: Contact Access
- Code: 264720
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Pin`: `tpin`

## Example

```ats
ContactSetTPOn("Pin1");
DTWait(3s);
ContactSetTPOff("Pin2");
```

## See also

`ContactSetTPOff`, `ContactSetOn`
