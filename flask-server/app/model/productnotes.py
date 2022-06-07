from app import db
from datetime import datetime
from app.model.products import Products

class Productnotes(db.Model):
   note_id = db.Column(db.CHAR(5), nullable=False, primary_key=True)
   prod_id =db.Column(db.String(10), db.ForeignKey(Products.prod_id))
   note_date=db.Column(db.Date, default=datetime.utcnow)
   note_text=db.Column(db.Text, nullable=False)

   def __repr__(self):
      return '<Productnotes {}>'.format(self.prod_id)
      



