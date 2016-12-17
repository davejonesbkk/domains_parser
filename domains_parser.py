from urllib.parse import urlparse
import csv

#Create a list to store the completed blog post urls
completed = []

#open the completed blog post urls file
orders_file = open('orders_dec15.txt', 'r')
completed = [line for line in orders_file.readlines()]

#store the completed urls in the list
completed = list(map(str.strip, completed))


#create a dictionary for building the domains and prices
mydict = {}

#get the website domains and respective prive for each 
with open('domains_prices.txt') as f:
	for line in f:
		#separate and then store in the dictionary
		tok = line.split()
		mydict[tok[0]] = tok[1]


#create a new file that will hold the completed blog posts urls and respective price
fp = open('completed_orders_dec15.csv', 'w')

#iterate over the completed post urls and get just the domain for each
for i in completed:
	x = urlparse(i)
	y = (x.netloc)

	#match the domain from the post urls to the domain and its price
	for k,v in mydict.items():
		k = urlparse(k)
		k = (k.netloc)

		if k == y:

			#save the completed post urls with its price to the new file
			writer = csv.writer(fp, delimiter=',')
			writer.writerow([i,v])








