from array import array
from app.model.orderitems import Orderitems
from app import response, app, db
from flask import request

def index():
   try:
      ordersitems = Orderitems.query.all()
      data = formatarray(ordersitems)
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
      'order_item' : data.order_item,
      'order_num' : data.order_num,
      'prod_id' : data.prod_id,
      'quantity' : data.quantity,
      'size' : data.size
   }
   return data

def detail(order_item):
   try:
      ordersItems = Orderitems.query.filter(Orderitems.order_item==order_item).first()
      if not ordersItems:
         return response.badRequest([],"Tidak ada data Orders Items")

      data = singleObject(ordersItems)

      return response.success(data, "success")

   except Exception as e:
      print(e)


def save():
   try:
      order_item = request.form.get('order_item')
      order_num = request.form.get('order_num')
      prod_id = request.form.get('prod_id')
      quantity = request.form.get('quantity')
      size = request.form.get('size')

      # Tampung pada sebuah variabel
      saveOrdersItems = Orderitems(order_item=order_item, order_num=order_num, prod_id=prod_id, quantity=quantity, size=size)
      db.session.add(saveOrdersItems)
      db.session.commit()

      return response.success('','Sukses Menambahkan Data Orders Items')
   except Exception as e:
      print(e)

def update(order_item):
   try:
      order_num = request.form.get('order_num')
      prod_id = request.form.get('prod_id')
      quantity = request.form.get('quantity')
      size = request.form.get('size')
      input = {
         'order_num' : order_num,
         'prod_id' : prod_id,
         'quantity' : quantity,
         'size' : size
      }
      ordersItems = Orderitems.query.filter_by(order_item=order_item).first()
      ordersItems.order_num = order_num
      ordersItems.prod_id = prod_id
      ordersItems.quantity = quantity
      ordersItems.size = size
      db.session.commit()
      return response.success(input, "Sukses Update Data Orders Items")
   except Exception as e:
      print (e)


def delete(order_item):
   try:
      ordersItems = Orderitems.query.filter_by(order_item=order_item).first()
      if not ordersItems:
         return response.badRequest([], 'Data Orders Kosong.....')
      db.session.delete(ordersItems)
      db.session.commit()
      return response.success('', 'berhasil Menghapus Data Orders Items')
   except Exception as e:
      print(e)