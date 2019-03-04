@echo off
echo Welcome Easy Control for Widget Clock
echo.
echo 1 - Start Widget Clock
echo 2 - Stop Widget Clock

set /p option=Choose which option you want:
if %option% equ 1 goto startclock
if %option% equ 2 goto stopclock

:startclock
msg * Close the CMD after starting the widget!
pythonw clock-widget.py

:stopclock
taskkill /im pythonw.exe
exit