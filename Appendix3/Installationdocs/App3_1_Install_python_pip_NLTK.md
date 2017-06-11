
# Setup Python, pip & NLTK 

# Installation and setup NLTK enviroment on Linux Ubuntu 14.04 (recommended way)




```
python
import sys
sys.version
sys.version_info 2_Python

```




    sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)


```

Installation of pyhton on Ubuntu 14.04

Ubuntu system has pyhton 2.7.X inbuilt no need to download and install it 

To confirm whether python has been properly install or not do following steps.

Step 1: Open system terminal
Step 2: 
         $ python -V
         Python 2.7.6

```


```

Install pip and setup tools On Linux ubuntu 14.04


What is pip?
pip is a package management system used to install and manage software packages written in Python

Open your system's terminal and execute following commands

$ sudo apt-get install -y python-pip
$ sudo pip install --upgrade pip


Confirm pip has been installed successfully.

$ pip -V
pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)Next step is to install nltk package and download nltk data
```


```


Installation steps for NLTK 

on terminal execute following command
$ sudo pip install nltk
$ pythonAfter this now you are inside the python shell and check your nltk package install properly or not

$ python
Python 2.7.6 (default, Oct 26 2016, 20:30:19) 
[GCC 4.8.4] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>import nltk
>>>nltk.download()

Choose the path where you wnat to download nltk data and click "Download" option.

Download process may take long time.
you can refer the diagram 1.4 given in chapter no 1

OR 

If you don't want to go inside python shell you can open your system's terminal and execute the following command
Command : sudo python -m nltk.downloader -d PATH_OF_NLTK_DATA all
Actual command : sudo python -m nltk.downloader -d /usr/local/share/nltk_data all



```
