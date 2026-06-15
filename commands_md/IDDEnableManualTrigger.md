# IDDEnableManualTrigger

## Declaration

```ats
function IDDEnableManualTrigger(Text: string): void;
```

## Call pattern

```ats
IDDEnableManualTrigger('Display text');
```

## Description

The function enables the manual trigger for the start of the measurement.

## Metadata

- Category: Parameters
- Code: 4097
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string` — Text which can contain an explanation for the operator what to do.

## Example

```ats
ParamStopOnFail(COMMANDS_IDD, ON);

ParamIDD(OFF);
ParamIDDStaticContinuity(20, 80, 2ms, 100ms, IDD_RxAmplification_On, 200ns);
ParamIDDContinuityMonitoring(100, 80, ON, IDD_RxAmplification_On, ON, 200ns);
ParamIDDIsolationMonitoring(200, 160, PARAM_DontChange, ON, 200ns);

IDDEnableManualTrigger('Activate the shaker and click to start the test');

NWCreatePinlist(TransmitterList, COMPONENT_Wire, COMPONENTDATA_Information , '*IDD*', COMPONENTPINS_Primary, FALSE);

IDDRun('Intermittent Defect Detection', TransmitterList, 30s);
```

## See also

`ParamIDD`, `ParamIDDStaticContinuity`, `ParamIDDContinuityMonitoring`, `ParamIDDIsolationMonitoring`, `IDDRun`
