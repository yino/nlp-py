from ..model.qa_question import Qa_question


class Qa:
    def getListByUserId(user_id):
        return Qa_question.query().filter(Qa_question.user_id==user_id).find() 
