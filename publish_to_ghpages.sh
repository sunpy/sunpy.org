#!/bin/sh

if [[ $(git status -s) ]]
then
    echo "The working directory is dirty. Please commit any pending changes."
    exit 1;
fi

echo "Deleting old publication"
rm -rf _build
git worktree prune
rm -rf .git/worktrees/*

echo "Checking out gh-pages branch into _build/html"
mkdir _build/html
git worktree add -B gh-pages _build/html origin/gh-pages

echo "Removing existing files"
rm -rf _build/html/*

echo "Generating site"
make html

echo "Updating gh-pages branch"
cd _build/html && git add . && git commit -m "Publishing to gh-pages (publish.sh)"
git push --force origin gh-pages
