import json
from collections import OrderedDict
import timeit


__Result = [] # Global list to store dictionay objects. Each object contains key/value pairs (product name : listings list)
__Listings_Dictionary = {} # Global dictionary for listings from the listings file
__Products_Dictionary = {} # Global dictionary for products and associated listing objects


# Parameters : manufacturer name, single listing object from listings file
# Description : This function populates the dictionary,"__Listings_Dictionary", with key/value pairs,
# where manufacturer name is the key and the list of listing objects is the value.
def load_dict(manName,listObj):

	if(__Listings_Dictionary.has_key(manName)):
			__Listings_Dictionary[manName].append(listObj)
	else:
		listings = []
		listings.append(listObj);
		__Listings_Dictionary[manName] = listings


# Parameters : product name, 3 product attributes : family,model,manufacturer
# Description : This function searches the dictionary,"__Listings_Dictionary",firstly
# by manufacturer name, to compare the product name of product objects from the products file,
# to listings in the listings dictionary. If a match is found, the listing object is sent to
# the "add_to_product" function.
def search_dict(productName,attributeA,attributeB,attributeC):

	if(__Listings_Dictionary.has_key(attributeC)):
		for obj in __Listings_Dictionary[attributeC]:
			if attributeA != "none":
				if attributeA.lower() in obj["title"].lower().split() :
					if attributeB in obj["title"].split() :
						add_to_product(productName,obj)
						__Listings_Dictionary[attributeC].remove(obj)
			else:
				if attributeB.lower() in obj["title"].lower().split() :
					add_to_product(productName,obj)
					__Listings_Dictionary[attributeC].remove(obj)


# Parameters : product name, single listing object from listings file
# Description : This function adds a listing object to a dictionary, where
# the key is the product name and the value is a list of lisiting objects.
# The dictionary is then sent to the "add_to_result" function.
def add_to_product(productName,listObj):

	if(__Products_Dictionary.has_key(productName)):
		__Products_Dictionary[productName]["listings"].append(listObj)
		return True;

	listings = []
	listings.append(listObj)
	product = OrderedDict([ ('product_name',productName), ('listings',listings) ])
	__Products_Dictionary[productName] = product
	add_to_result(__Products_Dictionary[productName])
	return True



def add_to_result(producstObj):
	__Result.append(producstObj)

# Parameters : none
# Description : This function reads the files "products.txt" and "listings.txt"
# and processes them for matches between individual products and one or more listings.
def read_files():

	productsFile = "products.txt"
	listingsFile = "listings.txt"

	with open(listingsFile) as l:
		print "loading listings dictionary..."
		for lLine in l:
			listing = json.loads(lLine)
			listingTitle = listing["title"]
			manufacturer = listing["manufacturer"].lower()
			if(len(manufacturer.split()) > 1):
				load_dict(manufacturer.split()[0],listing)
			else:
				load_dict(manufacturer,listing)
		print "listings dictionary loaded."

	with open(productsFile) as p:
		print "matching products with listings(may take a few seconds)..."
		for pLine in p:
			product = json.loads(pLine)
			productName = product["product_name"]
			if "family" in product:
				attrbA = product["family"]
			else:
				attrbA = "none"
			attrbB = product["model"]
			if(len(product["manufacturer"].split()) > 1):
				attrbC = product["manufacturer"].split()[0].lower()
			else:
				attrbC = product["manufacturer"].lower()
			search_dict(productName,attrbA,attrbB,attrbC)
		print "products matched with listings."


read_files()
strs = [json.dumps(obj) for obj in __Result]
s = "%s" % "\n".join(strs)
open('results.txt','w').write(s)
print "see results.txt"
