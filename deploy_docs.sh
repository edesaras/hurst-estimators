#!/bin/bash
set -e

# Build the documentation
poetry run sphinx-build -b html docs/source docs/build/html

# Go to the documentation build directory and create a .nojekyll file
cd docs/build/html
touch .nojekyll

# Initialize a new git repository and force push to the gh-pages branch
git init
git add .
git commit -m "Deploy documentation"
git remote add origin https://github.com/edesaras/hurst-estimators.git
git push --force origin master:gh-pages
