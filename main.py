import requests 
from bs4 import BeautifulSoup as soup
import json,os


URL = input("url of page: ") or 'https://speedcubedb.com/a/3x3/WV'
algn = int(input("how many algs? "))+1

data = requests.get(URL).text


main = soup(data,'html.parser')
cont = main.find_all(class_='container-fluid')[2]


c2 = cont.find_all('li')
h3 = cont.find_all('h3')

h3 = [i.text for i in h3]


res = []
cs = []
offset = 0




for ind in range(offset,algn+offset*4):
      res.append(cont.find_all('div',class_='col')[ind].select('li:not(.me-2)',class_='list-group-item')[0].text.split('\n')[1].split("\n")[0])
      
  
#print(len(res))
#print(h3)
#print(res)
out = []
#print(dict(zip(h3,res)))
x = dict(zip(h3,res[1:]))

ou2 = [{"name":k,"algs":[v]} for k,v in x.items()]



with open('out.json','w') as f:
  json.dump(ou2,f)  


os.system('python3 -m json.tool out.json')
