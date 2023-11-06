import requests, bs4

# e.g. https://en.wikipedia.org/wiki/A_Hard_Day's_Night_(album)
# All track listings are in a table class 'tracklist', so find these
# then extract contents


# Define a function that returns the required data, given the URL & album name
def get_tracks(url,album):

# Open the URL
    exfile = requests.get(url)
    exfile.raise_for_status()

# Soup it
    exsoup = bs4.BeautifulSoup(exfile.text,'html.parser')

# Find the track listing tables
    tablesides = exsoup.find_all("table", {"class": "tracklist"})

# Extract the data from the first two sides (problem for White Album
# with 4 x sides, will sort this out later)
    data = []

    side = 'A'
    rows = tablesides[0].find_all('tr')
# Loop through all rows except the first and last ones
    for i in range(1,len(rows)-1):
        row_data = []
        for cell in rows[i].contents:
            row_data.append(cell.text)
        row_data.append(album)
        row_data.append(side)
        data.append(row_data)
    

    side = 'B'
    rows = tablesides[1].find_all('tr')
# Loop through all rows except the first and last ones
    for i in range(1,len(rows)-1):
        row_data = []
        for cell in rows[i].contents:
            row_data.append(cell.text)
        row_data.append(album)
        row_data.append(side)
        data.append(row_data)

    return data
# END def get_tracks

# BEGIN main
test = get_tracks("https://en.wikipedia.org/wiki/A_Hard_Day's_Night_(album)", "A Hard Day's Night")
print(test)
exit()

