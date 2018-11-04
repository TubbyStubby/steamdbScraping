import urllib.request
from bs4 import BeautifulSoup as soup

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
	myurl="https://steamdb.info/api/GetGraph/?type=concurrent_max&appid="+i
	#print(myurl)
	req = urllib.request.Request(myurl, headers={'User-Agent':'Magic Browser'})
	con = urllib.request.urlopen(req)
	page_raw = con.read()
	con.close()

	page_soup = soup(page_raw,"html.parser")
	
	f = open(i+"_gdata.txt","w",encoding='utf-8')
	f.write(page_soup.text)
	f.close()