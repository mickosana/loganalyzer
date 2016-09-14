class Company(object):


    def __init__(self,name):
        '''create a new company object from the extracted text'''
        self.name=name
        self.transactions=[]









class transaction:
    '''a small class to simply calculation of usage and representation of a transaction'''
    def __init__(self,name):
        self.name=name
        self.usage=1


    def addusage(self):
        self.usage+=1

    def usagecalculator(self,usage):
        usage+=1
        self.usage=usage













