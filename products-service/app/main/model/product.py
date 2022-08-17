from .. import db

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    category_id = db.Column(db.String(255), nullable=False)
    inventory_id = db.Column(db.String(255), nullable=True)
    discount_id = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return "<Product '{}'>".format(self.name)
