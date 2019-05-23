import requests
from bs4 import BeautifulSoup
matches = []
matchcodes=[]
for val in range(1971,1972):
	G=str(val)+'0101'+str(val)+'1231'
	page = requests.get("http://howstat.com/cricket/Statistics/Matches/MatchList.asp?Group="+str(G)+"&Range="+str(val))
	soup = BeautifulSoup(page.text, 'html.parser')
	j=soup.find_all('a',attrs={'class':'LinkNormal'})
	for i in j:
		links='http://howstat.com/cricket/Statistics/Matches/'+i.get('href')
		matches.append(links)
	for i in range(1,len(matches),2):
		matchcodes.append(matches[i])
