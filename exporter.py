import pandas as pd
import ijson
class exporter(object):
    def __init__(self):
        self.dataframes = []
        self.names=[]
        self.date=''



    def excelExporter(self):

        with open('report.json') as f:
            data=ijson.items(f,'item')
            for i in data:
                counter=1
                idx=i['name']
                trans=i['transactions']
                key=i['key']
                self.date=i['date']
                self.names.append(idx)
                dataf=pd.DataFrame(trans,columns=[idx,'type','usage',key])
                dataf.index+=1
                dataf.set_index(key,inplace=True)


                self.dataframes.append(dataf)

                counter+=1
                print(dataf)

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('{0}.xlsx'.format(self.date) ,engine='xlsxwriter')
        workbook = writer.book
        for i in range(len(self.dataframes)):

            counter+=1
            # Convert the dataframe to an XlsxWriter Excel object.


            self.dataframes[i].to_excel(writer, sheet_name=self.names[i])

            worksheet=writer.sheets[self.names[i]]
            worksheet.write('A1','key')
            chart=workbook.add_chart({'type':'column'})
            chart.add_series({'values':'={0}!$D$2:$D$12'.format(self.names[i]),
                              'categories':[self.names[i],1,2,13,2],
                              'name':'={0}!$D1'.format(self.names[i])})
            worksheet.insert_chart('F3',chart)

            chart.set_title({'name':'={0}!$B$1'.format(self.names[i])})

        writer.save()



            # Close the Pandas Excel writer and output the Excel file.





if __name__=='__main__':
    expe=exporter()
    expe.excelExporter()












