@echo off
rem Windows: runs the show from this folder without internet. Close this window to stop.
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (py -3 serve.py) else (python serve.py)
pause
