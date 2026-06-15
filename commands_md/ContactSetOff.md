# ContactSetOff

## Declaration

```ats
function ContactSetOff(Contact: tcontact): void;
```

## Call pattern

```ats
ContactSetOff("Contact");
```

## Description

Turns the contact "Contact" off.

## Metadata

- Category: Contact Access
- Code: 264723
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Contact`: `tcontact`

## Example

```ats
ContactSetOn("Contact1");
DTWait(3s);
ContactSetOff("Contact1");
```

## See also

`ContactGroupSetOff`, `ContactResetAll`, `ContactSetOn`, `ContactSetTPOff`
