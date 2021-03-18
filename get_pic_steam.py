from bs4 import BeautifulSoup
import requests
import pandas as pd 
import urllib.request

url = requests.get("https://nlovecooking.com/%e0%b8%9b%e0%b8%a3%e0%b8%b0%e0%b9%80%e0%b8%a0%e0%b8%97%e0%b8%ad%e0%b8%b2%e0%b8%ab%e0%b8%b2%e0%b8%a3/%e0%b8%aa%e0%b8%b9%e0%b8%95%e0%b8%a3%e0%b8%ad%e0%b8%b2%e0%b8%ab%e0%b8%b2%e0%b8%a3%e0%b8%9b%e0%b8%a3%e0%b8%b0%e0%b9%80%e0%b8%a0%e0%b8%97%e0%b8%99%e0%b8%b6%e0%b9%88%e0%b8%87/")
htmltext = BeautifulSoup(url.text,'html.parser')

# print(htmltext)

web_recipe= htmltext.findAll ('td', limit=None)
# print(web_recipe)
# print(len(web_recipe))
countcolumn = []
total_web = []
total_name =[]

for menu in web_recipe:
  all_web = menu.findAll ('a', limit=None)
  # print(all_web)
  # print(len(all_web))
  for index_all_web in range(len(all_web)):
    if index_all_web == len(all_web) -1 :
      pre_web = str(all_web[index_all_web])
      # count +=1
      # print(pre_web)
      all_web_split = pre_web.split('"')
      # print(all_web_split)
      # print(len(all_web_split))
      for web in range(len(all_web_split)):
        if web == 1:
          # print(all_web_split[web])
          total_web.append(all_web_split[web])
        elif web == len(all_web_split)-1:
          all_name = str(all_web_split[web])
          # print(all_name)
          all_name_split = all_name.split('>')
          for name in range(len(all_name_split)):
            if name ==1 :
              all_name_split_1 = str(all_name_split[name])
              name_split = all_name_split_1.split('<')
              # print(name_split)
              for index_real_name in range(len(name_split)):
                if index_real_name == 0:
       
                  total_name.append(name_split[index_real_name])
                  # print(name_split[index_real_name])


print(total_web) 
print(len(total_web))
print(total_name)   
print(len(total_name)) 


for url_name,name_f in zip(total_web,total_name):
    url = requests.get(url_name)
    htmltext_pic = BeautifulSoup(url.text,'html.parser')

    # print(htmltext)

    web_recipe_pic= htmltext_pic.findAll ('img')

    list_pic_f = str(web_recipe_pic[2])
    print(list_pic_f) 
    if 'jpg' in list_pic_f:
        index_html = list_pic_f.find('https')
        index_jpg = list_pic_f.find('jpg')
        url_pic = list_pic_f[index_html:index_jpg+3]

        filename = f'{name_f}.jpg'
        image_url = url_pic
        urllib.request.urlretrieve(image_url, filename)
    elif 'png' in list_pic_f:
        index_html = list_pic_f.find('https')
        index_jpg = list_pic_f.find('png')
        url_pic = list_pic_f[index_html:index_jpg+3]

        filename = f'{name_f}.jpg'
        image_url = url_pic
        urllib.request.urlretrieve(image_url, filename)
   






