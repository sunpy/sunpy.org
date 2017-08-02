#!/bin/sh

if [[ $(git status -s) ]]
then
    echo "The working directory is dirty. Please commit any pending changes."
    exit 1;
fi

echo "Deleting old publication"
rm -rf _build
mkdir _build
git worktree prune
rm -rf .git/worktrees/_build

echo "Checking out gh-pages branch into public"
git worktree add -B gh-pages _build/ origin/gh-pages

echo "Removing existing files"
rm -rf _build/*

echo "Generating site"
make html

echo "Updating gh-pages branch"
cd _build/html && git add --all && git commit -m "Publishing to gh-pages (publish.sh)"
git push --force origin gh-pages
