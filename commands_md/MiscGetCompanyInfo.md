# MiscGetCompanyInfo

## Declaration

```ats
function MiscGetCompanyInfo(var CompanyName, CompanyLogo: string; var CompanyLogoWidth, CompanyLogoHeight: integer): void;
```

## Call pattern

```ats
MiscGetCompanyInfo(CompanyName, CompanyLogo, CompanyLogoWidth, CompanyLogoHeight);
```

## Description

Returns the specified company information:

Company name, company logo, width of the logo in pixels, height of the logo in pixels

The company name can be set in the configuration at "Test station->General"

The company logo can be set in teh configuration at "Test station->Files and Directories"

## Metadata

- Category: Miscellaneous
- Code: 266519
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `var CompanyName`: `string`
- `CompanyLogo`: `string`
- `var CompanyLogoWidth`: `integer`
- `CompanyLogoHeight`: `integer`

## Example

```ats
CompanyName = '';
CompanyLogo = '';
CompanyLogoWidth = 0;
CompanyLogoHeight = 0;
MiscGetCompanyInfo(CompanyName, CompanyLogo, CompanyLogoWidth, CompanyLogoHeight);
UIWriteNormal(CompanyName);
UIWriteNormal(CompanyLogo);
UIWriteNormal(CompanyLogoWidth);
UIWriteNormal(CompanyLogoHeight);
```

## See also

`MiscGetVersion`, `MiscGetTestStationIdentifier`
