
import csv, math
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
import pandas as pd
import numpy as np

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

myfile = drive.CreateFile({'id': '1wFDMRyo-NUj5dNDnq1MAMD9CBZ-P8cdxJCha2J3vR5w'})

myfile.GetContentFile('spm_orders.csv', mimetype='text/csv')

#Create a list to store the completed blog post urls
completed = []

#open the completed blog post urls file


df = pd.read_csv('spm_orders.csv')
url_col = df['Live URL']
for line in url_col:
	completed.append(line)


completed_list = [ x for x in completed if str(x) != 'nan']
print(completed_list)

#store the completed urls in the list
completed_list = list(map(str.strip, completed_list))




#create a dictionary for building the domains and prices
domainsprices_dict = {}

#get the website domains and respective prive for each 
with open('domains_prices.txt') as f:
	for line in f:
		#separate and then store in the dictionary
		tok = line.split()
		domainsprices_dict[tok[0]] = tok[1]


#create a new file that will hold the completed blog posts urls and respective price
total_prices = 0
with open('completed_orders_.csv', 'w') as fp:

	#iterate over the completed post urls and get just the domain for each
	for i in completed_list:
		x = urlparse(i)
		y = (x.netloc)

		#match the domain from the post urls to the domain and its price
		for k,v in domainsprices_dict.items():
			k = urlparse(k)
			k = (k.netloc)

			if k == y:

					#save the completed post urls with its price to the new file
				writer = csv.writer(fp, delimiter=',')
				writer.writerow([i,v])
				
				
wf = pd.read_csv('completed_orders_.csv')







