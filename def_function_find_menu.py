import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_menu(input_type,input_indre):
    df =  pd.read_csv("predata.csv")
    # print(df)

    list_total_name_ingredient = []
    list_total_name_type_food = []
    num_total_ingredient = {}

    for index, row in df.iterrows():
        list_row = list(row)
        list_row_re_nan = [t for t in list_row if str(t) != 'nan']
    #     print(list_row_re_nan)
    #     print(len(list_row_re_nan))
        if len(list_row_re_nan) != 0:
        
            name_index = list_row_re_nan[2]
     
            # print(name_index)
            num_total_ingredient[name_index] = int(len(list_row_re_nan))-3
            # print(len(list_row_re_nan))
            # print(num_total_ingredient[name_index])

        
    
        for index_name_ingredient in range(len(list_row)):
            if index_name_ingredient == 1:
                list_total_name_type_food.append(list_row[index_name_ingredient])

            elif index_name_ingredient >= 3:
                list_total_name_ingredient.append(list_row[index_name_ingredient])
                
    name_ingredient_final = [name_ingredient for name_ingredient in list_total_name_ingredient if str(name_ingredient) != 'nan']
    name_ingredient_final_1 = set(name_ingredient_final)

    list_total_name_type_food = list(set(list_total_name_type_food))

    df_ingredient = pd.DataFrame(name_ingredient_final_1)
    # print(df_ingredient)
    # print(num_total_ingredient)

    # print(list_total_name_type_food)
    # print(df_ingredient)
    df_ingredient.to_csv('ingredient.csv')


    def Word2OneHot(word):
        l_tmp = {}
        l=len(word)
        for i in range(l):
            char = word[i]
            l_tmp[char] = 1
        return l_tmp

    def guess(word,vocab):
        arr_vocab = []
        arr_guess = []
        for i in vocab:
            arr_vocab.append(Word2OneHot(i)) 
        arr_vocab.append(Word2OneHot(word))
        df_vocab = pd.DataFrame(arr_vocab).fillna(0)
        results = cosine_similarity(df_vocab)
        arr_weight = results[len(results)-1]
        maxvalue = 0
        maxkey = 0
        for i in range(0,len(arr_weight)-1):
            if arr_weight[i] > maxvalue:
                maxvalue = arr_weight[i]
                maxkey = i
        return maxkey


    dict_name_food = {}
    input_cat = input_type
    for name_type in input_cat:
        for index, row in df.iterrows():
            if row['Type_Food'] == name_type:
                score = 0
                for i in input_indre:
                    for j in df.columns:
                        if i == row[j]:
                            score += 1
                    if score > 0 :
                        dict_name_food[row['Name_Food']] = score
    #                     print(f"{row['Type_Food']} : {row['Name_Food']}")
    sorted_dict_name_food = {k: v for k, v in sorted(dict_name_food.items(), key=lambda item: item[1],reverse=True)}
    # print(sorted_dict_name_food)

    
    #find max type 
    find_max_type = [0]
    
    for name_f,count_same in sorted_dict_name_food.items():
        index_find_type =  df[df['Name_Food']==name_f].index.values
#         print(index_find_type)
        find_type = df.loc[index_find_type, 'Type_Food']
        find_type_torist = find_type.tolist()
        find_max_type.append(len(find_type))
    max_find_max_type = max(find_max_type)
    # print(max_find_max_type)

    list_dict_name_three = []
    #create list to make dataframe
    for name_f,count_same in sorted_dict_name_food.items():
        index_find_type =  df[df['Name_Food']==name_f].index.values
        find_type = df.loc[index_find_type, 'Type_Food']
        find_type_torist = find_type.tolist()
        list_dict_name_three_temp =[]
        if len(find_type_torist) == max(find_max_type):
            for t in find_type_torist:
                list_dict_name_three_temp.append(t)
        else:
            num_nan = max(find_max_type)-len(find_type_torist)
            for tt in find_type_torist:
                list_dict_name_three_temp.append(tt)
            for n in range(num_nan):
                list_dict_name_three_temp.append('')
            
        # print(len(list_dict_name_three_temp))
        # print(list_dict_name_three_temp)
                    
       
        list_dict_name_three_temp.append(name_f)
        list_dict_name_three_temp.append(count_same)
        list_dict_name_three_temp.append(num_total_ingredient[name_f] - count_same)
        list_dict_name_three.append(list_dict_name_three_temp)
    # print(list_dict_name_three)
        
    column_n = []
    for c in range(max_find_max_type):
        column_n.append(f'ประเภท {c+1}')
    column_n.append('เมนูอาหาร')    
    column_n.append('บ้านมี')
    column_n.append('บ้านไม่มี') 
    # print(column_n)
        
    df_list_dict_name = pd.DataFrame(list_dict_name_three,columns= column_n)
    
    return df_list_dict_name


