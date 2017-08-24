from util import Util
from exporter import exporter
import time,json
import logging

###this module bring its all together
class Runner:
    def __init__(self):
        self.logpath='',
        self.keypath=''
        self.date=''
        self.logger = logging.getLogger("STATSREPORTER")
        handler2=logging.StreamHandler()
        handler2.setLevel(logging.INFO)
        ##jsut setting up some loggin stuff
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s -%(levelname)s - %(message)s',
                            datefmt='%y-%m-%d %H:%M',
                            filename='statsreporter.log'
                            )



    def run(self):
        self.logger.log(logging.INFO,"##STARTING SESSION##")
        for date in self.date:
            try:

                self.start=time.clock()
                self.configurator()
                ut=Util(self.keypath,date)
                ut.keyreader(self.logpath)
                ut.fileconverter()
                ut.jsonFileReader()
                exp = exporter(date)
                exp.excelExporter()
                self.profileit()

            except KeyboardInterrupt as e:
                self.logger.error("oops program interrupted ..exiting",str(e))
            finally:
                ut.cleanup()
                self.logger.log(logging.INFO,"##EXITING##")


    def profileit(self):
        ##just for benchmarking
        print("job done in {0}".format(time.clock()-self.start))
    def configurator(self):
        ##reading configuraion parameters
        with open('config.json','r') as configfile:
            config=json.load(configfile)
            try:

                self.keypath=config['logpath']
                self.logpath=config['keypath']
                self.date=config['date']
            except Exception as e:
                self.logger.log(logging.ERROR,"an error occured while reading the config file",str(e))


if __name__== "__main__":

    Runner().run()
