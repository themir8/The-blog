import requests
from bs4 import BeautifulSoup as BS

max_page = 10
pages = []

for x in range(1, max_page + 1):
	pages.append(requests.get("https://www.texnoman.uz/sahifa/" + str(x)))

for r in pages:
	soup = BS(r.content, 'html.parser')

	#######
	
	    # print(title[0].text)

	with open('text.txt', 'w') as filehandle:
	  	for el in soup.select('.postBlock'):
	  		title = el.select("a")
	  		filehandle.write(title[0].text)
	#######