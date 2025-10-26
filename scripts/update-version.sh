#!/bin/bash
# Update version SHA in index.html footer
# This script should be run before committing changes

set -e

# Get the current short commit SHA
SHA=$(git rev-parse --short HEAD)

echo "Updating version to $SHA..."

# Update the version SHA in index.html
sed -i "s|commit/[0-9a-f]\{7\}|commit/$SHA|g" index.html
sed -i "s|v[0-9a-f]\{7\}|v$SHA|g" index.html

echo "Version updated to $SHA"
