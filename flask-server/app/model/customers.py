from app import db

class Customers(db.Model):
   cust_id = db.Column(db.CHAR(5), nullable=False, primary_key=True)
   cust_name=db.Column(db.String(50), nullable=False)
   cust_address=db.Column(db.String(50), nullable=False)
   cust_city=db.Column(db.String(20), nullable=False)
   cust_zip=db.Column(db.String(7), nullable=False)
   cust_country=db.Column(db.String(25), nullable=False)
   cust_telp=db.Column(db.String(15), nullable=False)

   def __repr__(self):
      return '<Customers {}>'.format(self.cust_id)
      
