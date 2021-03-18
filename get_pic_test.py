from bs4 import BeautifulSoup
import requests
import pandas as pd 
url = requests.get("""https://nlovecooking.com/%e0%b8%a2%e0%b8%b3-%e0%b8%aa%e0%b8%95%e0%b8%ad%e0%b9%80%e0%b8%9a%e0%b8%ad%e0%b8%a3%e0%b8%a3%e0%b8%b5%e0%b9%88-%e0%b8%81%e0%b8%b8%e0%b9%89%e0%b8%87%e0%b8%aa%e0%b8%94/""")
htmltext_pic = BeautifulSoup(url.text,'html.parser')

# print(htmltext)

web_recipe_pic= htmltext_pic.findAll ('img')

list_pic_f = str(web_recipe_pic[2])
print(list_pic_f) 
index_html = list_pic_f.find('https')
index_jpg = list_pic_f.find('jpg')
print(list_pic_f[index_html:index_jpg+3])