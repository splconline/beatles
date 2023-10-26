import requests, bs4

# Open the URL
# (Tested on Beatles, Queen, Miles Davis (Columbia only))
exfile = requests.get("https://en.wikipedia.org/wiki/The_Beatles_discography")
exfile.raise_for_status()

# Soup it
exsoup = bs4.BeautifulSoup(exfile.text,'html.parser')

# Find the *first* album listing table (which e.g. for the Beatles wikipedia page will
# be the UK albums, for Miles Davis will be the Columbia albums etc.)
albums = exsoup.find("table", {"class": "wikitable plainrowheaders"})

# Extracting the data we found that for class 'wikitable plainrowheaders' in an artist page:
#
# * Listing elements 1,2,3, n-1 and n shows that album names are in element 3 to n-1
# * The lbum title is in the second index
#
# Therefore, the following gets the URLs of all albums:

rows = albums.find_all('tr')
n = len(rows)

for i in range(2, n-1, 1):
    url = rows[i].find('a', href=True)
    print(url['href'])
