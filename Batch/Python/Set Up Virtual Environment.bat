cd /d %~dp0
for %%I in (.) do set CurrDirName=%%~nxI
set VirEnvName=%CurrDirName%_VirEnv
python -m venv %VirEnvName%
