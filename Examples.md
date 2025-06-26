## Git Basics GuideAdd commentMore actions

Quick reference for team members who are new to Git or need a refresher.

## Initial Setup (One Time Only)

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Clone the project repository
git clone <repository-url>
cd <project-folder>
```

## Daily Workflow

### 1. Start Your Work Session
```bash
# Always pull latest changes first
git pull origin main
```

### 2. Check Status
```bash
# See what files have changed
git status

# See specific changes in files
git diff
```

### 3. Save Your Changes
```bash
# Add specific files
git add filename.py
git add folder/

# Or add everything (be careful!)
git add .

# Commit with a meaningful message
git commit -m "Add password strength validation function"
```

### 4. Share Your Changes
```bash
# Push to the shared repository
git push origin main
```

## Working with Branches (Recommended)

### Create a Feature Branch
```bash
# Create and switch to new branch
git checkout -b feature/vulnerability-scanner

# Work on your feature, then commit
git add .
git commit -m "Implement SQL injection pattern detection"

# Push your branch
git push origin feature/vulnerability-scanner
```

### Merge Your Work
```bash
# Switch back to main
git checkout main

# Pull latest changes
git pull origin main

# Merge your feature
git merge feature/vulnerability-scanner

# Push the updated main
git push origin main

# Delete the feature branch (cleanup)
git branch -d feature/vulnerability-scanner
```

## Common Scenarios

### Someone Else Made Changes
```bash
# If push fails due to remote changes
git pull origin main
# Resolve any conflicts, then
git push origin main
```

### Undo Last Commit (Not Pushed Yet)
```bash
git reset --soft HEAD~1
```

### Discard Local Changes
```bash
# Discard changes to specific file
git checkout -- filename.py

# Discard all local changes (careful!)
git reset --hard HEAD
```

### See History
```bash
# View commit history
git log --oneline

# See what changed in last commit
git show
```

## File Management

### Ignore Files
Create a `.gitignore` file in project root:
```
# IDE files
.vscode/
*.swp

# Language specific
__pycache__/
*.pyc
node_modules/
bin/
obj/

# OS files
.DS_Store
Thumbs.db

# Environment files
.env
config.local.json
```

## Emergency Commands

### Oops, I Committed the Wrong Thing
```bash
# If you haven't pushed yet
git reset --soft HEAD~1
# Fix your files, then commit again

# If you already pushed (careful - affects others)
git revert HEAD
```

### Help, Everything is Broken
```bash
# See current state
git status

# Get back to last known good state
git reset --hard origin/main
```

## Best Practices

1. **Commit often** - Small, focused commits are better than large ones
2. **Write good commit messages** - "Fix bug" is bad, "Fix SQL injection in login form" is good  
3. **Pull before you push** - Always get latest changes first
4. **Don't commit sensitive data** - Use .gitignore for API keys, passwords, etc.
5. **Test before committing** - Make sure your code works
6. **Use branches for features** - Keep main branch stable

## Quick Reference

| Command | What it does |
|---------|--------------|
| `git status` | Show current state |
| `git add <file>` | Stage file for commit |
| `git commit -m "message"` | Save changes locally |
| `git push` | Upload changes to server |
| `git pull` | Download latest changes |
| `git log` | Show commit history |
| `git diff` | Show changes since last commit |

## Getting Help

```bash
# Get help for any command
git help <command>
git help commit

# Quick help
git <command> --help
```Add commentMore actions

Remember: When in doubt, ask for help! Git can be tricky, but these basics will cover 90% of what you need.