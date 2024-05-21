# Run tests
echo "Running tests..."
pytest

# Check if tests passed
if [ $? -eq 0 ]; then
  echo "Tests passed. Committing changes..."
  # Commit changes
  git add .
  git commit -m "Tests passed"
  echo "Changes committed."
else
  echo "Tests failed. Reverting changes..."
  # Revert changes
  git reset --hard HEAD
  echo "Changes reverted."
fi