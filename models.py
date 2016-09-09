class Company(object):
    _usage=0

    def __init__(self,name):
        '''create a new company object from the extracted text'''
        self.transactions=[]
        self.usage=0
        self.date=''
        self.name=name
        pass


    def addTransactionType(self,transaction):
        '''for checking is a transaction type has already been captured is not add it
        and change its usage to 1 if it already exists then just update the transaction usage'''
        self._transactions.append[transaction]
        if transaction in self._transactions:
            self._usage+= 1
        else:
            self._usage=1




