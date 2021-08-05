from re import T

import nlp_tfidf
from applications.service import user
from pymysql import NULL

from ..model.qa_question import Qa_question


class Qa:
    def getListByUserId(self, user_id):
        data =  Qa_question.query.filter(Qa_question.deleted_at == None).filter(Qa_question.user_id==user_id).all()
        result = []
        for val in data:
            result.append({
                "id": val.id,
                "question": val.question,
                "answer": val.answer
            })
        return result

    def trainModel(self, user_id):
        Tfidf = nlp_tfidf.Tfidf(work_dir="model/qa/%d" % (user_id), work_file_prefix=str(user_id))
        data = self.getListByUserId(user_id)
        question_list = []
        answer_list = []
        for val in data:
            question_list.append(val['question'])
            answer_list.append(val['answer'])
        print(question_list)
        res = Tfidf.save_model(question_list=question_list,answer_list=answer_list)
        print(res)
        return res

    def match(self,user_id,input_question):
        Tfidf = nlp_tfidf.Tfidf(work_dir="model/qa/%d" % (user_id), work_file_prefix=str(user_id))
        data = Tfidf.run(question=input_question)
        print(data)
        return data
