#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run ruff check
echo "Running Ruff linter..."
ruff check .

# Run ruff format check
echo ""
echo "Checking code formatting..."
ruff format --check .

echo ""
echo "To auto-fix issues, run: ruff check --fix . && ruff format ."

