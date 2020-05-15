@echo off
cd /d %~dp0

rem implement python
python add.py %1

rem git
git add .
git commit -m "."
git push -u origin master