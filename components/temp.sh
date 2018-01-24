#!/bin/bash

if [ $# < 2 ]; then
echo temp.sh "name" "note"
exit -1
else
cp tmp "$1.py" -f
sed -i "s/{name}/$1/g" "$1.py"
sed -i "s/{note}/$2/g" "$1.py"
vim "$1.py"
fi
