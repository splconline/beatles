table = soup.find('table', {'id': 'my_table'})

data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text)
    data.append(row_data)

# https://www.educative.io/answers/beautiful-soup-select

# https://saturncloud.io/blog/how-to-scrape-an-html-table-with-beautiful-soup-into-pandas/
