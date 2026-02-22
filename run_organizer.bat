@echo off
echo Running File Organizer...
echo.

cd /d "%~dp0"

python organize_by_type.py

echo.
echo Done.
pause