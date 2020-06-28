#Coded By: Paul N Thompson
#Coded for the NOMSS Tech Challenge
#Stores functions relevant to the application

import json

def getData():
    with open('data.json') as f:
        data = json.load(f)
    return data

def getProduct(productId, productList):
    for product in productList:
        if(product['productId'] == productId):
            return product
    return

#This would loop through stockItems given and call the appropriate api to make the order.
def reorderStock(stockItems):
    print("Reordering Stock: ")
    for stock in stockItems:
        print("Product Id: " + str(stock['productId']))
        print("Current Stock: " + str(stock['quantityOnHand']))
        print("Items: " + str(stock['reorderAmount']))
        print("------------------------")
    return
