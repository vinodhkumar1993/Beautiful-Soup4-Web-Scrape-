import urllib.request
import re
from bs4 import BeautifulSoup
import pandas as pd
name=[]
street=[]
locali=[]
zp_code=[]
phone=[]
url='https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA'
content=urllib.request.urlopen(url)
wholepage=content.read().decode('utf-8')
#print (wholepage)
soup=BeautifulSoup(wholepage,'html.parser')
#print(soup)
data=soup.find_all('a',{'class':'business-name'})
addr=soup.find_all('span',{'class':'street-address'})
zip=soup.find_all('span',{'itemprop':'postalCode'})
number=soup.find_all('div',{'class':'phones phone primary'})
#print(number)
#print(zip)
#print (addr)
local=soup.find_all('span',{'class':'locality'})
#print (local)

#print(data)
for i in data:
    for item in i:
        app=item.text
        name.append(app)
#print(name)
#print('\n')
        
for each in addr:
    for every in each:
        #print (every)
        street.append(every)
#print(street)  
#print('\n')
#
for loc in local:
    #print (loc)
    for loc1 in loc:
        (locali.append(loc1))
#        locali.append(loc1)
#print (locali)
for code in zip:
    zp_code.append(code.text)
#print (zp_code)
for num in number:
    phone.append(num.text)
#print(phone)
df=pd.DataFrame(name,columns=['Store Name'])
df['Street Address']=pd.DataFrame(street)
df['Locality']=pd.DataFrame(locali)
df['Zip Code']=pd.DataFrame(zp_code)
df['Phone Number']=pd.DataFrame(phone)
df.to_csv('scrape.csv',index=False)
#print (df)        
