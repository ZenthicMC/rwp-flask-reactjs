from array import array
from app.model.products import Products
from app.model.productnotes import Productnotes
from app import response, app, db
from flask import request

def index():
   try:
      products = Products.query.all()
      data = formatarray(products)
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
      'prod_id' : data.prod_id,
      'vend_id' : data.vend_id,
      'prod_name' : data.prod_name,
      'prod_price' : data.prod_price,
      'prod_desc' : data.prod_desc,
   }
   return data

def detail(prod_id):
   try:
      products = Products.query.filter_by(prod_id=prod_id).first()
      productnotes = Productnotes.query.filter(Productnotes.prod_id==prod_id)
      if not products:
         return response.badRequest([],"Tidak ada data Products")

      dataProductNotes = formatProductNotes(productnotes)
      data = singleDetailProductNotes(products, dataProductNotes)

      return response.success(data, "success")

   except Exception as e:
      print(e)

def singleDetailProductNotes(products, productnotes):
   data = {
      'prod_id' : products.prod_id,
      'vend_id' : products.vend_id,
      'prod_name' : products.prod_name,
      'prod_price' : products.prod_price,
      'prod_desc' : products.prod_desc,
      'product_notes' : productnotes
   }
   return data

def singleProductNotes(productsnotes):
   data = {
      'note_id' : productsnotes.note_id,
      'note_text' : productsnotes.note_text,
      'note_date' : productsnotes.note_date,
   }
   return data


def formatProductNotes(data):
   array=[]
   for i in data:
      array.append(singleProductNotes(i))
   return array


def save():
   try:
      prod_id = request.form.get('prod_id')
      vend_id = request.form.get('vend_id')
      prod_name = request.form.get('prod_name')
      prod_price = request.form.get('prod_price')
      prod_desc = request.form.get('prod_desc')

      # Tampung pada sebuah variabel
      saveProducts = Products(prod_id=prod_id, vend_id=vend_id, prod_name=prod_name, prod_price=prod_price, prod_desc=prod_desc)
      db.session.add(saveProducts)
      db.session.commit()

      return response.success('','Sukses Menambahkan Data Products ')
   except Exception as e:
      print(e)

def update(prod_id):
   try:
      vend_id = request.form.get('vend_id')
      prod_name = request.form.get('prod_name')
      prod_price = request.form.get('prod_price')
      prod_desc = request.form.get('prod_desc')
      input = {
         'vend_id' : vend_id,
         'prod_name' : prod_name,
         'prod_price' : prod_price,
         'prod_desc' : prod_desc
      }
      products = Products.query.filter_by(prod_id=prod_id).first()
      products.vend_id = vend_id
      products.prod_name = prod_name
      products.prod_price = prod_price
      products.prod_desc = prod_desc
      db.session.commit()
      return response.success(input, "Sukses Update Data Products")
   except Exception as e:
      print (e)

def delete(prod_id):
   try:
      products = Products.query.filter_by(prod_id=prod_id).first()
      if not products:
         return response.badRequest([], 'Data Products Kosong.....')
      db.session.delete(products)
      db.session.commit()
      return response.success('', 'berhasil Menghapus Data Products')
   except Exception as e:
      print(e)