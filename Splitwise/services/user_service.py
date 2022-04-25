from Splitwise.services.user_service_interface import UserServiceInterface
from Splitwise.modules.user import User
class UserService():
    userDetails = {}
    def addUser(self,id,name):
        user = User()
        user.setId(id)
        user.setName(name)
        self.__class__.userDetails[id] = user
        return user
        
