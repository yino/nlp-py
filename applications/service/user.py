
from ..model.user_appkey import User_appkey


class User:

    def getUserInfoByAk(Ak):
        return User_appkey.query.filter(User_appkey.app_key==Ak).first()
