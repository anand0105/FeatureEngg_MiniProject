# Import data
from datetime import datetime
import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np
import matplotlib.pyplot as plt

resturant_df = pd.read_excel(io='Food Orders - Shared-1.xlsx',sheet_name='SwiggyTo')

# resturant_df.assign(Paneer=(lambda: 1,lambda: 0)[resturant_df['Items'].str.contains('PANEER') == True]())

def calculate_time_difference(data: DataFrame, col1:str, col2:str):
    time_diff = []
    for row in data:
        print(row)
        time_diff.append(datetime.strptime(row[col2],'%d-%B-%Y %I.%M %p') - datetime.strptime(row[col1],'%d-%B-%Y %I.%M %p'))
    return time_diff
calculate_time_difference(resturant_df[['Delivery Time', 'DateTime']], 'Delivery Time', 'DateTime')

for idx, row in resturant_df_binarized[['Delivery Time', 'DateTime']].iterrows():
    print(idx)
    print(row[0])