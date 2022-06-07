from array import array
from app.model.orderitems import Orderitems
from app.model.orders import Orders
from app import response, app, db
from flask import request

def index():
   try:
      orders = Orders.query.all()
      data = formatarray(orders)
      return response.success(data, "success")
   except Exception as e:
      print(e)

def formatarray(datas):
   array = []
   for i in datas:
      array.append(singleObject(i))
   return array

def singleObject(data):
   data = {
      'cust_id' : data.cust_id,
      'order_num' : data.order_num,
      'order_date' : data.order_date,
   }
   return data

def detail(order_num):
   try:
      orders = Orders.query.filter_by(order_num=order_num).first()
      ordersItems = Orderitems.query.filter(Orderitems.order_num==order_num)
      if not orders:
         return response.badRequest([],"Tidak ada data Orders")

      dataOrdersItems = formatOrdersItems(ordersItems)
      data = singleDetailOrdersItems(orders, dataOrdersItems)

      return response.success(data, "success")

   except Exception as e:
      print(e)


def singleDetailOrdersItems(orders, ordersItems):
   data = {
      'cust_id' : orders.cust_id,
      'order_num' : orders.order_num,
      'order_date' : orders.order_date,
      'orders_items' : ordersItems
   }
   return data

def singleOrdersItems(ordersItems):
   data = {
      'order_item' : ordersItems.order_item,
      'prod_id' : ordersItems.prod_id,
      'quantity' : ordersItems.quantity,
      'size' : ordersItems.size
   }
   return data

def formatOrdersItems(data):
   array=[]
   for i in data:
      array.append(singleOrdersItems(i))
   return array


def save():
   try:
      order_num = request.form.get('order_num')
      cust_id = request.form.get('cust_id')
      order_date = request.form.get('order_date')

      # Tampung pada sebuah variabel
      saveOrders= Orders(order_num=order_num, cust_id=cust_id, order_date=order_date)
      db.session.add(saveOrders)
      db.session.commit()

      return response.success('','Sukses Menambahkan Data Orders')
   except Exception as e:
      print(e)


def update(order_num):
   try:
      cust_id = request.form.get('cust_id')
      order_date = request.form.get('order_date')
      input = {
         'cust_id' : cust_id,
         'order_date' : order_date
      }
      orders = Orders.query.filter_by(order_num=order_num).first()
      orders.cust_id = cust_id
      orders.order_date = order_date
      db.session.commit()
      return response.success(input, "Sukses Update Data Orders")
   except Exception as e:
      print (e)


def delete(order_num):
   try:
      orders = Orders.query.filter_by(order_num=order_num).first()
      if not orders:
         return response.badRequest([], 'Data Orders Kosong.....')
      db.session.delete(orders)
      db.session.commit()
      return response.success('', 'berhasil Menghapus Data Orders')
   except Exception as e:
      print(e)