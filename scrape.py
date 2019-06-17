import requests
import time
import json
data = {'data':[]}
for i in range(1,10001):
	url = 'http://api.stackexchange.com/2.2/questions?page='+str(i)+'&pagesize=100&sort=votes&site=stackoverflow'
	r = requests.get(url)
	if((i%100)==0):
		with open("ibm_data"+str(i)+".json",'a') as file1:
			json.dump(data,file1)
			print("Saved till",str(i),"pages in file")
			data['data']=[]
	if(r.status_code<=200):
		a = r.json()
		if('items' in a):
			data['data'].extend(a['items'])
			print("Page",(i)*100,"Done")
	else:
		if(r.status_code==502):
			print(r.json())
			print("Sleeping for 5 mins and restarting")
			time.sleep(300)

print("Code",r.status_code,"exit at page",i)