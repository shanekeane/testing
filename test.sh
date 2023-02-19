#!/bin/sh
echo committing to: $1
echo commit name: $2
echo git@github.com:shanekeane/$1.git
git add .
git commit -m "$2"
git remote set-url origin git@github.com:shanekeane/$1.git
git push -u origin main
