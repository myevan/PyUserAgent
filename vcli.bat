@echo off
call %~dp0venv.bat
%~dp0.venv\Scripts\python.exe %~dp0cli.py %*