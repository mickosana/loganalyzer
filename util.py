from models import Company,transaction
import os, sys ,glob ,json
from decimal import *
import logging
import time
class Util:
    '''this is the class responsible for all the donkey work and lifting the load'''
    def __init__(self ):
        self.filepath = '/home/micthaworm/Documents/statsCalculations/'
        self.filename=''
        self.filelist=[]
        self.companies=[]#list of all companies that will be converted to json
        self.jsondirpath=os.path.join(self.filepath + '/jsonfiles')
        self.tempobject={} #store the transactions temporarily






    def extractLog(self,path):
         '''this is the method responsible for extracting whatever file is given
         after the job is done it sends the a file object with all the data in it
         '''
         logfile = open(path, 'r')
         logdata = logfile.readlines()
         logfile.close()
         return logdata



    def getfile(self,filepath):
        '''the method responsible for taking the file path from the input and extracting
        which will be used to create the json'''
        self.filepath=filepath
        pathparts=filepath.split('/')
        self.filename=pathparts[-1]
        return self.filename
    def filelister(self):
        '''it searched through all the files in the directory  and list then one by one'''

        files=glob.glob(os.path.join(self.filepath, '*'))
        for file in files:
            logging.info("*###listing files###")
            print(file)
        return files
    def fileCamel(self):
        '''responsible for looping through all the files and doing the work that has to be done
        loop through every file and create a json file with the name
        it then takes the filenames in the directory object strips away the filename and create a json file with the same name
        after that it then  appends the name of the file to the path and reads it
        '''
        files=self.filelister()
        counter=1;
        print("There are {0} files to be processed..".format(len(files)))

        '''try and  create the directory to store the json file make sure it doesnt exist'''
        self.jsondirpath = '{0}jsonfiles'.format(self.filepath)
        logging.info("json path set to {0}".format(self.jsondirpath))
        try:
            os.mkdir(self.jsondirpath)
            print("directory created at path")
        except OSError:
            logging.warning("json file was found ...continuing")
            pass
        for file in files :
            filename=self.getfile(file)

            '''read the log file and write the text to a json file'''
            try:

                #print("reading file {0}\n".format(filename))
                logdata=self.extractLog(file)
                jsonfile = open('{0}/{1}.json'.format(self.jsondirpath, filename), 'w+')
                logging.info("writing data to {0}".format(jsonfile.name))
                jsonfile.writelines(logdata)
                self.progressCalculator(files, counter)
                jsonfile.close()

            except IOError:
                logging.error("there was an error somewhere dummy\n")
            finally:

                counter+= 1
    def obj_dict(self,obj):
        return obj.__dict__

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

        counter = 1
        jsonfile= open(os.path.join(self.jsondirpath + '/request.log.2016-08-13.json'), 'r')
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
            company.transactions.append(transa)



            '''find id the companies array is empty if not look for a match of the company name in the tempobject list
               if there is an object with tht name traverse find if'''
            if len(self.companies)==0:
                self.companies.append(company)
                self.tempobject[company.name]=company.transactions
                '''create a company if the companies list is empty'''
            else:
               '''in case where the companies list has something in it then check is the company name is in the
                  the companies list if it does not then do nothing else if it doesnt then add it
               '''
               if any(comp for comp in self.companies if comp.name == company.name):
                   pass
               else:
                   self.companies.append(company)
                   self.tempobject[company.name]=company.transactions
            '''now that all the companies in the file have been registered then start traversing thtought the transactions
               if the transaction exists then add the usage if not then add the transaction to the list of transactions of
               that company'''
            translist=self.tempobject[company.name]#list of transactions
            if any(tr for tr in translist if tr.name==transa.name):
                for i in range(len(translist)):
                    translist[i].usage+=1
            else:
                translist.append(transa)
        '''this is the part where we take all the values in our temparaay object and store then in the companies list'''
        for key in self.tempobject:#find all keys
                for i in range(len(self.companies)):
                    '''looop through the company list and add the transactions from the transactions llist'''
                    if self.companies[i].name==key:
                        self.companies[i].transactions=self.tempobject[key]
                    else:
                        pass
        '''write the companies to a json file'''
        f=open('./file.json','w+')
        jsonstring=json.dumps(self.companies,default=self.obj_dict)
        f.write(jsonstring)























































































