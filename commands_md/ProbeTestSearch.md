# ProbeTestSearch

## Declaration

```ats
function ProbeTestSearch(Name: string; Pin: tpin): integer;
```

## Call pattern

```ats
ProbeTestSearch('Name', "Pin");
```

## Description

Tests whether a pin is connected with the probe.

For this tests the measurement parameters for the continuity test are used..

Power pins are switched off before

If the wrong pin is touched the windows system sound for "Device disconnected" is played.
If the right pin is touched the windows system sound for "Device connected" is played.

## Metadata

- Category: Electrical testing
- Code: 525
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin`: `tpin`

## See also

`ConnectionTest`, `ProbeTest`, `WireTest`
