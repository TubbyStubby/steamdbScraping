import os,time,calendar
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
		f=open(mypath+'us.csv','r')
		s=f.read()
		f.close()
		s=s.split('\n')[:-1]
		print(mypath)
		for i in range(len(s)):
			s[i]=s[i].split(',')
			#print(s[i])
			#break
			myet = s[i][0][:10]+'.'+s[i][0][10:]
			myet = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(float(myet)))
			myt = myet[:-8]+'00:00:00'
			tt = time.strptime(myt,'%Y-%m-%d %H:%M:%S')
			te = calendar.timegm(tt)
			s[i][0] = str(te)
			ts=''
			for k in s[i]:
				ts=ts+','+k
			ts=ts[1:]+'\n'
			s[i]=ts
		#break
		ts=''
		for i in s:
			ts=ts+i
		f=open(mypath+'eus.csv','w')
		f.write(ts)
		f.close()
