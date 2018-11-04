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

'''myurl="Https://store.steampowered.com/app/578080/"
#print(myurl)
req = urllib.request.Request(myurl, headers={'User-Agent':'Magic Browser'})
con = urllib.request.urlopen(req)
page_raw = con.read()
con.close()

page_soup = soup(page_raw,"html.parser")

tags = page_soup.find_all('div', class_='popular_tags')

for i in tags:
	l=i.text.split()'''

f = open("top100_tags_steamdb.csv","w",encoding='utf-8')

cn=0
for i in appids:
	s = i+': '
	print(cn)
	cn+=1
	myurl="Https://store.steampowered.com/app/"+i+"/"
	#print(myurl)
	req = urllib.request.Request(myurl, headers={'User-Agent':'Magic Browser'})
	con = urllib.request.urlopen(req)
	page_raw = con.read()
	con.close()

	page_soup = soup(page_raw,"html.parser")

	tags = page_soup.find_all('div', class_='popular_tags')

	for i in tags:
		l=i.text.split()
		if len(l)>0:
			for j in l:
				if j.isalpha():
					s = s + ',' + j
	s+='\n'
	f.write(s)

f.close()