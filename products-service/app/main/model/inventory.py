from .. import db

class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.String(100), unique=True)
    quantity = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return "<Inventory '{}'>".format(self.quantity)
