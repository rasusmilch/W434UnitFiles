# ContactSetAbsOff

## Declaration

```ats
function ContactSetAbsOff(Contact: tcontactabs): void;
```

## Call pattern

```ats
ContactSetAbsOff("X.Y");
```

## Description

Turns the absolutely addressed contact "X.Y" off.

## Metadata

- Category: Contact Access
- Code: 264725
- Visible in alphabetical index: yes
- Deprecated: yes
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Contact`: `tcontactabs`

## Example

```ats
ContactSetAbsOn("15.a1");
DTWait(3s);
ContactSetAbsOff("15.a1");
```

## See also

`ContactResetAll`, `ContactSetOff`, `ContactSetTPOff`
