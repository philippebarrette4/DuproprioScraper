import pandas as pd
from openpyxl import load_workbook


#Import excel table into a dataframe
headers = [0,1]
df = pd.read_excel('duproprio.xlsx',sheet_name='Sheet1',
                   dtype={'City': str, 'Price': float})
#Drop the nan value
df.dropna()

#Don't want the scientific notation, so float specification
pd.set_option('display.float_format', lambda x: '%.2f' % x)
#Apply group function (by City column)
df_grouped = df.groupby(['City']).mean()

#Write the dataframe into new excel file
df_grouped.to_excel('filtered_data.xlsx', sheet_name='Sheet1')

