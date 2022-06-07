from app import db
from datetime import datetime
from app.model.customers import Customers

class Orders(db.Model):
    order_num = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date=db.Column(db.Date, default=datetime.utcnow)
    cust_id=db.Column(db.CHAR(5), db.ForeignKey(Customers.cust_id, ondelete='CASCADE'))

    def __repr__(self) :
        return '<Orders {}>'.format(self.order_num)
    