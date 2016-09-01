# yahooFinStream
Data Streaming App used to generate Real data from Yahoo Financial Stream.
A Great use case is to check the plumbing on your Spark Streaming or Kafka Job.

# make sure you have mongodb installed first. 
The script is configured for localhost. 

## Install - download git

##### create a development directory, cd into your new directory and make sure you have Yahoo Finance Installed.
##### $ pip install yahoo-finance
##### -or-
##### git clone git://github.com/lukaszbanasiak/yahoo-finance.git
##### $ cd yahoo-finance
##### $ python setup.py install
#####
##### create a /tmp/datastream directory
##### $ mkdir /tmp/datastream
##### run the data generator of your choice : yahooFinStrmTwo.py [generate a CSV files in /tmp/datastream]
##### -or- generate data into a mongodb database: yahooFinStrmThree.py
##### $ python yahooFinStrmThree.py
You can edit the file and adjust the sleep interval to make the job stream a little faster.
# sleep
time.sleep(5)
##### 
