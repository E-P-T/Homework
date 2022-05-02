# Python Practice - Session 3

1. Create a local folder and initialize it for git;
2. Create a text file in the folder and commit it;
3. Create a remote repository on GitHub;
4. Push the local repository to GitHub;
5. Create a new branch (develop) and switch to it;
6. Create a new branch from 'develop' and switch to it;
7. Add the first line in the text file, commit, and push to remote;
8. Clone your repository from GitHub into a separate folder;
9. Create another branch from 'develop' and switch to it using cloned project;
10. Add the first line of the text file (different from the first branch), 
    commit, and push on remote;
11. Switch to develop;
12  Merge the first branch and push changes;
13. Merge the second branch and push changes;
14. Resolve conflict;
16. Commit and push a separate text file with a list of all the commands, which were used to solve the problem;

===================================
1.
$ cd d:/
$ mkdir EPAM-test
$ cd EPAM-test
$ git init

2.
$ touch test.txt
$ git add test.txt
$ git commit -m 'add new file'

4.
$ git push
5.
$ git branch develop
$ git checkout develop

6.
$ git branch overdevelop
$ git checkout overdevelop
$ git push --set-upstream origin develop
$ git checkout -b overdevelop
$ git push --set-upstream origin overdevelop

7.
$ nano test.txt ==> adding a string
$ git commit -m 'writing first line'
$ git push

8.
$ git checkout main
$ cd ..
$ mkdir EPAM-test2
$ git clone git@github.com:Dmytro-TNT/EPAM-test.git d:/EPAM-test2
$ cd EPAM-test2

9.
$ git checkout develop
$ git checkout -b underdevelop

10.
$ nano test.txt
$ git add test.txt
$ git commit -m 'writing first line in clone underdevelop branch'
$ git push --set-upstream origin underdevelop

11.
$ git checkout develop

12.
$ git merge overdevelop
$ git push

13.
$ git merge underdevelop

14. На GitHub решаю конфликт перенося одну из конфликтущих строк на на другую строку (2 строки претендуют на одно и то же место в файле), и завершаю слияние.

