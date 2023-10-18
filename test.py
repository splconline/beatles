import bs4

#

exfile = open('beatles-track-listing.html')
exsoup = bs4.BeautifulSoup(exfile,'html.parser')
print(type(exsoup))
#print(exsoup.prettify())

# This finds the div that has the track-listing
#sides = exsoup.find_all("div", {"class": "track-listing"})
#print(sides[0].prettify())
#print(sides[1].prettify())

# Whereas this finds the two tables (for each side) that has tracklist
tablesides = exsoup.find_all("table", {"class": "tracklist"})
print(type(tablesides))

#print(tablesides[0].prettify())
#print(tablesides[1].prettify())

data = []
for row in tablesides[0].find_all('tr'):
    row_data = []

#   for cell in row.find_all('td'):

    for cell in row.contents:
        row_data.append(cell.text)
    data.append(row_data)

print(data)
