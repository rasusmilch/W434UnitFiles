# IDDRun

## Declaration

```ats
function IDDRun(Name: string; Transmitters: tpinarray; Duration: ttime; AutomaticallyRunPretest: boolean = ON; IsolationMonitoringEnabled: boolean = OFF; ShortIdentificationEnabled: boolean = OFF): boolean;
```

## Call pattern

```ats
IDDRun('Name', ["Pin1", "Pin2", ...], <Duration>s);
```

## Description

Executes the Intermittent Defect Detection

## Metadata

- Category: Electrical testing
- Code: 4096
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Transmitters`: `tpinarray`
- `Duration`: `ttime`
- `AutomaticallyRunPretest`: `boolean = ON` — Allowed values: ON, OFF
- `IsolationMonitoringEnabled`: `boolean = OFF` — Allowed values: ON, OFF
- `ShortIdentificationEnabled`: `boolean = OFF` — Allowed values: ON, OFF

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

`IDDEnableManualTrigger`, `ParamIDD`, `ParamIDDStaticContinuity`, `ParamIDDContinuityMonitoring`, `ParamIDDIsolationMonitoring`
