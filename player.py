# from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def comma_rem(str):
	str2=""
	j=0;
	for i in str:
		if i == ',':
			pass
			#str2+=' '
		else:
			str2+=str[j]
		j+=1
	return str2

myurl="C:\\Projects\\BS4\\concurrentplayers.html"

# uClient = uReq(myurl)
# page_raw = uClient.read()
# uClient.close()

page_soup = soup(open(myurl,encoding='utf-8'),"html.parser")

rows = page_soup.findAll("tr",class_="app")

f = open("top100_players_steamdb.csv","w",encoding='utf-8')
header = "AppID, Name, Current, 24H Peak, All Time \n"
print(rows[1])

f.write(header)

for i in range(1,101):
	s = ""
	t=rows[i].text.split('\n')
	print(t)
	for j in range(2,len(t)-1):
		s=s+comma_rem(t[j])+','
	s=s+'\n'
	f.write(s)
f.close()