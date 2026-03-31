#!/bin/bash

set -e

echo "🛠  Starting AI Operator Local Deployment..."

# Check for .env file
if [ ! -f .env ]; then
  echo "❌ .env file not found. Please create one with your credentials."
  exit 1
fi

# Export environment variables
export $(grep -v '^#' .env | xargs)

echo "✅ Loaded environment variables."

# Start containers
echo "🐳 Launching services with Docker Compose..."
docker-compose up --build -d

