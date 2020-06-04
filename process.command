#!/bin/sh
cd `dirname $0`

python3 add.py %1

git add .
git commit -m "."
git push -u origin master

exit