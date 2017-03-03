
# How to install pycharm community edition on linux

Download pycharm latest version using this url: https://www.jetbrains.com/pycharm/download/#section=linux

The downloaded file is tar.gz file now follow the below step to install it.Execute all the following command on terminal

Untar the file in /opt path
```
    $ tar xvzf ~/Downloads/pycharm-community*.tar.gz -C /opt
```    
    
    
Change ownership if only need
```
    $ sudo chown -R jalaj:jalaj  /opt/pycharm-community-2016.3.2
```


Jump to the following path
```
    $ cd /opt/pycharm-community-2016.3.2/bin
``` 
 
 
Now you can see the pycharm.sh
```
    $ sh ./pycharm.sh or sudo sh./pycharm.sh
```


If you want to make desktop entry for pycahrm so the pycharm can be lunched from luncher then follow the steps  
given below
```
        Start PyCharm.
        
        From the Tools menu, select "Create Desktop Entry..."
        
        Tick the corresponding box if you want the launcher for all users.
        
        If you selected "Create entry for all users", you will be asked for your password.
        
        A green message bubble should appear informing you that it was successful.
        
        You should then be able to find PyCharm in the Unity Dash or pin it to the launcher.
        
```

