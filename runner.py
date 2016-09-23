from util import Util
from exporter import exporter
import time,json
class Runner:
    def __init__(self):
        self.logpath='',
        self.keypath=''
    def run(self):

            try:
                self.start=time.clock()
                self.pathfinder()
                ut=Util(self.keypath)
                ut.keyreader(self.logpath)
                ut.getfile()
                ut.dateextractor()
                ut.fileconverter()
                ut.jsonFileReader()
                exp = exporter()
                exp.excelExporter()
                ut.cleanup()
                self.profileit()
            except Exception:
                print(Exception)
            finally:
                ut.cleanup()






    def profileit(self):
        print("job done in {0}".format(time.clock()-self.start))
    def pathfinder(self):
        with open('config.json','r') as configfile:
            config=json.load(configfile)
            self.keypath=config['logpath']
            self.logpath=config['keypath']
















if __name__== "__main__":
    Runner().run()
