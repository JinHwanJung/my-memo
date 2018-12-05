#!/usr/bin/env bash

if [ "$1" ];
then
    msg=$1
else
    msg=`date '+%Y-%m-%d %H:%M:%S'`
fi

git add .
git commit -m "$msg"
git push origin master
