import pandas as pd
 
 
# Reading the csv file
df_new = pd.read_csv('info.csv')
 
# saving xlsx file
change = pd.ExcelWriter('info.xlsx')
df_new.to_excel(change, index=False)
 
change.save()