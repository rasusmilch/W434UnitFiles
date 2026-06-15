# GenReset

## Declaration

```ats
function GenReset(ResetRouting: boolean; ResetStim: boolean; ResetMeas: boolean;ActuateGenU2: boolean; ActuateGenU3: boolean): boolean;
```

## Call pattern

```ats
GenReset(TRUE, TRUE, TRUE, FALSE, FALSE);
```

## Description

ResetRouting disconnects the generator from the matrix 

ResetStim reset the generators

ResetMeas reset the measurement units

ActuateGenU2 and ActuateGenU3 reset also the U2 and U3 generator

## Metadata

- Category: Generators
- Code: 270088
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ResetRouting`: `boolean`
- `ResetStim`: `boolean`
- `ResetMeas`: `boolean`
- `ActuateGenU2`: `boolean`
- `ActuateGenU3`: `boolean`

## Example

```ats
//The variables ResetRouting, ResetStim and ResetMeas should always be true.
//With ActuateGenU2 and ActuateGenU3 is then determined whether also the U2/U3 generator should be reset.
//All generators are disconnected from the matrix.
GenReset(TRUE, TRUE, TRUE, TRUE, TRUE);
//U2 and U3 Generator are not disconnected.
GenReset(TRUE, TRUE, TRUE, FALSE, FALSE);
```
