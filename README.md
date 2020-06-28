# NOMSS_warehouse_api
Endpoint that instigates customer order fulfilment. 
This application demonstrates an api that takes in an array of order numbers and uses a local data file to process orders and determine if they can be fulfilled.

This application demonstrates a POST api. 
The api expects to receive an a request structured { "orderIds" : [x,y,z]}.
It returns order ids of orders that could not be fulfilled as a response structed { "unfulfillable": [x,y,z]} 

It includes an extremely simple html page run on port :5000 using checkboxes with order numbers to demonstrate the API receiving and responding to external applications.

## About this app
This app was constructed in python, using elements of the Flask web framework to assist with templating and apis. 


## Time Split
### Designing (~30 mins)
After reading the Tech Challenge brief I noted the requirements and acceptance criteria on a whiteboard.
I then wrote down a rough outline of the processes  
  I mainly noted how I would find the JSON orders based on the ids given.  
  This design process also briefly outlined how I would look at the stock on hand and make adjustments.  
I listed two sets of requirements:
  1. Requirements to get the base api working. 
  2. Requirements to demonstrate the api.
### Creating API (~4 hours)
I created the application and worked on constructing the api.  
There was only one area overlooked in the design stage that I had to fix during construction.  
  This involved orders adjusting stock on the first product, then having their second item unable to be filled.  
  e.g order 1123 processed product 1 and 2, adjusting their stock. Then got flagged as unfulfilled. Then order 1124 was also flagged as unfulfilled as it oculd not process product 2.
### Creating Demonstration & Review (~2 hours)  
This involved the creation of index.html as a quick way to demonstrate the api being accessed via fetch andd viewing the return response.  
In this portion I carefully reviewed the Tech Challenge and test cases. 

## 
