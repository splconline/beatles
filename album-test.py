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

# TODO function call

"""
# Initialise (OUTSIDE LOOP)
   result = []

# get the tracks in an album
   tracks = retrieve_tracks(wikiURL,album_name, album_date)

# add tracks to result
   for track in tracks:
       add track to result

def retrieve_tracks(url,name,date):
    goto wikipedia.org/url and retrieve the soup
    tracklist = []
    side = A
    last track number = 0
    for each track in the soup:
        track = []
        if track number > last track number side = B
        to track add: side, track number, track title, album_name, album_date, ""
        add track to tracklist
        last track number = track number
    return tracklist
"""
