from models import Company
import os, sys ,glob
import logging
class Util:
    '''this is the class responsible for all the donkey work and lifting the load'''
    def __init__(self ):
        self.filepath=' '
        self.filename=''
        self.filelist=[]
        self.companies=[]

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
        self.filepath='/home/micthaworm/Documents/statsCalculations/'
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
        '''try and  create the directory to store the json file make sure it doesnt exist'''
        jsondirpath = '{0}jsonfiles'.format(self.filepath)
        logging.info("json path set to {0}".format(jsondirpath))
        try:
            os.mkdir(jsondirpath)
            print("directory created at path")
        except OSError:
            logging.warning("json file was found ...continuing")
            pass
        for file in files :
            filename=self.getfile(file)

            '''read the log file and write the text to a json file'''
            try:

                logging.info("reading file {0}".format(filename))
                logdata=self.extractLog(file)
                jsonfile = open('{0}/{1}.json'.format(jsondirpath, filename), 'w+')
                logging.info("writing data to {0}".format(jsonfile.name))
                jsonfile.writelines(logdata)
                jsonfile.close()
            except IOError:
                logging.error("there was an error somewhere dummy")



































