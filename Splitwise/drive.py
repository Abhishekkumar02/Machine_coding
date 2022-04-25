import sys
sys.path.append('/Users/avik/Documents/MachineCoding')
from Splitwise.controller.user_controller import UserController
from Splitwise.controller.group_controller import GroupController
from Splitwise.controller.bill_controller import BillController

from Splitwise.services.bill_service import BillService
from Splitwise.services.group_service import GroupService
from Splitwise.services.user_service import UserService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('user1','pawan')
user2 = userController.addUser('user2','abhishek')
user3 = userController.addUser('user3','ashish')
user4 = userController.addUser('user4','abhi')
user5  = userController.addUser('user5','avik')

members  = [user1,user2,user3,user4,user5]
group1 = groupController.addGroup('group1','avengers',members)

contribution ={'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}
paidBy = {'user1':200,'user2':100,'user3':50,'user4':50,'user5':100}

bill1 = billController.addBill('bill1','group1',500,contribution,paidBy)

balance = billController.getUserBalance('user2')
print(balance)
