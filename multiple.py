from bs4 import BeautifulSoup
import requests

url="https://ark.fandom.com/wiki/Explorer_Notes/Locations"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

# wikitable sortable mw-collapsible mw-made-collapsible jquery-tablesorter
# mw-headline

all_tables = soup.find_all("table", attrs={"class": "wikitable"})
all_tables = all_tables[:-3 or None]

#mobile = all_tables.pop()

row_index = 0

for table in all_tables:
    guid_data = (row_index + 1) * 1000
    single_table_data = table.tbody.find_all("tr")

    data = []

    for row in single_table_data:
        row_data  = []

        for td in row.find_all("td"):
            # print(td)
            row_data.append(td.text.replace('\n', ' ').strip())
        
        data.append(row_data)

    table_heading_element = soup.find_all("h4")

    single_table_title = table_heading_element[row_index].find("span", attrs={"class": "mw-headline"})
    single_table_title_text = single_table_title.text.replace('\n', ' ').strip()

    print(single_table_title_text)
    #print(data[0])
    #print(data)

    file_name = 'ark_tables_textfile-' + str(single_table_title_text.replace(" ", "")) + '.js'

    with open(file_name, 'w') as f:
        #f.write(f'{single_table_title_text}\n\n')
        f.write(f'export const data = \n')
        f.write('[\n')
        guid_single_id = 0
        for data_row in data:
            if len(data_row) > 1:
                guid = guid_data + guid_single_id
                print(guid)
                data_object = "{ id: " + str(guid) + ", name: '" + data_row[2] + "', note: '" + data_row[1] + "', lat: " + data_row[3] + ", lon: " + data_row[4] + ", location: \"" + data_row[5] + "\" },"
                f.write(data_object + '\n')
                guid_single_id = guid_single_id + 1

        f.write('];\n')
    
    row_index = row_index + 1
