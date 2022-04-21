# Task 1, session 3 by Aliaksandr Dvornik

## 1. Initialize repo

    git init task1_session3
    cd task1_session3

## 2. Create a text file in the folder and commit it
    
    touch README_.md
    git add .
    git commit -m "Initial commit"
    git log
    git status

## 3. Create a remote repository on GitHub

## 4. Push the local repository to GitHub

    git remote add origin git@github.com:ADv0rnik/task1_session3.git
    git push -u origin master

## 5. Create a new branch (develop) and switch to it

    git checkout -b develop

## 6. Create a new branch from 'develop' and switch to it

    git checkout -b develop_new develop
    git branch

## 7. Add the first line in the text file, commit, and push to remote

    echo text1 > README_.md
    cat README_.md
    git status
    git add . 
    git commit -m "Added new line into file"
    git log --oneline
    git push origin develop_new

## 8. Clone your repository from GitHub into a separate folder

    git clone git@github.com:ADv0rnik/Task_3_1.git new_folder
    cd new_folder    

## 9. Create another branch from 'develop' and switch to it using cloned project

    git checkout -b develop
    git branch
    git checkout -b develop_new_2 develop

## 10. Add the first line of the text file (different from the first branch), commit, and push on remote

    echo text2 > README_.md
    git  add .
    git commit -m "Added another new line into file"
    git push origin develop_new_2

## 11. Switch to develop
    
    git checkout develop
    
## 12.  Merge the first branch and push changes

    git merge origin/develop_new
    git push origin develop

## 13. Merge the second branch and push changes

    git merge develop_new_2
    git status

## 14. Resolve conflict
    
    git add README_.md
    git branch
    git commit -m "Updated file"
    git push origin develop

## 15. Commit and push a separate text file with a list of all the commands, which were used to solve the problem

    cd Homework    
    git checkout session_3
    git status
    git add Task1_3.md
    git commit -m "Added file with list of commands"
    git push





