
class User(object):
    def __init__(self):
        self.Id = None
        self.Name = None
    
    def setId(self,Id):
        self.Id = Id
    
    def getId(self):
        return self.Id
    
    def setName(self, Name):
        self.Name = Name

    def getName(self):
        return self.Name