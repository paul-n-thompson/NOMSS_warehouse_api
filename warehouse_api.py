#Coded By: Paul N Thompson
#Coded for the NOMSS Tech Challenge
#Contains api's relevant to the warehouse and order fulfilment

from flask import Flask, render_template, jsonify, request, Blueprint
import json
import functions

warehouse_blueprint = Blueprint('warehouse_blueprint',__name__)

@warehouse_blueprint.route("/api/v1/warehouse/fulfilment", methods=['POST'])
def placeOrders(): 
    ordersPlaced = request.json
    orderList = functions.getData()['orders']
    productList = functions.getData()['products']
    pendingOrders = []
    unfulfillableOrders = []
    fulfilledOrders = []
    stockToReorder = []
    response = {}
    
    #Finds the JSON data associated with orderIds from array input
    for order in orderList:
        if order['orderId'] in ordersPlaced['orderIds']:
            pendingOrders.append(order)

    #Loops through all requested orders and determines if they can be filled
    #assumes orders can be filled until proven otherwise
    for order in pendingOrders:
        if order["items"] is not None and len(order["items"]) > 0:
            productsInStock = True
            for desiredItem in order['items']:
                stockItem = functions.getProduct(desiredItem['productId'], productList)

                if (desiredItem['quantity'] > stockItem['quantityOnHand']):
                    productsInStock = False
                    if order not in unfulfillableOrders:
                        order['status'] = "Error: Unfulfillable"
                        unfulfillableOrders.append(order)

            #if the order was not flagged as unfulfillable then it is filled
            #if stock is taken below threshhold it is noted 
            if productsInStock and order['status'] == 'Pending':
                for desiredItem in order['items']:
                    stockItem = functions.getProduct(desiredItem['productId'], productList)
                    stockItem['quantityOnHand'] -= desiredItem['quantity']
                    if (stockItem['quantityOnHand'] < stockItem['reorderThreshold']):
                        if stockItem not in stockToReorder:
                            stockToReorder.append(stockItem)
                order['status'] = 'Fulfilled'
                fulfilledOrders.append(order)
    
    #Stock is reordered once all fulfillable reorders are placed
    #This is done after to prevent duplicate reorders
    functions.reorderStock(stockToReorder)

    print("Orders Placed:")
    print(ordersPlaced['orderIds'])
    print("------------------------")
    print('Orders Fulfilled:') 
    for order in fulfilledOrders:
        print(order['orderId'])
    print("------------------------")
    print('Orders Unfulfilled:')
    for order in unfulfillableOrders:
        print(order['orderId'])
        if "Unfillable" in response:
            response["Unfillable"].append(order['orderId'])
        else:
            response["Unfillable"] = [order['orderId']]
    print("------------------------")
    
 
            
    #print (orderList)
    #print(ordersPlaced)
    return jsonify(response)
