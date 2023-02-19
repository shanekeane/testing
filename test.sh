#!/bin/sh
echo committing to: $1
echo commit name: $2
git add .
git commit -m "$2"
git remote add origin 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@github.com/shanekeane/$2.git
git remote -v
git push origin main
