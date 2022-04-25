from re import A
from Splitwise.services.bill_service_interface import BillServiceInterface
from Splitwise.modules.bill import Bill
class BillService():
    billDetails = {}
    def addBill(self,id,groupId,amount,contribution,paidBy):
        bill = Bill()
        bill.setId(id)
        bill.setGroupId(groupId)
        bill.setAmount(amount)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        self.__class__.billDetails[id] = bill
        return bill

