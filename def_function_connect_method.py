import pandas as pd
import numpy as np

def get_total_method(food_name):
    df =  pd.read_csv("total_food_method.csv")
    # print(df)
    df_list = df.values.tolist()
    for name in df_list:
        if food_name in name:
            cleanedList_method = [x for x in name if str(x) != 'nan']
    # print(cleanedList)
    cut_cleandList = cleanedList_method[3:]
    df = pd.DataFrame(cut_cleandList,columns = ['วิธีทำ'])
    return df


food_name = 'ยำสตรอว์เบอรี่กุ้งสด'
print(get_total_method(food_name))