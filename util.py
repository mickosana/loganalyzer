from models import Company,transaction
import os, sys ,glob ,json,re
import time,ijson
from collections import Counter
class Util:
    '''this is the class responsible for all the donkey work and lifting the load'''
    def __init__(self ,path,date):
        self.filepath = path
        self.filename=''
        self.filelist=[]
        self.companies=[]#list of all companies that will be converted to json
        self.jsondirpath=os.path.join(self.filepath)
        self.tempobject={} #store the transactions temporarily
        self.obj={}
        self.names=[]
        self.date=date
        self.pattern='^request\.log\.({0})'.format(self.date) #pattern used throughout for filtering by date





    def getfile(self,filepath):
        '''the method responsible for taking the file path from the input and extracting
        which will be used to create the json'''

        pathparts=filepath.split('/')
        filename=pathparts[-1]
        return filename
    def filelister(self,path):
        '''it searched through all the files in the directory  and list then one by one'''

        files=glob.glob(os.path.join(path, '*'))

        return files

    def obj_dict(self,obj):
        return obj.__dict__
    def fileconverter(self):
        files=self.filelister(self.filepath)
        for file in files:
            filename = self.getfile(file)

            match=re.match(self.pattern,filename)
            if match!=None:
                os.rename(file,os.path.join("{0}.json".format(file)))

    def cleanup(self):
        files=self.filelister((self.filepath))
        for file in files:
            ext=file.split('.')[-1]

            if ext=='json':
                filename,fileext=os.path.splitext(file)
                os.rename(file,filename)
            else:
                pass


    def progressCalculator(self, load,counter,message):
             '''this is out progress method to be called whever we need to show a bit progress to the user'''

             progress=((counter/len(load))*100)
             if progress != 100:

                 print( "{0}...{1}%".format(message,int(progress)))
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
        counter=0
        message="analyzing data"
        count=Counter()
        for file in files:
            filename=self.getfile(file)
            match=re.match(self.pattern,filename) # check first if the file is a request file for the date stated
            if match!=None:

                '''this results in a string collections of all object lines in the file making it easy for us to look through the linees and convert then to objects we can wwork with'''

                print("working on file {0} \n".format(file))
               

                for key in self.tempobject:#find all keys.json
                     for i in range(len(self.companies)):
                         '''looop through the company list and add the transactions from the transactions llist'''
                         if self.companies[i].key==key:
                             self.companies[i].name=self.obj[key]
                             self.companies[i].transactions=self.tempobject[key]
                             transactions=self.companies[i].transactions
                             for j in range(len(transactions)):
                                 transactions[j].usage=count[(key,transactions[j].type)]

                         else:
                             pass
            self.progressCalculator(files,counter,message)
            counter+=1
            ''''''
            '''write the companies to a json file'''

        f=open('report.json','w+')
        jsonstring=json.dumps(self.companies,default=self.obj_dict)
        f.write(jsonstring)
    def keyreader(self,path):

        with open(os.path.join('{0}/keys.json').format(path)) as f:
            data=ijson.items(f,'')
            for obj in data:
              keys=list(obj.keys())
              for key in keys:
                  self.obj[key]=obj[key]['name']


































































































