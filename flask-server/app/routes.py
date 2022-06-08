from app import app
from flask import render_template, request
from app.controller import CustomerController
from app.controller import OrdersController
from app.controller import OrderItemsController
from app.controller import ProductsController
from app.controller import ProductNotesController
from app.controller import VendorsController
from flask_cors import CORS, cross_origin

CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
@cross_origin()
def index():
    return "Ini Flask"
    
@app.route("/customers", methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        return CustomerController.index()
    else:
        return CustomerController.save()

@app.route("/customers/<cust_id>", methods=['GET', 'PUT', 'DELETE'])
@cross_origin()
def customersDetail(cust_id):
    if request.method == "GET" :
        return CustomerController.detail(cust_id)
    elif request.method == "PUT":
        return CustomerController.update(cust_id)
    else:
        return CustomerController.delete(cust_id)

@app.route("/orders", methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        return OrdersController.index()
    else:
        return OrdersController.save()

@app.route("/orders/<order_num>", methods=['GET', 'PUT', 'DELETE'])
def ordersDetail(order_num):
    if request.method == "GET" :
        return OrdersController.detail(order_num)
    elif request.method == "PUT":
        return OrdersController.update(order_num)
    else:
        return OrdersController.delete(order_num)


@app.route("/orderitems", methods=['GET', 'POST'])
def orderitems():
    if request.method == 'GET':
        return OrderItemsController.index()
    else:
        return OrderItemsController.save()

@app.route("/orderitems/<order_num>", methods=['GET', 'PUT', 'DELETE'])
def orderitemsDetail(order_num):
    if request.method == "GET" :
        return OrderItemsController.detail(order_num)
    elif request.method == "PUT":
        return OrderItemsController.update(order_num)
    else:
        return OrderItemsController.delete(order_num)

@app.route("/products", methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return ProductsController.index()
    else:
        return ProductsController.save()

@app.route("/products/<prod_id>", methods=['GET', 'PUT', 'DELETE'])
def productsDetail(prod_id):
    if request.method == "GET" :
        return ProductsController.detail(prod_id)
    elif request.method == "PUT":
        return ProductsController.update(prod_id)
    else:
        return ProductsController.delete(prod_id)

@app.route("/productnotes", methods=['GET', 'POST'])
def productnotes():
    if request.method == 'GET':
        return ProductNotesController.index()
    else:
        return ProductNotesController.save()

@app.route("/productnotes/<prod_id>", methods=['GET', 'PUT', 'DELETE'])
def productnotesDetail(prod_id):
    if request.method == "GET" :
        return ProductNotesController.detail(prod_id)
    elif request.method == "PUT":
        return ProductNotesController.update(prod_id)
    else:
        return ProductNotesController.delete(prod_id)

@app.route("/vendors", methods=['GET', 'POST'])
def vendors():
    if request.method == 'GET':
        return VendorsController.index()
    else:
        return VendorsController.save()

@app.route("/vendors/<vendor_id>", methods=['GET', 'PUT', 'DELETE'])
def vendorsDetail(vendor_id):
    if request.method == "GET" :
        return VendorsController.detail(vendor_id)
    elif request.method == "PUT":
        return VendorsController.update(vendor_id)
    else:
        return VendorsController.delete(vendor_id)

# @app.route("/login", methods=['POST'])
# def logins():
#     return UserController.login()


# @app.route("/createadmin", methods=['POST'])
# def users():
#     return UserController.buatAdmin()
