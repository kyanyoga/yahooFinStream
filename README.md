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
#### sleep
time.sleep(5)
##### 
You can also edit the file to stream the stocks of your choice.
##### stocks
stocks = ["YHOO", "HPE", "AMZN", "AAPL", "GOOGL", "TWTR", "FB"]
##### output
host:bin kyanyoga$ cat /tmp/datastream/BSM_FIN_STRM2016-09-01T16\:45\:57 
2016-09-01T16:45:57,YHOO,42.93,42.78,43.10,42.72,5572160
2016-09-01T16:46:03,HPE,22.16,21.43,22.32,21.08,18887132
2016-09-01T16:46:08,AMZN,770.62,770.90,772.04,766.75,1790740
2016-09-01T16:46:13,AAPL,106.73,106.14,106.80,105.62,26596909
2016-09-01T16:46:19,GOOGL,790.75,791.98,792.89,786.33,827416
2016-09-01T16:46:25,TWTR,19.4999,19.3700,20.1400,19.2700,37492115
...
