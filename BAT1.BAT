@ECHO OFF

:choice
set /P c=Do you want to continue [Y/N]?
if /I "%c%" EQU "Y" goto :yes
if /I "%c%" EQU "N" goto :no
goto :choice

:yes
echo "User has typed yes"
goto :continue

:no
echo "User has typed no"

:continue
pause