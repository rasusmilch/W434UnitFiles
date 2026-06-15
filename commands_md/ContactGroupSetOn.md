# ContactGroupSetOn

## Declaration

```ats
function ContactGroupSetOn(Contacts: tcontactarray): void;
```

## Call pattern

```ats
ContactGroupSetOn(["Contact1", "Contact2", "Contact3", ...]);
```

## Description

Turns the specified contacts on.

## Metadata

- Category: Contact Access
- Code: 264726
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

`ContactGroupSetOff`, `ContactResetAll`, `ContactSetOn`
