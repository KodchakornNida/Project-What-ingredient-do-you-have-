from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from def_function_change_vacab import change_vacab
from pandastable import Table, TableModel
from def_function_find_menu import find_menu
from def_function_find_menu import gen_column, get_all_menu
from def_function_connect_method import get_total_method
from def_function_connect_ingretotal import get_total_ingredient
from PIL import ImageTk, Image
import os

root = Tk()
root.title('Project')
Indredient_input_list = []
Type_Food_list = []
def delete():
    Indredient_input_list.pop(Ingredient_list.curselection()[0])
    Ingredient_list.delete(0, END)
    for x in Indredient_input_list:
        Ingredient_list.insert(END, x + '\n')
    
def append_ingredient():
    if Entry_Ingredient.get() != "":
        correct_ingredient = change_vacab(Entry_Ingredient.get())
        Ingredient_list.delete(0, END)  #clear listbox
        Indredient_input_list.append(correct_ingredient)
        for x in Indredient_input_list:
            Ingredient_list.insert(END, x + '\n')
        Entry_Ingredient.delete(0, END)

def sortby(tv, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tv.set(child, col), child) \
        for child in tv.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tv.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tv.heading(col, command=lambda col=col: sortby(tv, col, \
        int(not descending)))

def pop_window(event):
    data =  tv.selection()[0]
    # print(data)
    data_item = tv.item(data,'values')
    # print('aaaaaaaaaa')
    list_data_item =list(data_item)
    
    # print(list_data_item)
    for nf in list_data_item:
        # print(nf)
        if nf in get_all_menu() :
            currfood = nf
            print(currfood)
    top = Toplevel(root)
    top.title('Food Information')
    # top = tk.Toplevel(root)

    # Label Frame pic---------------------------------------------------------------------------------------------------
    labelframe_pic = LabelFrame(top, text=currfood ,padx=15, pady=15,font='Helvetica 12 bold')
    labelframe_pic.pack(fill="both", expand="yes",padx=5, pady=5)
    # Label Frame pic ---------------------------------------------------------------------------------------------------

    # Label Frame pop 1---------------------------------------------------------------------------------------------------
    labelframe_pop_1 = LabelFrame(top, text="ส่วนผสม",padx=15, pady=15,font='Helvetica 12 bold')
    labelframe_pop_1.pack(fill="both", expand="yes",padx=5, pady=5)
    # Label Frame pop 1 ---------------------------------------------------------------------------------------------------

    # Label Frame pop 2---------------------------------------------------------------------------------------------------
    labelframe_pop_2 = LabelFrame(top, text="วิธีทำ",padx=15, pady=15,font='Helvetica 12 bold')
    labelframe_pop_2.pack(fill="both", expand="yes",padx=5, pady=5)
    # Label Frame ---------------------------------------------------------------------------------------------------

    # Ingredient ---------------------------------------------------------------------------------------------------
    df = get_total_ingredient(currfood)
    pt = Table(labelframe_pop_1, dataframe=df,showtoolbar=False, showstatusbar=False)
    pt.show()
    pt.redraw()

    # Method ---------------------------------------------------------------------------------------------------
    df_method = get_total_method(currfood)
    pt = Table(labelframe_pop_2 ,dataframe=df_method,showtoolbar=False, showstatusbar=False)
    
    pt.show()
    pt.columnconfigure(1, weight=3)
    pt.redraw()

    
    # display pic --------------------------------------------------------------------------------------------------

     
    stim_filename = 'image\\'+currfood+".jpg"
    Img_pil = Image.open(stim_filename)
    Img_TK = ImageTk.PhotoImage(Img_pil)

    label1 = Label(labelframe_pic,image = Img_TK)
    label1.image = Img_TK
    label1.pack()
    


def type_food():
    x = tv.get_children()
    # print(x)
    for child in x:
        tv.delete(child)
    Type_Food_list = []
    if var_boil.get() == 1:
        Type_Food_list.append('ต้ม')
    if var_grill.get() == 1:
        Type_Food_list.append('ปิ้งย่าง')
    if var_food_j.get() == 1:
        Type_Food_list.append('อาหารเจ')
    if var_puff.get() == 1:
        Type_Food_list.append('ผัด') 
    if var_steam.get() == 1:
        Type_Food_list.append('นึ่ง')
    if var_yum.get() == 1:
        Type_Food_list.append('ยำ')
    if var_fried.get() == 1:
        Type_Food_list.append('ทอด')
    
    # print(Type_Food_list)
    column_gen = tuple(gen_column(Type_Food_list,Indredient_input_list))
    # print(column_gen)

    # x = tv.get_children()
    # for child in x:
    #     tv.delete(child)
    # tv = ttk.Treeview(labelframe3,columns=column_gen,show="headings",height="5")
    tv.configure(columns = column_gen)
    for i in range(len(column_gen)):
        tv.heading(i,text=column_gen[i],command=lambda c=column_gen[i]: sortby(tv,c, 0))
        tv.column(i, anchor="e")   


    df = find_menu(Type_Food_list,Indredient_input_list)
    # print(df)
    df_list = df.values.tolist()
    for row in df_list:
        # print(row)
        tv.insert("","end",values=row)

    tv.bind("<Double-Button-1>", pop_window)
    # # tv.config(yscrollcommand=scrollbar.set)
    # scrollbar.config(command=tv.yview)


