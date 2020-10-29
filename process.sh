#!/bin/sh

# usage: sudo ./process.sh 200605

cd `dirname $0`

python3 add.py $1

git add .
git commit -m "."
git push -u origin master

exit 0