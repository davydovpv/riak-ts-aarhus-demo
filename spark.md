#Installing Apache Spark (on Linux)

1. Make sure you have a JDK installed and working correctly.


2. Install scala 2.10.6 following the instructions on http://www.scala-lang.org/download/.  Go to the bottom of the page, do not take the 2.11 version offered at the top.  2.11 requires additional steps in the Spark build which make it complicated.  


3. Set $SCALA_HOME and $PATH per this page:  http://www.scala-lang.org/download/install.html.  This could be in one of several files per your set-up.  My environment is set-up to use BASH, so I set the variables in ‘~/.bashrc’.  Test by running the spark shell (‘$scala’).


4. Download spark 1.6.1 source,  [can build several Hadoop versions], direct download from:  http://spark.apache.org/downloads.html


5. Extract the tgz file into a convenient location.


6. Run ‘make-distribution.sh’ in the root Spark directory (‘$shell make-distribution.sh’ or ‘$bash make-distribution.sh’ depending on your set-up.


7. Set JAVA_HOME in the same place as the other variables in step 3.  JAVA_HOME should point to the directory that contains the “bin” subdirectory.


8. From the spark root directory ($spark-1.x.x) run ‘build/mvn -DskipTests clean package’.


9. If there are no error messages run ./bin/spark-shell.  That should open the spark shell.


10. If the above works correctly, run ./bin/pyspark.  That should open PySpark.


You are now set-up with Spark.



