

import urllib.request
import time
import json
import random

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
	""" Produce all of the needed values to generate a datapoint """
	""" ------------- Update this function ------------- """
	stock = quote['stock']
	bid_price = float(quote['top_bid']['price'])
	ask_price = float(quote['top_ask']['price'])
	#make changes to the price return values,this change how price is been computed
	price = (bid_price + ask_price)/2
	return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
	""" Get ratio of price_a and price_b """
	""" ------------- Update this function ------------- """
	""" Also create some unit tests for this function in client_test.py """
	if (price_b == 0):
		#when price_b is 0 to avoid throwing zeroDivisionError
		return
		#effect a change to return value of stock price 
	return price_a/price_b

# Main
if __name__ == "__main__":

	# Query the price once every N seconds.
	for _ in range(N):
		quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

		""" ----------- Update to get the ratio --------------- """
		for quote in quotes:
			stock, bid_price, ask_price, price = getDataPoint(quote)
			
			print ("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
		#update the getRatio output so as to return a value other than 1
		print ("Ratio %s" % getRatio(3.5,2.6))
