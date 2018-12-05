#!/usr/bin/env bash

if [ "$1" ];
then
    msg=$1
else
    msg=`date +%Y%m%d_%H%M%S`
fi

git checkout -b "$msg"
git add .
git commit -m "$msg"
git push origin "$msg"
git checkout master
