from email.policy import default
from .. import db

class Discount(db.Model):
    __tablename__ = 'discount'

    id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    discount_percent = db.Column(db.Float, nullable=False)
    active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return "<Discount '{}'>".format(self.name)
