@echo off

setlocal
set PYTHON_CMD=python
if exist %~dp0python.bat set PYTHON_CMD=call %~dp0python.bat

if not exist %~dp0.venv (
    %PYTHON_CMD% -m venv %~dp0.venv
    if exist %~dp0requirements.txt (%~dp0.venv\Scripts\python.exe -m pip install -r %~dp0requirements.txt)
)