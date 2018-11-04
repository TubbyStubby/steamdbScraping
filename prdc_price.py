import os,ast
f = open("top100_players_steamdb.csv","r",encoding='utf-8')
appids = f.read()
f.close()

appids = appids.split('\n')
del appids[0]
for i in range(len(appids)):
	appids[i] = appids[i].split(',')
	appids[i] = appids[i][0]

for i in appids:
	mypath = 'c:/projects/bs4/eprice/'+i+'/'
	if os.path.exists(mypath):
		l = os.listdir(mypath)
		for j in l:
			f=open(mypath+j,'r')
			s=f.read()
			f.close()
			d = ast.literal_eval(s)
			new = 'c:/projects/bs4/csvprice/'+i+'/'
			if not os.path.exists(new):
				os.makedirs(new)
			f=open(new+j[:-3]+'csv','w')
			s2=''
			for a in d['final']:
				s2 = str(a[0])+','+str(a[1])+','+str(d['formatted'][str(a[0])]['discount'])+'\n'
				f.write(s2)
			f.close()
