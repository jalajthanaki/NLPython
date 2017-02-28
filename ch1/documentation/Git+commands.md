
# Git tutorial

# Following are the steps that you need to follow
Git is version control system.

```


1. Go to github and signup
   https://github.com2. Open your system termianl and execute following commands.
   2.1 $ git clone https://github.com/jalajthanaki/NLPython.git
   
   2.2 $ git config --global user.email "example@domain.com" put your emailID which you have given on github
   
   2.3 $ git config --global user.name "username"
   
   2.4 make changes
   
   2.5 $ git status 
   
        (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    linuxcommands

        Untracked files:
        (use "git add <file>..." to include in what will be committed)

        .gitignore
        linuxcommands.md
   2.6  Add all untracked file on git 
        $ git add -A 
   
   2.7  Commit/save your changes
        $ git commit -m "message"
   
   2.8  Push your changes on git branch
        $ git push
        
   2.9  If you want to update and sync your repository with master branch
        $ git pull
```

       
# If you want to create a branch and work on it then want to merge and puch with master then following is the process


```



1. Create branch locally
   $ git checkout -b [name_of_your_new_branch]
   example : git checkout -b test
```

```

        
2. You can work locally in your branch, when you are ready to share the branch, push it. 
   The next command push the branch to the remote repository origin and tracks it
   $ git push <remote-name = origin> <branch-name> 
   example: $git push origin test
```

```

        
3. Show branches
   $ git branch
     This will show all branches
```
```


       
4. Add a new remote for your branch :
   $ git remote add [name_of_your_remote] 
   example: $ git remote add tester 
```
```



5. Push changes from your commit into your branch : 
   $ git push [name_of_your_new_remote] [name_of_your_branch]
   example: $ git push test tester
```
```



6. Update your branch when the original branch from official repository has been updated :
   $ git fetch [name_of_your_remote]
   example: $ git fetch tester
```
```


        
7. Then you need to apply to merge changes, if your branch is derivated from tester you need to do
   $ git merge [name_of_your_remote]/tester
   example: $ git mearge tester
```
