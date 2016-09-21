from models import Company,transaction
import os, sys ,glob ,json
import logging
import time
import ijson
class Util:
    '''this is the class responsible for all the donkey work and lifting the load'''
    def __init__(self ,path):
        self.filepath = path#'/home/micthaworm/Documents/statsCalculations'
        self.filename=''
        self.filelist=[]
        self.companies=[]#list of all companies that will be converted to json
        self.jsondirpath=os.path.join(self.filepath)
        self.tempobject={} #store the transactions temporarily
        self.obj={}
        self.date=''



    def getfile(self):
        '''the method responsible for taking the file path from the input and extracting
        which will be used to create the json'''

        pathparts=self.filepath.split('/')
        self.filename=pathparts[-1]
        return self.filename
    def filelister(self,path):
        '''it searched through all the files in the directory  and list then one by one'''

        files=glob.glob(os.path.join(path, '*'))
        #for file in files:
           # logging.info("*###listing files###")
            #print(file)
        return files

    def obj_dict(self,obj):
        return obj.__dict__
    def fileconverter(self):
        files=self.filelister(self.filepath)
        for file in files:
            os.rename(file,os.path.join("{0}.json".format(file)))
        self.filename=file.split('/')[-1];

    def cleanup(self):
        files=self.filelister((self.filepath))
        for file in files:
            ext=file.split('.')[-1]

            if ext=='json':
                filename,fileext=os.path.splitext(file)
                os.rename(file,filename)
            else:
                pass


    def progressCalculator(self, load,counter):
             '''this is out progress method to be called whever we need to show a bit progress to the user'''

             progress=((counter/len(load))*100)
             if progress != 100:

                 print( "converting files...{0}%".format(int(progress)))
                 sys.stdout.write("\033[F")  # Cursor up one line
                 time.sleep(1)
             else:
                 print("DONE...:)")
                 sys.stdout.write("\033[F")  # Cursor up one line# #
                 time.sleep(1)
    def jsonFileReader(self):
        ''''this is the slave method for xtracting json objects into company information to be used
          for stats calculation
        '''
        files=self.filelister(self.jsondirpath)

        for file in files:

            jsonfile= open(file, 'r')
            jsonlines=jsonfile.readlines()
            '''this results in a string collections of all object lines in the file making it easy for us to look through the linees and convert then to objects we can wwork with'''
            print("there are {0} lines to be processed".format(len(jsonlines)))
            '''loop through every line and  convert to workable dict'''

            for jsonline in jsonlines:
                jsonobj=json.loads(jsonline)
                co=jsonobj['key']
                type=jsonobj['type']
                transa=transaction(type)
                company=Company(co)
                company.date=self.date
                company.transactions.append(transa)



                '''find id the companies array is empty if not look for a match of the company name in the tempobject list
                if there is an object with tht name traverse find if'''
                if len(self.companies)==0:
                    self.companies.append(company)
                    self.tempobject[company.key]=company.transactions
                    '''create a company if the companies list is empty'''
                else:
                    '''in case where the companies list has something in it then check is the company name is in the
                     the companies list if it does not then do nothing else if it doesnt then add it
                    '''
                    if any(comp for comp in self.companies if comp.key == company.key):
                       pass
                    else:
                       self.companies.append(company)
                       self.tempobject[company.key]=company.transactions
                ''''now that all the companies in the file have been registered then start traversing thtought the transactions
                if the transaction exists then add the usage if not then add the transaction to the list of transactions of
                that company'''
                translist=self.tempobject[company.key]#list of transactions
                if any(tr for tr in translist if tr.type==transa.type):
                    for i in range(len(translist)):
                        translist[i].usage+=1
                else:
                    translist.append(transa)
            '''this is the part where we take all the values in our temparaay object and store then in the companies list'''
            for key in self.tempobject:#find all keys.json
                for i in range(len(self.companies)):
                    '''looop through the company list and add the transactions from the transactions llist'''
                    if self.companies[i].key==key:
                        self.companies[i].name=self.obj[key]
                        self.companies[i].transactions=self.tempobject[key]
                    else:
                        pass
            ''''''
            '''write the companies to a json file'''

        f=open('report.json','w+')
        jsonstring=json.dumps(self.companies,default=self.obj_dict)
        f.write(jsonstring)
    def keyreader(self):

        with open(('keys.json')) as f:
            data=ijson.items(f,'')
            for obj in data:
              keys=list(obj.keys())
              for key in keys:
                  self.obj[key]=obj[key]['name']
        print(self.obj)
    '''this is the function that will take the date from the files extension'''
    def dateextractor(self):
        filename=self.filename
        date=filename.split('.')[-1]
        final=date.split('-')[:2]
        s='-'
        finaldate=s.join(final)
        self.date=finaldate






























































































