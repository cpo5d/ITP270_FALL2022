# Step 1: To initialize Git repository
# $git init

# -OR-

# Step 1: To bring someone else's repo down to your local environment
# $git clone <remote address> <workspace name>

# Step 2: To check the status of files in the workspace and if they are committed
# $git status

# Step 3: To add a file to the staging area that you have changed to track them
# $git add <filename> ex: git add scene-1.txt

# Step 4: To check the difference between the working directory and the staging area
# $git diff <filename> ex: git diff scene-1.txt

# Step 5: To update a file in the staging area with untracked changes
# $git add <filename> ex: git add scene-1.txt

# Step 6: To commit changes from staging to the repo on the git server
# $git commit -m "<Commit message>" 

# Step 7: Show a log of all previous commits in the workspace
# $git log

#Other commands

# To list the origin of remotes of a local workspace
# git remote -v

# Grab files from a remote repo when there have been changes and place then in the remote branch
# git fetch

# Merge changes from the remote branch into the local master repository
# git merge origin/master

# Create a branch for work locally
# git branch <branch name> ex: git branch bio-questions

# Switch to a new branch
# git checkout <branch name> ex: git checkout bio-questions

# Push changes from a local branch to a remote repo
# git push origin <local branch name> ex: git push origin bio-questions
