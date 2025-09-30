# Just practicing git and github with SSH

# Initialize local repo
git init

# Create a file
touch index.html

# Edit file in VSCode
code index.html   # (use 'code' not 'vscode')

# Add all files
git add .

# Commit them
git commit -m "Initial commit"

# Connect to GitHub via SSH (replace with your repo SSH link)
git remote add origin git@github.com:your-username/project.git

# Push files (use main if your branch is main)
git push -u origin master
