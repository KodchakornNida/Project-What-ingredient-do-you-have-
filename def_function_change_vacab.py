import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def change_vacab(input_indre):

    df =  pd.read_csv("predata.csv")
    # print(df)

    list_total_name_ingredient = []
    list_total_name_type_food = []
    for index, row in df.iterrows():
        list_row = list(row)
        # print(list_row)
        for index_name_ingredient in range(len(list_row)):
          if index_name_ingredient == 1:
            list_total_name_type_food.append(list_row[index_name_ingredient])

          elif index_name_ingredient >= 3:
            list_total_name_ingredient.append(list_row[index_name_ingredient])

    name_ingredient_final = [name_ingredient for name_ingredient in list_total_name_ingredient if str(name_ingredient) != 'nan']
    name_ingredient_final_1 = set(name_ingredient_final)

    list_total_name_type_food = list(set(list_total_name_type_food))

    df_ingredient = pd.DataFrame(name_ingredient_final_1)

#     print(list_total_name_type_food)
#     print(df_ingredient)
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

    arr_vocab = name_ingredient_final
    
    key  = guess(input_indre,arr_vocab)
    return arr_vocab[key]

# input_indre = 'หัวหอม'
# print(change_vacab(input_indre))