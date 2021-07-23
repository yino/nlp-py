import datetime

from . import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key = True, nullable=False)
    name = db.Column(db.String(255), )
    mobile = db.Column(db.BigInteger, unique = True, nullable=False)
    email = db.Column(db.String(100), nullable = True)
    password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255), nullable = True)
    token_expire = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    created_at = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime(3), default = datetime.now, nullable=False)
    deleted_at = db.Column(db.DateTime(3), default = datetime.now, nullable = True)

    def __repr__(self):
        return self.name
