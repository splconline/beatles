import requests, bs4

# Open the URL
exfile = requests.get("https://en.wikipedia.org/wiki/The_Beatles_discography")
exfile.raise_for_status()

# Soup it
exsoup = bs4.BeautifulSoup(exfile.text,'html.parser')

# Find the *first* album listing table (which will be the UK albums)
albums = exsoup.find("table", {"class": "wikitable plainrowheaders"})

# Extract the data
data = []
for row in albums.find_all('tr'):
    row_data = []
    for cell in row.contents:
        row_data.append(cell.text)
    data.append(row_data)

dataLength = len(data)
print('Table length:' + str(dataLength))

print('First element:')
print(data[0])

print('Second element:')
print(data[1])

print('Third element:')
print(data[2])

print('Penultimate element:')
print(data[dataLength-2])

print('Last element:')
print(data[dataLength-1])

print('Third Element, Second Index:')
print(data[2][1])

print('Fourth Element, Second Index:')
print(data[3][1])

print('Fifth Element, Second Index:')
print(data[4][1])

