#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Step 1: Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Step 2: Apply Django migrations
echo "Applying Django migrations..."
python api/manage.py migrate

# Step 3: Collect static files
echo "Collecting static files..."
python api/manage.py collectstatic --noinput

# Step 4: Install Node.js dependencies (if needed)
# This is useful if you have a frontend or additional build steps
echo "Installing Node.js dependencies..."
npm install

# Step 5: Build the project (if applicable)
echo "Building the project..."
npm run build

# Step 6: Clean up unnecessary files (optional)
# echo "Cleaning up..."
# rm -rf ./build

echo "Build process completed successfully."
