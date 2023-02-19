#!/bin/sh
echo committing to: $1
echo commit name: $2
git add .
git commit -m "$2"
git remote add origin git@github.com:shanekeane/$1.git
git push -u origin master
