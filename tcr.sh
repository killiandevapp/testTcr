# Run tests
pytest

# Check if tests passed
if [ $? -eq 0 ]; then
  # Commit changes
  git add .
  git commit -m "Tests passed"
else
  # Revert changes
  git reset --hard HEAD
fi