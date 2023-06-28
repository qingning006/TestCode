@echo off
cd /d %~dp0
pyinstaller -w -F -n calculator.exe calculator.py

pause