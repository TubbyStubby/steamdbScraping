import urllib.request
from bs4 import BeautifulSoup as soup
import os

f = open("top100_players_steamdb.csv","r",encoding='utf-8')
appids = f.read()
f.close()

appids = appids.split('\n')
del appids[0]
for i in range(len(appids)):
	appids[i] = appids[i].split(',')
	appids[i] = appids[i][0]

j=0
for i in appids:
	print(j,i)
	j+=1
	myurl="https://steamdb.info/app/"+i
	#print(myurl)
	req = urllib.request.Request(myurl, headers={'User-Agent':'Magic Browser'})
	con = urllib.request.urlopen(req)
	page_raw = con.read()
	con.close()

	page_soup = soup(page_raw,"html.parser")

	chk = page_soup.findAll('td',class_='price-line')
	if len(chk)!=0:
		l = []
		pth = "c:/projects/bs4/price/"+i
		if not os.path.exists(pth):
			os.makedirs(pth)
		for cc in chk:
			myurl="https://steamdb.info/api/GetPriceHistory/?appid="+i+"&cc="+cc['data-cc']
			#print(myurl)
			req = urllib.request.Request(myurl, headers={'User-Agent':'Magic Browser'})
			con = urllib.request.urlopen(req)
			pdata_page = con.read()
			con.close()

			price_soup = soup(pdata_page,'html.parser')

			f=open(pth+'/'+cc['data-cc']+'.txt','w')
			f.write(price_soup.text)
			f.close()