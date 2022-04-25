import abc
class BillServiceInterface(metaclass= abc.ABCMeta):
    @abc.abstractmethod
    def addBill(self,id,groupID,amount,contribution,paidBy):
        pass