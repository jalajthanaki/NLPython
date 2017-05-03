## Spark installation guide for singled node cluster
```
Installation have 5 major steps.
Step 1: Installation of prerequisite
Step 2: Downloand and extract spark
Step 3: Config files changes
Step 4: Start services and stop services
Step 5: Run basic scala example


```
## Step 1: Installation of prerequisite

**Installation of Scala**
```
Step 1: Install scala
Download scala by clicking on this link: http://www.scala-lang.org/download/

Step 2: Extract scala to /usr/local
$ sudo tar vxzf ~/Downloads/scala-2.12.2.tgz -C /usr/local/

Step 3: Perform following command
$ cd /usr/local/
$ sudo mv scala-2.12.2/ scala/
$ sudo chown -R jalaj:jalaj scala/

Step 4: Set environment variables in bashrc file.
$ sudo vi ~/.bashrc

add the following lines at the end of the bashrc file.

export SCALA_HOME=/usr/local/scala
export PATH=$SCALA_HOME/bin:$PATH

Save and exit from .bashrc file.
Esc :wq

Step 5: Apply cahnges of bashrc file on system level
$ source ~/.bashrc

```
**Installation of maven**
```
Step 1: You install by using following comand
$ sudo apt-get install maven

Step 2: Verify maven installed successfully or not execute following command.
$ mvn -v 
    OR
$ mvn --version

```

## Step 2: Download and extract the spark 

```
Step 1: Download spark using given link 
http://spark.apache.org/downloads.html

Step 2: Extract spark in /usr/local
sudo tar vxzf ~/Downloads/spark-2.1.0-bin-hadoop2.7.tgz -C /usr/local/

Step 3: Execute following commands.
$ cd /usr/local/
$ sudo mv spark-2.1.0-bin-hadoop2.7/ spark/
$ sudo chown -R jalaj:jalaj spark/


Step 4: Set environment variables in bashrc file.
$ sudo vi ~/.bashrc

add the following lines at the end of the bashrc file.

export SPARK_HOME=/usr/local/spark
export PATH=$SPARK_HOME/bin:$PATH

Save and exit from .bashrc file.
Esc :wq

Step 5: Apply cahnges of bashrc file on system level
$ source ~/.bashrc

```

## Step 3: Config files changes
```
Step 1: Go to this location.
$ cd /usr/local/spark/conf
```
**spark-env.sh file config changes**
```
Step 2: Copy the spark-evn.sh.template file.
$ sudo cp spark-env.sh.template spark-env.sh

Step 3: Open file and check the machine name.
$ sudo vi /etc/hosts

you can see the system name and its ipaddress. 
you can also see the the localhost and its ipaddress.
Note your system name.

press Esc and then type :q

Step 4: make directory 
sudo mkdir -p /home/jalaj/sparkworker/sparkdata
$ sudo chown -R jalaj:jalaj /home/jalaj/sparkworker/sparkdata
$ Step 5: Open 'spark-env.sh' file and add following lines

Step 5: open spark-env.sh and adding the config variables.
$ sudo vi spark-env.sh

Add the following line at the end of spark-env.sh
export SCALA_HOME=/usr/local/scala
export SPARK_WORKER_MEMORY=1g
export SPARK_WORKER_INSTANCES=2
export SPARK_WORKER_DIR=/home/jalaj/sparkworker/sparkdata
export SPARK_MASTER_WEBUI_PORT=8081 #<<PORT NO as per your choice>>
export SPARK_MASTER_HOST=jalaj-System-Product-Name #<< type your system name>>

save and exit from spark-env.sh
Esc :wq
```
**slaves file config changes**
```
Step 6: Copy slaves.template as slaves.
$ sudo cp slaves.template slaves

Step 7: Open file and remove localhost and paste your computer name.
$ sudo vi slaves

delete localhost
insert following system name (in my case)
jalaj-System-Product-Name

save and exit from slaves.template
Esc :wq
```
**spark-defaults.conf.template file config changes**
```
Step 8: Open spark-defaults.conf.template file.
$ sudo vi spark-defaults.conf.template

add following line
spark://jalaj-System-Product-Name:7077
save and exit from spark-env.sh
Esc :wq

```
## Start spark services and stop spark service commands

```
Step 1: Go to the spark_home location
$ cd $SPARK_HOME

Step 2: Now we need to start master service
$ ./sbin/start-master.sh

Step 3: Now we need to start slaves service
$ ./sbin/start-slaves.sh

Step 4: To verify master and workers nodes are running or not execute the following command.
$ jps
    17473 Jps
    14611 Worker
    3192 Main
    14459 Master
    14701 Worker
    
Step 5: To stop services execute the following command.
$ ./sbin/stop-slaves.sh
$ ./sbin/stop-master.sh
```

## Run basic scala example
```
Step 1: Go to SPARK_HOME
$ cd $SPARK_HOME

Step 2: Execute following command to start spark shell. Yo can get Scala>> 
$ ./bin/spark-shell

Step 3: Now open the web URLs to see spark master and track your job activities. 
http://jalaj-system-product-name:4040/jobs/
http://jalaj-system-product-name:8081/

Step 4: Execute following command.
scala>> sc.parallelize( 2 to 200).count

Step 5: To exit from spark shell.
scala>> :quit


```
