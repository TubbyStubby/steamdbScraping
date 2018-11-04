import ast
f = open("top100_players_steamdb.csv","r",encoding='utf-8')
appids = f.read()
f.close()

appids = appids.split('\n')
del appids[0]
for i in range(len(appids)):
	appids[i] = appids[i].split(',')
	appids[i] = appids[i][0]

for i in appids:
	f=open('egdata/'+i+'_gdata_edit.txt','r')
	s=f.read()
	f.close()
	f=open('csvgdata/'+i+'_data.csv','w')
	f.write('X'+i+',Y'+i+'\n')
	d = ast.literal_eval(s)
	start = int(d["start"])
	step = int(d["step"])
	val = d["values"]
	se = ''
	for i in range(len(val)):
		se += (str(start+step*i) +','+ str(val[i])+'\n')
	f.write(se)
	f.close()