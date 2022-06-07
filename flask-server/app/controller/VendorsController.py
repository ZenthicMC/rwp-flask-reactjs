from array import array
from app.model.vendors import Vendors
from app import response, app, db
from flask import request

def index():
   try:
      vendors = Vendors.query.all()
      data = formatarray(vendors)
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
      'vend_id' : data.vend_id,
      'vend_name' : data.vend_name,
      'vend_address' : data.vend_address,
      'vend_kota' : data.vend_kota,
      'vend_zip' : data.vend_zip,
      'vend_country' : data.vend_country
   }
   return data

def detail(vend_id):
   try:
      vendors = Vendors.query.filter(Vendors.vend_id==vend_id).first()
      if not vendors:
         return response.badRequest([],"Tidak ada data Vendors")

      data = singleObject(vendors)

      return response.success(data, "success")

   except Exception as e:
      print(e)


def save():
   try:
      vend_id = request.form.get('vend_id')
      vend_name = request.form.get('vend_name')
      vend_address = request.form.get('vend_address')
      vend_kota = request.form.get('vend_kota')
      vend_zip = request.form.get('vend_zip')
      vend_country = request.form.get('vend_country')

      # Tampung pada sebuah variabel
      vendors = Vendors(vend_id=vend_id, vend_name=vend_name, vend_address=vend_address, vend_kota=vend_kota, vend_zip=vend_zip, vend_country=vend_country)
      db.session.add(vendors)
      db.session.commit()

      return response.success('','Sukses Menambahkan Data Vendors')
   except Exception as e:
      print(e)

def update(vend_id):
   try:
      vend_name = request.form.get('vend_name')
      vend_address = request.form.get('vend_address')
      vend_kota = request.form.get('vend_kota')
      vend_zip = request.form.get('vend_zip')
      vend_country = request.form.get('vend_country')
      input = {
         'vend_name' : vend_name,
         'vend_address' : vend_address,
         'vend_kota' : vend_kota,
         'vend_zip' : vend_zip,
         'vend_country' : vend_country
      }
      vendors = Vendors.query.filter_by(vend_id=vend_id).first()
      vendors.vend_name = vend_name
      vendors.vend_address = vend_address
      vendors.vend_kota = vend_kota
      vendors.vend_zip = vend_zip
      vendors.vend_country = vend_country
      db.session.commit()
      return response.success(input, "Sukses Update Data Vendors")
   except Exception as e:
      print (e)

def delete(order_item):
   try:
      vendors = Vendors.query.filter_by(order_item=order_item).first()
      if not vendors:
         return response.badRequest([], 'Data Vendors Kosong.....')
      db.session.delete(vendors)
      db.session.commit()
      return response.success('', 'Berhasil Menghapus Data Vendor')
   except Exception as e:
      print(e)