# Label Frame ---------------------------------------------------------------------------------------------------
labelframe = LabelFrame(root, text="สั่งอาหาร",padx=15, pady=15,font='Helvetica 12 bold')
labelframe.pack(fill="both", expand="yes",padx=5, pady=5)
# Label Frame ---------------------------------------------------------------------------------------------------

# Let Go botton ---------------------------------------------------------------------------------------------------
Button_Delete_Ingredient = Button(root, text ="Let Go!",command = type_food, bg='blue', fg='white')
Button_Delete_Ingredient.pack(fill="both", expand="yes",padx=5, pady=5)
# Let Go botton ---------------------------------------------------------------------------------------------------

# Label Frame 3 ---------------------------------------------------------------------------------------------------
labelframe3 = LabelFrame(root, text="Result",padx=15, pady=15,font='Helvetica 12 bold')
labelframe3.pack(fill="both", expand="yes",padx=5, pady=5)
scrollbar = Scrollbar(labelframe3)
scrollbar.pack(side=RIGHT, fill=Y)
tv = ttk.Treeview(labelframe3,columns = (1,2,3),show="headings",height="5")
tv.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tv.yview)
tv.pack()
# Label Frame 3 ---------------------------------------------------------------------------------------------------

#  ---------------------------------------------------------------------------------------------------
# label text 
textngongo = Label(labelframe, text ='Select type of Food',font='Helvetica 10 bold')
textngongo.grid(row=0, column=0,padx=5, pady=5)

# check buttons 
var_boil = IntVar()
boil = Checkbutton(labelframe, text ='ต้ม',variable=var_boil,  onvalue = 1,  offvalue = 0)
boil.grid(row=1, column=0,padx=5, pady=5,sticky=W)

var_grill = IntVar()
grill = Checkbutton(labelframe, text ='ปิ้งย่าง',variable=var_grill,  onvalue = 1,  offvalue = 0)
grill.grid(row=2, column=0,padx=5, pady=5,sticky=W)

var_food_j = IntVar()
food_j = Checkbutton(labelframe, text ='อาหารเจ',variable=var_food_j,  onvalue = 1,  offvalue = 0)
food_j.grid(row=3, column=0,padx=5, pady=5,sticky=W)

var_puff = IntVar()
puff = Checkbutton(labelframe, text ='ผัด',variable=var_puff,  onvalue = 1,  offvalue = 0)
puff.grid(row=4, column=0,padx=5, pady=5,sticky=W)

var_steam = IntVar()
steam = Checkbutton(labelframe, text ='นึ่ง',variable=var_steam,  onvalue = 1,  offvalue = 0)
steam.grid(row=1, column=1,padx=5, pady=5,sticky=W)

var_yum = IntVar()
yum = Checkbutton(labelframe, text ='ยำ',variable=var_yum,  onvalue = 1,  offvalue = 0)
yum.grid(row=2, column=1,padx=5, pady=5,sticky=W)

var_fried = IntVar()
fried = Checkbutton(labelframe, text ='ทอด',variable=var_fried, takefocus = 0)
fried.grid(row=3, column=1,padx=5, pady=5,sticky=W)


# Input ---------------------------------------------------------------------------------------------------
Ingredient_Input_label = Label(labelframe, text="Input Ingredient",font='Helvetica 10 bold')
Ingredient_Input_label.grid(row=0, column=3,padx=5, pady=5,sticky=W)
Entry_Ingredient = Entry(labelframe)
Entry_Ingredient.grid(row=0, column=4,padx=5, pady=5)

Ingredient_Input_label = Label(labelframe, text="Ingredient",font='Helvetica 10 bold')
Ingredient_Input_label.grid(row=1, column=3,padx=5, pady=5,sticky=W)
# Input ---------------------------------------------------------------------------------------------------

Button_Ingredient = Button(labelframe, text ="Input",command = append_ingredient, bg='#ffb3fe')
Button_Ingredient.grid(row=0, column=5,padx=5, pady=5)

Button_Delete_Ingredient = Button(labelframe, text ="Delete",command = delete, bg='#ffb3fe')
Button_Delete_Ingredient.grid(row=1, column=5,padx=5, pady=5)

# Button_Delete_Ingredient = Button(root, text ="Let Go!",command = type_food)
# Button_Delete_Ingredient.pack(fill="both", expand="yes",padx=5, pady=5)




Ingredient_list = Listbox(labelframe)



Ingredient_list.grid(row=1, column=4,padx=5, pady=5,rowspan = 6)

# pt = Table(labelframe3,dataframe=find_menu(Type_Food_list,Indredient_input_list),showtoolbar=False, showstatusbar=False)
# pt.show()
# pt.redraw()




root.mainloop()