from . import db


class Qa_question(db.Model):
    __tablename__ = "qa_questions"
    id = db.Column(db.BigInteger, primary_key = True)
    question = db.Column(db.String(255))
    answer = db.Column(db.String(255))
    pid = db.Column(db.Integer, unique = True)
    user_id = db.Column(db.BigInteger)
    type = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime(3))
    updated_at = db.Column(db.DateTime(3))
    deleted_at = db.Column(db.DateTime(3))

    # def __repr__(self):
    #     return self.name
