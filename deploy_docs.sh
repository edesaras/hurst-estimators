#!/bin/bash
set -e

# Build the documentation
poetry run sphinx-build -b html docs/source docs/build/html

# Go to the documentation build directory and create a .nojekyll file
cd docs/build/html
touch .nojekyll

git init
git config user.name "GitHub Actions"
git config user.email "actions@github.com"

# Initialize a new git repository and force push to the gh-pages branch
git add .
git commit -m "Deploy documentation"
git remote add origin https://github.com/${GITHUB_REPOSITORY}.git
git push --force "https://${GITHUB_ACTOR}:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" master:gh-pages
