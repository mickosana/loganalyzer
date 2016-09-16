import pandas as pd
import ijson

dataframes=[]
with open('request.log.2016-08-25.json') as f:
    data=ijson.items(f,'item')
    for i in data:
        counter=1
        idx=i['name']
        trans=i['transactions']
        dataf="df{0}".format(counter)
        dataf=pd.DataFrame(trans,columns=[idx,'name','usage'])

        dataf.index+=1

        dataframes.append(dataf)

        counter+=1
        print(dataf)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

for i in range(len(dataframes)):


    # Convert the dataframe to an XlsxWriter Excel object.
    sheetname = "sheet{0}".format(i)

    dataframes[i].to_excel(writer, sheet_name=sheetname)


    # Close the Pandas Excel writer and output the Excel file.

writer.save()
















