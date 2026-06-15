# ContactGroupSetOff

## Declaration

```ats
function ContactGroupSetOff(Contacts: tcontactarray): void;
```

## Call pattern

```ats
ContactGroupSetOff(["Contact1", "Contact2", "Contact3", ...]);
```

## Description

Turns the specified contacts off.

## Metadata

- Category: Contact Access
- Code: 264727
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Contacts`: `tcontactarray`

## Example

```ats
ContactGroupSetOn(["Contact1", "Contact2", "Contact2"]);
DTWait(3s);
ContactGroupSetOff(["Contact1", "Contact2", "Contact2"]);
```

## See also

`ContactGroupSetOn`, `ContactResetAll`, `ContactSetOff`
