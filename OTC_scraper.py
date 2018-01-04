#file
import csv

#Networking
import requests

#Misc
import time
import itertools
from collections import defaultdict

#html parsing tools
from bs4 import BeautifulSoup

########################################################

#set default declaration of list variables
columns = defaultdict(list)
symbols = defaultdict(list)

#open csv file provided by OTC Markets
with open("symbol_info.csv") as f:
	reader=csv.reader(f)
	for row in reader:
        	for (i,v) in enumerate(row):
            		columns[i].append(v)

#create list of symbols to  check
for i in range(1,len(columns[0])):
	symbols[i] = columns[0][i]


#create list of pages
pages = ["http://www.otcmarkets.com/stock/"+ symbols[i] + "/profile" for i in symbols]

with open('stock_emails.csv', 'a') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in range(0,len(pages):
		page = requests.get(pages[i])
		soup = BeautifulSoup(page.content, 'html.parser')
		try:
			email_selector = soup.select("div.compInfo-contactInfo ul.plainMenuVert li a")[1].get_text()
		except Exception as e:
			email_selector = "No Email"

#collect the website through the website selector
		try:
			website_selector = soup.select("div.compInfo-contactInfo ul.plainMenuVert li a")[0].get_text()
		except Exception as e:
			email_selector = "No Website"
		filewriter.writerow([symbols[i], email_selector,website_selector])
	








