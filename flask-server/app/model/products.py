from app import db
from app.model.vendors import Vendors

class Products(db.Model):
   prod_id = db.Column(db.String(10),nullable=False, primary_key=True)
   vend_id = db.Column(db.CHAR(5), db.ForeignKey(Vendors.vend_id))
   prod_name = db.Column(db.String(100), nullable=False)
   prod_price = db.Column(db.Integer, nullable=False)
   prod_desc = db.Column(db.Text, nullable=False)

   def __repr__(self):
      return '<Products {}>'.format(self.prod_id)   

