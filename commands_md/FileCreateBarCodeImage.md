# FileCreateBarCodeImage

## Declaration

```ats
function FileCreateBarCodeImage(ConfigurationFile: string; Data: string; ImageFile: string): integer;
```

## Call pattern

```ats
FileCreateBarCodeImage('.\BarCodeConfigurations\???.bcconf', 'Data', '.\Temp\BarCodes\BarCodeImage.bmp');
```

## Description

Image files with bar codes can be created with this function.
Possible file formats are the BMP (bitmap) and the PNG (portable network graphics) format.

The required configuration files can be made in the configuration at Reports->Bar codes

## Metadata

- Category: File Access
- Code: 263706
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ConfigurationFile`: `string`
- `Data`: `string`
- `ImageFile`: `string`

## Return value

The function will return BARCODE_Error_None if the file was created.
Otherwise it will return one of the following values.

BARCODE_Error_NotInitialized: The required DLL is not loaded.

BARCODE_Error_ConfigNotFound: The configuration file was not found.

BARCODE_Error_InvalidType: The bar code type is unknown.

BARCODE_Error_InvalidData: The passed data does not fit the bar code type.

BARCODE_Error_OutputFile: The output file can not be created.

BARCODE_Error_CreateFailed: The bar code can not be created.

## Example

```ats
FileCreateBarCodeImage('.\BarCodeConfigurations\MyBarCode.bcconf', '9783161484100', '.\Temp\BarCodes\BarCode.bmp');
```
