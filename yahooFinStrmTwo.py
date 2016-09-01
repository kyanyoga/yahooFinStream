#!/usr/bin/env python
from yahoo_finance import Share
import time
import os

# stocks
stocks = ["YHOO", "HPE", "AMZN", "AAPL", "GOOGL", "TWTR", "FB"]
print stocks.__len__()

# main loop - infinite loop
while(True):
    # timestamp
    t = time.strftime('%Y-%m-%dT%H:%M:%S')
    
    # write to csv file
    import csv
        
    # filename
    outfile = '/tmp/datastream/' + 'BSM_FIN_STRM' + t
    # outfile = 'BSMLABS_fin_csvstream.csv'
    
    # loop counter
    x = 1
        
    with open( outfile, 'wa' ) as csvfile:
        fieldnames = ['ts','symbol', 'price', 'open', 'days_high', 'days_low', 'volume']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # write file header
        # writer.writeheader() -- don't need header for big data
        
        # main loop - cycle X times based on length of stock array
        while (x <= (stocks.__len__() * 5)):
            # stock loop
            for stock in stocks:
                
                # print header 
                print ("Stock: %12s  TimeStamp: %20s" % (stock, t))
                
                # sample: yahoo = Share('YHOO')
                # print t, yahoo.get_open(), yahoo.get_price(), yahoo.get_days_high(), yahoo.get_days_low()
                
                # update timestamp
                t = time.strftime('%Y-%m-%dT%H:%M:%S')
                
                # get yahoo finacne information
                shareinfo = Share(stock)
                
                # print share information
                print ("lc: %d price: %s open: %s dayhigh: %s daylow: %s volume: %s" 
                       % (x,
                          shareinfo.get_price(), 
                          shareinfo.get_open(), 
                          shareinfo.get_days_high(), 
                          shareinfo.get_days_low(), 
                          shareinfo.get_volume() 
                        ))
                
                # line space
                print
                        
                # write data to csv file
                writer.writerow({'ts':t,
                                 'symbol':stock,
                                 'price':shareinfo.get_price(),
                                 'open':shareinfo.get_open(),
                                 'days_high':shareinfo.get_days_high(),
                                 'days_low':shareinfo.get_days_low(),
                                 'volume':shareinfo.get_volume()})
               
                # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
                
                # sleep
                time.sleep(5)
                
                # increment counter
                x += 1
                    
    # close streamed file
    csvfile.close()
    
    #sleep 5 seconds - not much faster at .250
    #time.sleep(15)
    
    
    # find . -type f -name 'BSM*' -exec cat {} + >> stream.csv
