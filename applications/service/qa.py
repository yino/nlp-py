from pymysql import NULL

from ..model.qa_question import Qa_question


class Qa:
    def getListByUserId(user_id):
        data =  Qa_question.query.filter(Qa_question.deleted_at == None).filter(Qa_question.user_id==user_id).all()
        result = []
        for val in data:
            result.append({
                "id": val.id,
                "question": val.question,
            })
        return result
