from array import array
from app.model.productnotes import Productnotes
from app import response, app, db
from flask import request

def index():
   try:
      productNotes = Productnotes.query.all()
      data = formatarray(productNotes)
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
      'note_id' : data.note_id,
      'prod_id' : data.prod_id,
      'note_date' : data.note_date,
      'note_text' : data.note_text
   }
   return data

def detail(note_id):
   try:
      productNotes = Productnotes.query.filter(Productnotes.note_id==note_id).first()
      if not productNotes:
         return response.badRequest([],"Tidak ada data Product Notes")

      data = singleObject(productNotes)

      return response.success(data, "success")

   except Exception as e:
      print(e)


def save():
   try:
      note_id = request.form.get('note_id')
      prod_id = request.form.get('prod_id')
      note_date = request.form.get('note_date')
      note_text = request.form.get('note_text')

      # Tampung pada sebuah variabel
      saveProductNotes = Productnotes(note_id=note_id, prod_id=prod_id, note_date=note_date, note_text=note_text)
      db.session.add(saveProductNotes)
      db.session.commit()

      return response.success('','Sukses Menambahkan Data Product Notes')
   except Exception as e:
      print(e)

def update(note_id):
   try:
      prod_id = request.form.get('prod_id')
      note_date = request.form.get('note_date')
      note_text = request.form.get('note_text')
      input = {
         'prod_id' : prod_id,
         'note_date' : note_date,
         'note_text' : note_text
      }
      productNotes = Productnotes.query.filter_by(note_id=note_id).first()
      productNotes.prod_id = prod_id
      productNotes.note_date = note_date
      productNotes.note_text = note_text
      db.session.commit()
      return response.success(input, "Sukses Update Data Product Notes")
   except Exception as e:
      print (e)

def delete(order_item):
   try:
      productNotes = Productnotes.query.filter_by(order_item=order_item).first()
      if not productNotes:
         return response.badRequest([], 'Data Product Notes Kosong.....')
      db.session.delete(productNotes)
      db.session.commit()
      return response.success('', 'berhasil Menghapus Data Product Notes')
   except Exception as e:
      print(e)