from bs4 import BeautifulSoup
import requests

url="https://ark.fandom.com/wiki/Explorer_Notes/Locations"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

# wikitable sortable mw-collapsible mw-made-collapsible jquery-tablesorter
# mw-headline

first_table = soup.find("table", attrs={"class": "wikitable"})
first_table_data = first_table.tbody.find_all("tr")

data = []

for row in first_table_data:
    row_data  = []

    for td in row.find_all("td"):
        row_data.append(td.text.replace('\n', ' ').strip())
    
    data.append(row_data)

table_heading_element = soup.find("h4")
table_title = table_heading_element.find("span", attrs={"class": "mw-headline"})
table_title_text = table_title.text.replace('\n', ' ').strip()

print(table_title_text)

file_name = 'ark_tables_textfile.txt'

with open(file_name, 'w') as f:
    f.write(f'{table_title_text}\n\n')
    f.write('[\n')
    for data_row in data:
        if len(data_row) > 0:
            f.write(f'["{data_row[2]}", "{data_row[1]}", {data_row[3]}, {data_row[4]}, "{data_row[5]}"],')
            f.write('\n')
    f.write(']\n')
