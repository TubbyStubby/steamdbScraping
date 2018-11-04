import os
f = open("top100_players_steamdb.csv","r",encoding='utf-8')
appids = f.read()
f.close()

appids = appids.split('\n')
del appids[0]
for i in range(len(appids)):
	appids[i] = appids[i].split(',')
	appids[i] = appids[i][0]

for i in appids:
	mypath = 'c:/projects/bs4/price/'+i+'/'
	if os.path.exists(mypath):
		l = os.listdir(mypath)
		for j in l:
			f=open(mypath+j,'r')
			s=f.read()
			f.close()
			new = 'c:/projects/bs4/eprice/'+i+'/'
			if not os.path.exists(new):
				os.makedirs(new)
			f=open(new+j,'w')
			f.write('{'+s[24:-2]+'}')
			f.close()