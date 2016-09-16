import pandas as pd
import ijson
class exporter(object):
    def __init__(self):
        self.dataframes = []
    def excelExporter(self):

        with open('report.json') as f:
            data=ijson.items(f,'item')
            for i in data:
                counter=1
                idx=i['name']
                trans=i['transactions']

                dataf=pd.DataFrame(trans,columns=[idx,'type','usage'])
                dataf.index+=1


                self.dataframes.append(dataf)

                counter+=1
                print(dataf)

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('report.xlsx', engine='xlsxwriter')
        workbook = writer.book
        for i in range(len(self.dataframes)):

            counter+=1
            # Convert the dataframe to an XlsxWriter Excel object.
            sheetname = "sheet{0}".format(i)

            self.dataframes[i].to_excel(writer, sheet_name=sheetname)

            worksheet=writer.sheets[sheetname]
            chart=workbook.add_chart({'type':'column'})
            chart.add_series({'values':'={0}!$D$2:$D$12'.format(sheetname),
                              'categories':[sheetname,1,2,13,2],
                              'name':'={0}!$D1'.format(sheetname)})
            worksheet.insert_chart('F3',chart)

            chart.set_title({'name':'={0}!$B$1'.format(sheetname)})

        writer.save()


            # Close the Pandas Excel writer and output the Excel file.





if __name__=='__main__':
    expe=exporter()
    expe.excelExporter()












