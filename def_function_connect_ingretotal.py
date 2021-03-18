import pandas as pd
import numpy as np

def get_total_ingredient(food_name):
    df =  pd.read_csv("pre_total_ingredient.csv")
    # print(df)
    df_list = df.values.tolist()
    for name in df_list:
        if food_name in name:
            cleanedList = [x for x in name if str(x) != 'nan']
    # print(cleanedList)
    cut_cleandList = cleanedList[3:]
    df = pd.DataFrame(cut_cleandList,columns = ['ส่วนผสม'])
    return df


food_name = 'ยำสตรอว์เบอรี่กุ้งสด'
print(get_total_ingredient(food_name))