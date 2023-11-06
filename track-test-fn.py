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

# How many sides?
    print("Sides:", len(tablesides))

# Extract the data
    data = []
    for row in tablesides[1].find_all('tr'):
        row_data = []
        for cell in row.contents:
            row_data.append(cell.text)
        row_data.append(album)
        data.append(row_data)
    return data

test = get_tracks("https://en.wikipedia.org/wiki/A_Hard_Day's_Night_(album)", "A Hard Day's Night")
print(test)
exit()

