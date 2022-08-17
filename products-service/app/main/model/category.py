from .. import db

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return "<Category '{}'>".format(self.name)
