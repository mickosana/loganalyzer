from util import Util
from exporter import exporter
import time
class Runner:

    def run(self):
        self.start=time.clock()
        ut=Util()
        exp=exporter()
        ut.fileconverter()
        ut.jsonFileReader()
        exp.excelExporter()
        self.profileit()
    def profileit(self):
        print(time.clock()-self.start)




if __name__== "__main__":
    Runner().run()