def gen_column(input_type,input_indre):
    df =  pd.read_csv("predata.csv")
    # print(df)

    list_total_name_ingredient = []
    list_total_name_type_food = []
    num_total_ingredient = {}

    for index, row in df.iterrows():
        list_row = list(row)
        list_row_re_nan = [t for t in list_row if str(t) != 'nan']
        if len(list_row_re_nan) != 0:
        
            name_index = list_row_re_nan[2]
            # print(name_index)
            # print(len(list_row_re_nan))
            num_total_ingredient[name_index] = int(len(list_row_re_nan))-3
        
    
        for index_name_ingredient in range(len(list_row)):
            if index_name_ingredient == 1:
                list_total_name_type_food.append(list_row[index_name_ingredient])

            elif index_name_ingredient >= 3:
                list_total_name_ingredient.append(list_row[index_name_ingredient])
                
    name_ingredient_final = [name_ingredient for name_ingredient in list_total_name_ingredient if str(name_ingredient) != 'nan']
    name_ingredient_final_1 = set(name_ingredient_final)

    list_total_name_type_food = list(set(list_total_name_type_food))

    df_ingredient = pd.DataFrame(name_ingredient_final_1)
    # print(num_total_ingredient)

    # print(list_total_name_type_food)
    # print(df_ingredient)
    df_ingredient.to_csv('ingredient.csv')


    def Word2OneHot(word):
        l_tmp = {}
        l=len(word)
        for i in range(l):
            char = word[i]
            l_tmp[char] = 1
        return l_tmp

    def guess(word,vocab):
        arr_vocab = []
        arr_guess = []
        for i in vocab:
            arr_vocab.append(Word2OneHot(i)) 
        arr_vocab.append(Word2OneHot(word))
        df_vocab = pd.DataFrame(arr_vocab).fillna(0)
        results = cosine_similarity(df_vocab)
        arr_weight = results[len(results)-1]
        maxvalue = 0
        maxkey = 0
        for i in range(0,len(arr_weight)-1):
            if arr_weight[i] > maxvalue:
                maxvalue = arr_weight[i]
                maxkey = i
        return maxkey


    dict_name_food = {}
    input_cat = input_type
    for name_type in input_cat:
        for index, row in df.iterrows():
            if row['Type_Food'] == name_type:
                score = 0
                for i in input_indre:
                    for j in df.columns:
                        if i == row[j]:
                            score += 1
                    if score > 0 :
                        dict_name_food[row['Name_Food']] = score
    #                     print(f"{row['Type_Food']} : {row['Name_Food']}")
    sorted_dict_name_food = {k: v for k, v in sorted(dict_name_food.items(), key=lambda item: item[1],reverse=True)}
    # print(sorted_dict_name_food)

    
    #find max type 
    find_max_type = [0]
    
    for name_f,count_same in sorted_dict_name_food.items():
        index_find_type =  df[df['Name_Food']==name_f].index.values
#         print(index_find_type)
        find_type = df.loc[index_find_type, 'Type_Food']
        find_type_torist = find_type.tolist()
        find_max_type.append(len(find_type))
    max_find_max_type = max(find_max_type)
    # print(max_find_max_type)

    list_dict_name_three = []
    #create list to make dataframe
    for name_f,count_same in sorted_dict_name_food.items():
        index_find_type =  df[df['Name_Food']==name_f].index.values
        find_type = df.loc[index_find_type, 'Type_Food']
        find_type_torist = find_type.tolist()
        list_dict_name_three_temp =[]
        if len(find_type_torist) == max(find_max_type):
            for t in find_type_torist:
                list_dict_name_three_temp.append(t)
        else:
            num_nan = max(find_max_type)-len(find_type_torist)
            for tt in find_type_torist:
                list_dict_name_three_temp.append(tt)
            for n in range(num_nan):
                list_dict_name_three_temp.append('')
            
        # print(len(list_dict_name_three_temp))
        # print(list_dict_name_three_temp)
                    
       
        list_dict_name_three_temp.append(name_f)
        list_dict_name_three_temp.append(count_same)
        list_dict_name_three_temp.append(num_total_ingredient[name_f] - count_same)
        list_dict_name_three.append(list_dict_name_three_temp)
    # print(list_dict_name_three)
        
    column_n = []
    for c in range(max_find_max_type):
        column_n.append(f'ประเภท {c+1}')
    column_n.append('เมนูอาหาร')    
    column_n.append('บ้านมี')
    column_n.append('บ้านไม่มี') 
    # print(column_n)
        
    df_list_dict_name = pd.DataFrame(list_dict_name_three,columns= column_n)
    
    return column_n
    

def get_all_menu():
    df =  pd.read_csv("predata.csv")
    # print(df)

    list_total_name_food = []
   

    for index, row in df.iterrows():
        list_row = list(row)
        list_row_re_nan = [t for t in list_row if str(t) != 'nan']
        if len(list_row_re_nan) != 0:
            name_index = list_row_re_nan[2]
            list_total_name_food.append(name_index)
    # print(type(list_total_name_food))
    return list_total_name_food
 
    #     print(name_index)






