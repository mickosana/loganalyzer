from util import Util
from exporter import exporter
import time,json

class Runner:
    def __init__(self):
        self.logpath='',
        self.keypath=''
        self.date=''
    def run(self):
        try:
            self.start=time.clock()
            self.configurator()
            ut=Util(self.keypath,self.date)
            ut.keyreader(self.logpath)
            ut.fileconverter()
            ut.jsonFileReader()
            exp = exporter(self.date)
            exp.excelExporter()
            self.profileit()

        except KeyboardInterrupt:
            print("operation stopped by user")
        finally:
            ut.cleanup()







    def profileit(self):
        print("job done in {0}".format(time.clock()-self.start))
    def configurator(self):
        with open('config.json','r') as configfile:
            config=json.load(configfile)
            self.keypath=config['logpath']
            self.logpath=config['keypath']
            self.date=config['date']

















if __name__== "__main__":
    Runner().run()
