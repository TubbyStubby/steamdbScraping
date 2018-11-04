f = open("top100_players_steamdb.csv","r",encoding='utf-8')
appids = f.read()
f.close()

appids = appids.split('\n')
del appids[0]
for i in range(len(appids)):
	appids[i] = appids[i].split(',')
	appids[i] = appids[i][0]

for i in appids:
	f=open(i+"_gdata.txt",'r')
	s=f.read()
	f.close()
	f=open('egdata/'+i+"_gdata_edit.txt",'w')
	f.write('{'+s[24:-2]+'}')
	f.close()