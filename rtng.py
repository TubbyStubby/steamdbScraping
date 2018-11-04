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

f = open("top100_rating_steamdb.csv","w",encoding='utf-8')
header = "AppID, Total, Positive \n"
f.write(header)

j=0
for i in appids:
	print(j,i)
	j+=1
	myurl="https://steamdb.info/app/"+i+"/graphs/"
	#print(myurl)
	req = urllib.request.Request(myurl, headers={'User-Agent':'Magic Browser'})
	con = urllib.request.urlopen(req)
	page_raw = con.read()
	con.close()

	page_soup = soup(page_raw,"html.parser")
	
	try:
		total = page_soup.find('meta', {'itemprop':'reviewCount'})['content']
		rating = page_soup.find('meta', {'itemprop':'ratingValue'})['content']
	except TypeError:
		try:
			print('e')
			good = page_soup.find('span', class_='header-thing-good').text
			poor = page_soup.find('span', class_='header-thing-poor').text
			total = int(good)+int(poor)
			rating = float(good)/total
		except:
			total='N/A'
			rating='N/A'

	f.write(i+','+str(total)+','+str(rating)+'\n')

f.close()