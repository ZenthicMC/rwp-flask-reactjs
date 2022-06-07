from app import db
from app.model.orders import Orders
from app.model.products import Products

class Orderitems(db.Model):
   order_item = db.Column(db.Integer, primary_key=True)
   order_num=db.Column(db.Integer, db.ForeignKey(Orders.order_num))
   prod_id=db.Column(db.String(10), db.ForeignKey(Products.prod_id))
   quantity= db.Column(db.Integer, primary_key=True)
   size = db.Column(db.Integer, primary_key=True)

   def __repr__(self) :
      return '<Orderitems {}>'.format(self.order_num)

