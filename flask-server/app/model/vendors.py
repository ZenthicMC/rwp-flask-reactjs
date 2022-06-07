from app import db

class Vendors(db.Model):
   vend_id = db.Column(db.CHAR(5),nullable=False, primary_key=True)
   vend_name=db.Column(db.String(50), nullable=False)
   vend_address=db.Column(db.Text, nullable=False)
   vend_kota=db.Column(db.Text, nullable=False)
   vend_zip=db.Column(db.String(7), nullable=False)
   vend_country=db.Column(db.String(25), nullable=False)

   def __repr__(self):
      return '<Vendors {}>'.format(self.vend_id)

      