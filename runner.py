from util import Util
from exporter import exporter
import time
class Runner:

    def run(self):


            self.start=time.clock()
            path=self.menu()
            ut=Util(path)
            ut.keyreader()
            ut.getfile()
            ut.dateextractor()
            ut.fileconverter()
            ut.jsonFileReader()
            exp = exporter()
            exp.excelExporter()
            ut.cleanup()
            self.profileit()





    def profileit(self):
        print(time.clock()-self.start)
    def menu(self):
        print("#########################################\n"
              "#                                        #\n"
              "# STATS REPORTER                        #\n"
              "#                                        #\n"
              "##########################################\n")
        path= input("enter the path to the log files:")
        return path














if __name__== "__main__":
    Runner().run()
