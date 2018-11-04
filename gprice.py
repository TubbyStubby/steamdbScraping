import os
f = open("top100_players_steamdb.csv","r",encoding='utf-8')
appids = f.read()
f.close()

appids = appids.split('\n')
del appids[0]
for i in range(len(appids)):
	appids[i] = appids[i].split(',')
	appids[i] = appids[i][0]

for j in appids:
	mypath = 'c:/projects/bs4/csvprice/'+j+'/'
	if os.path.exists(mypath):
		f=open(mypath+'eus.csv','r')
		s=f.read()
		f.close()
		s=s.split('\n')[:-1]
		print(j)
		col1=[]
		col0=[]
		for i in range(len(s)):
			s[i] = s[i].split(',')
			col1.append(float(s[i][1]))
			col0.append(s[i][0])
		f=open('c:/projects/bs4/csvgdata/'+j+'_data.csv','r')
		gs = f.read()
		f.close()
		gs=gs.split('\n')[:-1]
		gs[0]=gs[0]+',Price,Discount'
		gs[1]=gs[1].split(',')
		gs[1].append(str(max(col1)))
		gs[1].append('0')
		k=-1
		for i in range(2,len(gs)):
			gs[i]=gs[i].split(',')
			if gs[i][0] not in col0:
				gs[i].append(gs[i-1][2])
				gs[i].append(gs[i-1][3])
			else:
				k+=1
				gs[i].append(s[k][1])
				gs[i].append(s[k][2])
		for i in range(1,len(gs)):
			gs[i]=','.join(gs[i])
		gs='\n'.join(gs)
		f=open('c:/projects/bs4/gprice/'+j+'.csv','w')
		f.write(gs)
		f.close()