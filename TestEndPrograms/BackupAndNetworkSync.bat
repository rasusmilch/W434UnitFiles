@echo off
setlocal

REM Define source and backup directories
set "SOURCE_DIR=C:\Users\Public\Documents\CEETIS\TestEndPrograms"
set "NETWORK_DIR=O:\Test Eng\434\TEST LAB\TestEndPrograms"

REM Check if source directory exists
if not exist "%SOURCE_DIR%\*" (
    echo Source directory does not exist. Please verify the source path.
    
    goto End
)

REM Check network availability by attempting to list the directory contents
dir "%NETWORK_DIR%" >nul 2>&1
if errorlevel 1 (
    echo Network location is not accessible. Please check the network connection.
    
    goto End
)

REM Get current date in YYYY-MM-DD format
for /f "tokens=2 delims==" %%i in ('wmic OS Get localdatetime /value') do set datetime=%%i
set "DATE_DIR=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%"
set "BACKUP_DIR=C:\Users\Public\Documents\CEETIS\TestEndPrograms_backup\%DATE_DIR%"

REM Create backup directory
if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"

REM Move files to backup directory
move "%SOURCE_DIR%\*.*" "%BACKUP_DIR%"

REM Copy files from network to source directory
xcopy "%NETWORK_DIR%\*.*" "%SOURCE_DIR%" /D /Y

:End
endlocal
