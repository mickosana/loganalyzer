import pandas as pd
import ijson
class exporter(object):
    def __init__(self,date):
        self.dataframes = []
        self.names=[]##names for all the work sheets one by one
        self.date=date
        self.tempnames=[]
        self.totalRequests=[]
        self.indexes=[]




    def excelExporter(self):

        with open('report.json') as f:
            data=ijson.items(f,'item')
            for i in data:
                sum=0;
                obj={}
                counter=1
                idx=i['name']
                trans=i['transactions']
                key=i['key']
                trans[0]['name']=idx
                trans[0]['key']=key
                for i in trans:
                    sum=sum+i['usage']
                self.names.append(idx)
                dataf=pd.DataFrame(trans,columns=['key','name','type','usage'])
                dataf.index+=1
                self.dataframes.append(dataf)
                obj['Total Requests'] = sum
                obj['name']=idx
                self.totalRequests.append(obj)

                counter+=1

        summaryDataFrame = pd.DataFrame(self.totalRequests,columns=['name','Total Requests'])
        summaryDataFrame.set_index('name',inplace=True)

        print(summaryDataFrame)
        #Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('{0}.xlsx'.format(self.date) ,engine='xlsxwriter')
        workbook = writer.book
        #create an exccel sheet that has the summary of all the type of requests
        summaryDataFrame.to_excel(writer,sheet_name='Usage summary')
        sheet=writer.sheets['Usage summary']
        ##give title and data for each
        sheet.write('A18','Total Overall Requests')
        sheet.write_formula('B18','=SUM(B2:B17)')
        for i in range(len(self.dataframes)):

            counter+=1
            #Convert the dataframe to an XlsxWriter Excel object.


            self.dataframes[i].to_excel(writer, sheet_name=self.names[i])

            worksheet=writer.sheets[self.names[i]]
            chart=workbook.add_chart({'type':'column'})
            chart.add_series({'values':'={0}!$E$2:$E$12'.format(self.names[i]),
                              'categories':[self.names[i],1,3,13,3],
                              'name':'={0}!$D1'.format(self.names[i])}
                             )
            ##draws a chart on the f# collumn of that nth sheet
            worksheet.insert_chart('F3',chart)
            #set the title of the sheet
            chart.set_title({'name':'={0}!$C$2'.format(self.names[i])})
            #give the title
            worksheet.write('D15','Total Requests')
            worksheet.write_formula('E15','=SUM(E2:E14)')


        writer.save()



            # Close the Pandas Excel writer and output the Excel file.















