class Bill(object):
    def __init__(self):
        self.Id = None
        self.groupId = None
        self.amount = 0
        self.contribution = {}
        self.paidBy ={}
    
    def setId(self,Id):
        self.Id = Id
    
    def getId(self):
        return self.Id

    def setGroupId(self,groupId):
        self.groupId = groupId
    
    def retGroupId(self):
        return self.groupId

    def setAmount(self,amount):
        self.amount = amount
    
    def getAmount(self):
        return self.amount
    
    def setContribution(self, contribution):
        self.contribution = contribution

    def getContribution(self):
        return self.contribution
    
    def setPaidBy(self, paidBy):
        self.paidBy = paidBy

    def getPaidBy(self):
        return self.paidBy

    
