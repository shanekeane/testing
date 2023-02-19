#!/bin/sh
echo committing to: $1
echo commit name: $2
git add .
git commit -m "$2"
git remote add origin $1
git remote -v
git push origin main
