# ContactSetOn

## Declaration

```ats
function ContactSetOn(Contact: tcontact): void;
```

## Call pattern

```ats
ContactSetOn("Contact");
```

## Description

Turns the contact "Contact" on.

## Metadata

- Category: Contact Access
- Code: 264722
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

`ContactGroupSetOn`, `ContactResetAll`, `ContactSetOff`, `ContactSetTPOn`
