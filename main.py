#Coded By: Paul N Thompson
#Coded for the NOMSS Tech Challenge
#TODO: Tidy code, remove print statements used for troubleshooting
#TODO: Seperate code as needed into appropriate structure
#TODO: Double check Tech Challenge Acceptance Criteria and Test Cases

from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

def getData():
    with open('data.json') as f:
        data = json.load(f)
    return data

def getProduct(productId, productList):
    for product in productList:
        if(product['productId'] == productId):
            return product
    return

#This would create a loop that would call the appropriate APIs to reorder stock
def reorderStock(stockItems):
    
    return

#TODO: If I cannot get the array from the body of the post request, mock a simple webpage and have the order array fed in
@app.route("/")
def home():
    return render_template("main.html")

#TODO: Change this to get the array from a body in the post request.
@app.route("/api/v1/warehouse/fulfilment", methods=['POST'])
def placeOrders(ordersPlaced): 
    orderList = getData()['orders']
    productList = getData()['products']
    pendingOrders = []
    unfulfillableOrders = []
    fulfilledOrders = []
    stockToReorder = []
    
    #Finds the JSON data associated with orderIds from array input
    for order in orderList:
        if order['orderId'] in ordersPlaced:
            pendingOrders.append(order)

    #Loops through all requested orders and determines if they can be filled
    #assumes orders can be filled until proven otherwise
    for order in pendingOrders:
        productsInStock = True
        for desiredItem in order['items']:
            stockItem = getProduct(desiredItem['productId'], productList)

            if (desiredItem['quantity'] > stockItem['quantityOnHand']):
                productsInStock = False
                if order not in unfulfillableOrders:
                    order['status'] = "Error: Unfulfillable"
                    unfulfillableOrders.append(order)

        #if the order was not flagged as unfulfillable then it is filled
        #if stock is taken below threshhold it is noted 
        if productsInStock:
            print("Fulfilling order:" , order["orderId"])
            for desiredItem in order['items']:
                stockItem = getProduct(desiredItem['productId'], productList)
                print("Desired Item:" , desiredItem["productId"])
                print("Desired Qty:" , desiredItem['quantity'])
                print("Existing Qty:" , stockItem['quantityOnHand'])

                stockItem['quantityOnHand'] -= desiredItem['quantity']
                print("Qty after order:" , stockItem['quantityOnHand'])
                print("Qty threshhold:", stockItem['reorderThreshold'])
                if (stockItem['quantityOnHand'] < stockItem['reorderThreshold']):
                    if stockItem not in stockToReorder:
                        stockToReorder.append(stockItem)

            print("------------------------")
            order['status'] = 'Fulfilled'
            fulfilledOrders.append(order)
    
    #Stock is reordered once all fulfillable reorders are placed
    #This is done after to prevent duplicate reorders
    reorderStock(stockToReorder)


    print('Fulfilled:')
    print(fulfilledOrders)
    print("------------------------")
    print('Unfulfilled:')
    print(unfulfillableOrders)
    print("------------------------")
    print("Stock to Reorder:")
    print(stockToReorder)


            
    #print (orderList)
    #print(ordersPlaced)
    return


orders = [1122, 1123, 1124, 1125] 
placeOrders(orders)

if __name__ == "__main__":
    app.run(debug=True)