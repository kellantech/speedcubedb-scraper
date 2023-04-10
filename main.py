import requests 
from bs4 import BeautifulSoup as soup
import json,os

URL = "https://speedcubedb.com/a/Megaminx/MegaminxCP" # url of the page


data = requests.get(URL).text


main = soup(data,'html.parser')
cont = main.find_all(class_='container-fluid')[2]


c2 = cont.find_all('li')
h3 = cont.find_all('h3')

h3 = [i.text for i in h3]


res = []
cs = []
offset = 0 # play around with this until it works :) (start small)
nalg = 1 # number of algs shown on page


for ind in range(offset,len(c2),4):
  #print(c2[ind])
  res.append(c2[ind].find('div').text)


out = []


for n in range(0,len(res),nalg):
  out.append({"name":h3[n//nalg],"algs":res[n:n+nalg]})

with open('out.json','w') as f:
  json.dump(out,f)  


os.system('python3 -m json.tool out.json')
