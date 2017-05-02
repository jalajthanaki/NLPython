## Hadoop Installation Steps for single node standalone cluster
```
There are 3 major steps which are given below.
1. Install java and ssh server and clint as prerequisites
2. Download and extract hadoop
3. Config hadoop for standalone Hadoop installation

```
## 1. Java installation on Ubuntu
```
Step 1: Download jdk. Click on this link and accept the license.
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

Suppose you have downloaded jdk-8u121-linux-x64.tar.gz

Step 2: Make a directory by using following command.
$ sudo mkdir /usr/java

Step 3: $ cd

Step 4: Extract the java tar file.
$ sudo tar vxzf ~/Downloads/jdk-8u121-linux-x64.tar.g -C /usr/java

Step 5: run bunch of following commands
$ sudo update-alternatives --install "/usr/bin/java" "java“ "/usr/lib/jvm/jdk1.8.0_<java version>/jre/bin/java" 1
$ sudo update-alternatives --install "/usr/bin/javac" "javac“ "/usr/lib/jvm/jdk1.8.0_<java version>/bin/javac" 1
$ sudo update-alternatives --install "/usr/bin/javaws" "javaws“ "/usr/lib/jvm/jdk1.8.0_<java version>/bin/javaws" 1
$ sudo update-alternatives --install "/usr/bin/jps" "jps“ "/usr/lib/jvm/jdk1.8.0_<java version>/bin/jps" 1
$ sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_<java version>/jre/bin/java
$ sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_<java version>/bin/javac
$ sudo update-alternatives --set javaws /usr/lib/jvm/jdk1.8.0_<java version>/bin/javaws

Step 6: Set an environment variable
Open bashrc file by using following command:
    $ sudo vi ~/.bashrc
At the end of the file paste the following content
    JAVA_HOME=/usr/java/jdk1.8.0_121
    export JAVA_HOME
    PATH=$PATH:$JAVA_HOME/bin
    export PATH
    
Step 7: Save and exit file by typing following comand
press ECS then :wq

Step 8: Apply cahnges of bashrc file on system level
$ source ~/.bashrc

Step 9: You need to type following command to confirm that java has been installed successfully.
$ java -version
```
## Install open ssh and generate rsa key
```
Step 1: To install openssh client use the following command.
$ sudo apt install openssh-client

Step 2: To install openssh server use the following command.
$ sudo apt install openssh-server

Step 3: generate rsa key
$ ssh-keygen -t rsa -P '' 
press enter
$ cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
$ ssh localhost 

if it connects to localhost then you are done with prerequisites.

```
## Download and extract the hadoop
```
Step 1: Download Hadoop
you can use any of the give link
https://archive.apache.org/dist/hadoop/common/
https://archive.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz

Step 2: Extract the hadoop in /usr/local
$ sudo tar vxzf ~/Downloads/hadoop-2.7.3.tar.gz -C /usr/local
$ cd /usr/local
$ sudo mv ./hadoop-2.7.3 ./hadoop
$ sudo chown -R jalaj:jalaj hadoop/ (use your PC username instand of using jalaj)

Downloading and extracting has been done.

```

## Config hadoop for single node cluster
```
Step 1: Go to following path.
$ cd /usr/local/hadoop/etc/hadoop

Step 2: Open hadoop-env.sh and add export path of JAVA_HOME
$ sudo vi hadoop-env.sh

find these lines and we need to change them.
# The java implementation to use.
export JAVA_HOME=${JAVA_HOME}

Change above line to the following
# The java implementation to use.
#export JAVA_HOME=${JAVA_HOME}
export JAVA_HOME=/usr/java/jdk1.8.0_121

Step 3: save and exit file Esc :wq

Step 4: make tmp directory for hadoop
$ sudo mkdir -p /app/hadoop/tmp
$ sudo chown jalaj:jalaj /app/hadoop/tmp/

Step 5: Open core-site.xml
$ sudo vi core-site.xml

Step 6: Insert following properties inside the configuration xml tags.
<property>
  <name>hadoop.tmp.dir</name>
  <value>/app/hadoop/tmp</value>
  <description>A base for other temporary directories.</description>
</property>

<property>
  <name>fs.default.name</name>
  <value>hdfs://localhost:54310</value>
  <description>The name of the default file system.  A URI whose
  scheme and authority determine the FileSystem implementation.  The
  uri's scheme determines the config property (fs.SCHEME.impl) naming
  the FileSystem implementation class.  The uri's authority is used to
  determine the host, port, etc. for a filesystem.</description>
</property>

Step 7: save and exit the file.
Esc :wq

Step 8: create following directories for namenode and datanode.
$ sudo mkdir -p /home/jalaj/mydata/hdfs/namenode
$ sudo mkdir -p /home/jalaj/mydata/hdfs/datanode
$ sudo chown -R jalaj:jalaj /home/jalaj/mydata

Step 9: Open hdfs-site.xml
$ sudo vi hdfs-site.xml

Step 10: add the following properties inside the configuration xml tag
<property>
    <name>dfs.replication</name>
    <value>1</value>
    <description>Default block replication.
  The actual number of replications can be specified when the file is created.
  The default is used if replication is not specified in create time.
   </description>
</property>
<property>
    <name>dfs.namenode.name.dir</name>
    <value>file:/home/jalaj/mydata/hdfs/namenode</value>
</property>
<property>
    <name>dfs.datanode.data.dir</name>
    <value>file:/home/jalaj/mydata/hdfs/datanode</value>
</property>

Step 11: Save and exit from file
$ Esc :wq

Step 12: Now we have to add environment variables inside bashrc file so open bashrc file.
$ sudo vi ~/.bashrc
At the end of the file add following commands
 export HADOOP_HOME=/usr/local/hadoop
 export PATH=$PATH:$HADOOP_HOME/bin
 export PATH=$PATH:$HADOOP_HOME/sbin
 export HADOOP_MAPRED_HOME=$HADOOP_HOME
 export HADOOP_COMMON_HOME=$HADOOP_HOME
 export HADOOP_HDFS_HOME=$HADOOP_HOME
 export YARN_HOME=$HADOOP_HOME
 export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
 export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"

Step 13: save and exit from the bashrc file.
$ Esc :wq

Step 14: Run the following command to apply cahnges of bashrc file on system level
source ~/.bashrc

Step 15: Now it is time to check hadoop has been installed or not
$ hadoop version
if you can see the version of hadoop then you have installed it sucessfully.

Step 16: We first need to format namenode.
$ hadoop namenode -format

Step 17: Now we need to start hadoop services.
$ start-dfs.sh
after this command namenode,datanode and secondary namenode are going to start. To verify it you can use following command.
$ jps
you got this kind of output.
10432 Main
13796 DataNode
13643 NameNode
14171 Jps
14047 SecondaryNameNode
numbers indicated processid so it will be vary from ervey one.

Step 18: Now we need to start our yarn
$ start-yarn.sh
it will start resource manager and node manager
you can verify by using jps command.
$ jps
10432 Main
14418 NodeManager
13796 DataNode
14265 ResourceManager
13643 NameNode
14748 Jps
14047 SecondaryNameNode

Step 19: If you want to stop services then use following commands.
$ stop-yarn.sh
$ stop-dfs.sh

you can monitor hadoop cluster via using following URL.
http://localhost:50070/

This is the end of the installation process.

```