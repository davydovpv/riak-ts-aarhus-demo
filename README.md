# riak-ts-aarhus-demo
##Description
This set of files makes up a demonstration of Riak TS, the Riak Python Client and associated Python libraries for data analysis and the Riak-Apache Spark connector.

##Demonstration limitation
Due to the GitHub limit on file uploads a demonstration data extract is included here.  The original demonstration uses a dataset of 13.7 million rows but that is too large to be uploaded here, even when compressed.  Therefore a demonstration data extract of 50,000 rows is included here. If anyone wants the full dataset, please contact me.

##Pre-requisites
The following need to be installed before running this demonstration:
* A JDK (with the environment variable of JAVA_HOME set and tha PATH edited to include the path to the java executables)
* Scala (I advise you not to use Scala 2.11 as this needs additional steps in its build that further complicate matters)
* Apache Spark - the original demonstration runs with Spark 1.6.1.  Installing Spark is not straightforward.  The document [spark.md](./spark.md) contains details of how I installed Spark on Linux Mint 17.2.  Those instructions will need to be changed for other Linux distributions
* Riak TS - a download can be found [here](http://docs.basho.com/riak/ts/latest/downloads/) and instructions for installation can be found [here](http://docs.basho.com/riak/ts/latest/installing/).  The demonstration assumes one node running locally.
* A build environment:  on Debian/ubuntu derivatives this is installed as <code>$sudo apt-get install build-essential</code>.  On RHEL derived systems this is a groupinstall of "development-tools".
* Python 2.7 this should be available as part of any Linux distribution, but if the version included is less than 2.7 you will need to upgrade.
* Pip - the python install tool; on linux mint and Debian/Ubuntu derivatives this can be installed with "sudo apt-get install python-pip".
* Python virtualenv - a library that allows the creation of isolated python development environments so that the core python which is used by many Linux system utilities is not adversely affected by installation of other python libraries and modules.  This can be installed as follows on linux "sudo pip install virtualenv".
* The Riak-Spark connector jar - this needs to be downloaded from [here] (https://github.com/basho/spark-riak-connector/releases/latest)
and copied to a sub-directory that your user has access to.  I suggest a subdirectory within your user's home directory.
* Certain python modules require operating system libraries.  You should refer to google/documentation for details on how to install these on your Linux distribution.  The ones needed (which are used by the graph drawing library matplotlib) are:
  1. libpng and libpng-dev
  2. libfreetype6 and libfreetype6-dev

##Installation instructions
In the following instructions I assume that the demonstration is being loaded and run on a Linux machine.  The '$' is the linux command prompt - DO NOT ENTER THE $ CHARACTER!
* Clone this repository to your machine.
* Create a python virtualenv - I will assume that you will use the cloned repository on your machine as the virtualenv, so to accomplish this task do:

```bash
$cd riak-ts-aarhus-demo
$virtualenv
```

* Once the virtualenv has been created enter `$source ./bin/activate`  This will change the command prompt showing the virtual environment is active.
* Then enter `$pip install -r requirements.txt` This will load the required python modules, including the current Riak python client.
* Unzip the demo-data-extract.zip file to get demo-data-extract.csv 

##Demonstration instructions
_This is not a demonstration of the Jupyter notebook analysis environment.  To run python code contained in a notebook cell you have to use the key combination SHIFT+ENTER.  If you want to explore Jupyter further, I refer you to the project [homepage](http://jupyter.org)_

Ensure Riak TS is running. Consider modifying the default configuration in `etc/riak.conf` when running a development installation of a single instance of Riak. 

```bash
$cd $path_to_riak

#assuming a developer environment of a single instance
#change ring_size from default (64) to 16
#this is a better reflection of how many virtual nodes would be allocated to a single machine in a Riak cluster
$echo "ring_size = 16" >> etc/riak.conf

#assuming a developer environment of a single instance
#change replica count from default (3) to 1
#otherwise Riak will write 3 replicas to the same instance
$echo "buckets.default.n_val = 1" >> etc/riak.conf

#start riak
$bin/riak start
```

With your python virtual environment active (see above), in the riak-ts-aarhus-demo subdirectory enter the following:

`SPARK_CLASSPATH=/path/to the /jar file/installed including the /jarfile jupyter notebook`

This will start a jupyter notebook server and open your browser to its home directory.  

In that directory you will find the following files (there will also be other files but you can ignore them as the server lists the subdirectory contents):
* _create-table-aarhus.ipynb_ - this is the initial notebook to create the table in RiakTS for the demonstration data, so run this first.  Once it has run, follow the instructions in the notebook for changing the default replication value (n_val).  Then in a separate terminal window (running the python virtual environment) run the python load script with the following command <code>$python load-data.py</code>  Once that has completed, switch to the Jupyter server homepage again in your browser and access
* _querying-arhus-data.ipynb_ - this notebook does an analysis of the aarhus sensor data for the sensor pair 668, then invoke the following from the server home page
* _aarhus-pyspark.ipynb_ - this notebook uses the Riak-Spark connector to do further analysis of the sensor pair 668 data.


