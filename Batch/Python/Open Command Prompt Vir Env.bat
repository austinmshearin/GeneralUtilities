cd /d %~dp0
for %%I in (.) do set CurrDirName=%%~nxI
set VirEnvName=%CurrDirName%_VirEnv
CALL ./%VirEnvName%/Scripts/activate.bat
cmd /k