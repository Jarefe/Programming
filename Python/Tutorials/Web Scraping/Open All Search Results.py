import requests, sys, webbrowser, bs4


search = "python projects"
print('Searching...')
res = requests.get('https://google.com/search?q=' + search)
res.raise_for_status()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open browser tab for each result
linkElems = soup.select('a.result__a')

numOpen = min(5,len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://google.com/search?q=' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)