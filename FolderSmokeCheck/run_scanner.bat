@echo off
echo ================================
echo   Project Security Scanner
echo ================================
echo.

set /p project_path=Enter full project path to scan:

python "%~dp0security_project_scanner.py"

pause
