
# Linux (Ubuntu 14.04) installation links
```

Follow the link where you can find various option to install it.

https://simplifydatascience.wordpress.com/2016/10/11/ubuntu-for-beginners-part-1/
```

# Basic Commands for directory
```

1. cd to change directory
   cd /home/jalaj/folder1
   
   To make directory
   sudo mkdir folderpath
   sudo mkdir /home/jalaj/foldername2. ~ stands for /home/USERNAME
   example:
   cd ~ = cd /home/jalaj

2. To see at which location
   pwd
   example:
   $ pwd
   /home/jalaj/folder14. Jump to parent directory
   cd ..

3. Jump to root directory
   cd
4. Jump to home directory
   cd ~ or cd /home/jalaj

5. To visit last path
   cd -
   example:
   cd /home/jalaj/folder1
   cd ..
   cd /home/jalaj/folder2
   now you want to visit folder1 again
   cd -

6. . stands for current directory
   cd /home/jalaj/folder1
   cd ./subfolder1 means you can jump inside subfolder1 which is reside inside folde1
   structure is as below
   folder1
   |
   |
    -----subfolder1

```


# Basic command for files
```


1. Open file
   sudo vi /home/jalaj/test.txt

2. Edit or write inside the file
   press Insert key and start writing OR
   press i and start writing
   i or Insert indication writing mode for file
3. If you press Esc key you can't edit file.
4. once you have finshed writing you need to do following steps to save file with its content
   press Esc key
   type :wq This is for saving file with its content
5. If you open file and changed content but you now you don't want to save it
   press Esc
   type :q!
```

# List all items inside the directory


```



1. To list all items including folders and files 
   $ ls

2. To list all items with permissions, ownership, size, Modified data & time.
   $ ls -l
   
3. To see latest modified files and folders 
   $ ls -lt
 
4. To see latest modified files and folders inn reverse order
   $ ls -ltr
   
5. To see all hidden files and folders as well as not hidden files and folder
   $ ls -la
   
6. To see all hidden files with indication of which are files and which are directory
   $ ll

```
    
   
# Copy Paste commands

```

1. Copy paste a file 
   $ cp sourcefilepath destinationfilepath
   example:
   $ cp ./folder/file.txt /home/jalaj/file.txt 
   
   If you will get permission error then execute following command.
   $ sudo cp ./folder/file.txt /home/jalaj/file.txt 2. Copy paste a folder
   $ cp -R sourcefolderpath destinationfolderpath
   example:
   $ cp -R ./folder ./folder1
   
   If you will get permission error then execute following command.
   $ sudo cp -R ./folder ./folder1


```


# Cut Paste commands

```


1. Cut paste a file
   $ mv sourcefilepath destinationfilepath
   example:
   $ mv ./folder/file.txt /home/jalaj/file.txt 
   
   If you will get permission error then execute following command.
   $ sudo mv ./folder/file.txt /home/jalaj/file.txt 
2. Cut paste a folder
   $ mv -R sourcefolderpath destinationfolderpath
   example:
   $ mv ./folder /home/jalaj/
   
   If you will get permission error then execute following command.
   $ sudo mv -R ./folder /home/jalaj/
```

# Rename files or folders


```

1. Rename a file.
   $ mv currentfilename newfilename
   example:
   $ mv ./filename1.txt ./filename2.txt
   2. Rename folder.
   $ mv currentfolder newfolder
   example:
   $ mv ./foldername ./newfoldername


```
# Delete files or folder

```



1. Delete file 
   $ rm -rf filename

2. Delete folder 
   $ rm -rf ./folder
```


# Change ownership of files and folder

```

1. Change ownership of file
   $ chown usename:username filename
   example:
   $ chown jalaj:jalaj ./test.txt
   
   if you will get permission error then try to execute the following command.
   $ sudo chown jalaj:jalaj ./test.txt2. Change ownership of the folder as well as files which reside inside that folder
   $ chown -R username:username folderpath
   example:
   $ chown -R jalaj:jalaj /home/jalaj/foldername1
   
      
   if you will get permission error then try to execute the following command.
   $ sudo chown -R jalaj:jalaj /home/jalaj/foldername1

```

# Change permission for file(s) & folder


```
There are three types of permission
1. Read 2. Write 3. Execute

See the article to know more on this http://linuxcommand.org/lts0070.php1. Change permission of file
   $ sudo chmod permissionflag ./filenamewithfullpath
   example:
   $ sudo chmod 777 ./test.txt


2. Change permission of folder
   $ sudo chmod -R 777 ./foldername1

```


# Tar and Untar (zip & unzip) commands

```


1. compress file or directory
   $tar -czvf name-of-archive.tar.gz /path/to/directory-or-file
   example:
   $tar -czvf test.tar.gz /home/jalaj/test.txt

   -c: Create an archive.
   -z: Compress the archive with gzip.
   -v: Display progress in the terminal while creating the archive, also known as “verbose” mode. The v is always          optional in these commands, but it’s helpful.
   -f: Allows you to specify the filename of the archive.2. unzip file or directory
   $ tar -xzvf archive.tar.gz    
   example:
   $ tar -xzvf test.tar.gz /home/jalaj/folder1

2. unzip file or directory to specific folder
   $ tar -xzvf archive.tar.gz -C /tmp
   example:
   $ tar -xzvf test.tar.gz /usr/lib/test 

```

```


# Basic installation for software on ubuntu
1. Command to install softwares or you can us software center 
   $ sudo apt-get softwarename
   example:
   $ sudo apt-get git
   $ sudo apt-get gedit

To get the update on ubuntu 
$ sudo apt-get update

```


# How to define golbal environment variable inside bashrc files for software
```


1. If you want to define path of software as global environment variable then follow the steps
   1.1. Open bashrc file which is a hidden file.
   1.2. Path of bashrc file is /home/jalaj/.bashrc or ~/.bashrc
   1.3 Open file and you can set enviroment variable.
    
   example: If I want to set global environment variable for folderpath /home/jalaj/bin 
            I should add folloing lines to the bashrc file.
            - Open file
              $ sudo vi ~/.bashrc
                
            - Add line at the end of the file (press Insert key to add following lines)
              $ export PATH=$PATH:~/bin
              then press Esc 
              then type :wq to save it
              
            - Then execute following command to apply changes in bashrc file
              $ source ~/.bashrc 
                

```
