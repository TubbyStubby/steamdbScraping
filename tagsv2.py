import urllib.request
from bs4 import BeautifulSoup as soup
import re

f = open("top100_players_steamdb.csv","r",encoding='utf-8')
appids = f.read()
f.close()

appids = appids.split('\n')
del appids[0]
for i in range(len(appids)):
	appids[i] = appids[i].split(',')
	appids[i] = appids[i][0]

f = open("top100_tagsv2_steamdb.csv","w",encoding='utf-8')

j=0
for i in appids:
	print(j,i)
	j+=1
	myurl="https://steamdb.info/app/"+i+"/info/"
	#print(myurl)
	req = urllib.request.Request(myurl, headers={'User-Agent':'Magic Browser'})
	con = urllib.request.urlopen(req)
	page_raw = con.read()
	con.close()

	page_soup = soup(page_raw,"html.parser")

	s = str(i)
	try:
		for itms in page_soup(text = re.compile('store_tags'))[0].parent.parent.find_all('a'):
			s = s + ',' + itms.text
	except:
		print('no')
		s=s+',No Tags'
	s+='\n'
	f.write(s)

f.close()