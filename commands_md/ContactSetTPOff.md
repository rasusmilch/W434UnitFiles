# ContactSetTPOff

## Declaration

```ats
function ContactSetTPOff(Pin: tpin): void;
```

## Call pattern

```ats
ContactSetTPOff("Pin");
```

## Description

Turns the Contact that is assigned to "Pin" off.

## Metadata

- Category: Contact Access
- Code: 264721
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
ContactSetTPOff("Pin1");
```

## See also

`ContactResetAll`, `ContactSetTPOn`, `ContactSetOff`
