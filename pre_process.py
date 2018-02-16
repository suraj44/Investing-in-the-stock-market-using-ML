import pandas as pd
import os
import time
from datetime import datetime
 

path = "/media/suraj/LET US/ML/intraQuarter"

def key_Stats(gather="Total Debt/Equity (mrq)"):
	df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio'])
 	statspath = path + '/_KeyStats'
 	stock_list = [x[0] for x in os.walk(statspath)]
 	print '0000'
 	for each_dir in stock_list[1:]:
 		print 1
 		each_file = os.listdir(each_dir)
 		ticker = each_dir.split("/")[7]
 		df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio'])
 		if len(each_file)>0:
 			for file in each_file:

 				date_stamp = datetime.strptime(file,'%Y%m%d%H%M%S.html')
 				unix_time = time.mktime(date_stamp.timetuple())
 				#print date_stamp, unix_time 
 				full_file_path = each_dir + '/' + file  
 				#print full_file_path
 				source = open(full_file_path, 'r').read()
 				#print source
 				#time.sleep(15)
 				try:
 					value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split("</td>")[0])
 					#value = float(value.split("</td>")[0])
 					df = df.append({'Date':1,'Unix':2,'Ticker':3,'DE Ratio':4,},ignore_index = True)
 					#print 1;
 				except Exception as e:
 					pass
 	save = gather.replace(' ','').replace(')', '').replace('(','').replace('/','') + '1.csv'
 	print save
	df.to_csv(save)
	source.close()




key_Stats()

