import requests, bs4

# e.g. https://en.wikipedia.org/wiki/A_Hard_Day's_Night_(album)
# All track listings are in a table class 'tracklist', so find these
# then extract contents

# Open the URL
exfile = requests.get("https://en.wikipedia.org/wiki/A_Hard_Day's_Night_(album)")
exfile.raise_for_status()

# Soup it
exsoup = bs4.BeautifulSoup(exfile.text,'html.parser')

# Find the track listing tables
tablesides = exsoup.find_all("table", {"class": "tracklist"})

# Extract the data
data = []
for row in tablesides[0].find_all('tr'):
    row_data = []
    for cell in row.contents:
        row_data.append(cell.text)
    data.append(row_data)

print(data)
