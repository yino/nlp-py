from app import db


class User_appkey(db.Model):
    __tablename__ = "user_appkey"
    id = db.Column(db.BigInteger,primary_key = True)
    app_key = db.Column(db.String(255), unique = True)
    app_secret = db.Column(db.String(255), unique = True)
    type = db.Column(db.String(20))
    req_num = db.Column(db.BigInteger)
    user_id = db.Column(db.BigInteger,  primary_key = True)
    created_at = db.Column(db.DateTime(3))
    updated_at = db.Column(db.DateTime(3))
    deleted_at = db.Column(db.DateTime(3))

    def __repr__(self):
       return self.name
    
