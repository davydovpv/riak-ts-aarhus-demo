# rts12-sc-demo
##Description
This set of files makes up a demonstration of Riak TS 1.2, the Riak Python Client and associated Python libraries for data analysis and the Riak-Apache Spark connector.

##Demonstration limitation
Due to the GitHub limit on file uploads a demonstration data extract is included here.  The original demonstration uses a dataset of 13.7 million rows but that is too large to be uploaded here, even when compressed.  Therefore a demonstration data extract of 50,000 rows is included here. If anyone wants the full dataset, please contact me.

##Pre-requisites
The following need to be installed before running this demonstration:
* A JDK (with the environment variable of JAVA_HOME set and tha PATH edited to include the path to the java executables)
* Scala (I advise you not to use Scala 2.11 as this needs additional steps in its build that further complicate matters)
* Apache Spark - the original demonstration runs with Spark 1.6.1.  Installing Spark is not straightforward.  The document [] contains details of how I installed Spark on Linux Mint 17.2.  Those instructions will need to be changed for other Linux distributions
* Riak TS 1.2 - a download and instructions for installing this can be found at [].
* Python 2.7 this should be available as part of any Linux distribution, but if the version included is less than 2.7 you will need to upgrade.
* Pip - the python install tool; on linux mint and Debian/Ubuntu derivatives this can be installed with "sudo apt-get install python-pip".
* Python virtualenv - a library that allows the creation of isolated python development environments so that the core python which is used my many Linux system utilities is not adversely affected by installation of other python libraries and modules.  This can be installed as follows on linux "sudo pip install virtualenv".
* The Riak-Spark connector jar - this needs to be downloaded from [] and copied to a sub-directory that your user has access to.  I suggest a subdirectory within your user's home directory.
* Certain python modules require operating system libraries.  The ones needed are:
1. libpng and libpng-dev
2. libfreetype6 and libfreetype6-dev

##Instructions
In the following instructions I assume that the demonstration is being loaded and run on a Linux machine.  The '$' is the linux command prompt - DO NOT ENTER THE $ CHARACTER!
* Clone this repository to your machine.
* Create a python virtualenv - I will assume that you will use the cloned repository on your machine as the virtualenv, so to accomplish this task do:

<code>$cd rts12-sc-demo

$virtualenv</code>
* Once the virtualenv has been created enter <code>$source ./bin/activate</code>  This will change the command prompt.
* Then enter <code>$pip install -r requirements.txt</code> This will load the required python modules, including the current Riak python client


