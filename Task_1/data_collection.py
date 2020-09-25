from bs4 import BeautifulSoup
import sqlite3

html = open('UEEX.html').read()
soup = BeautifulSoup(html, "html.parser")
div_value = soup.find_all('div', class_='value')
list_data = [item.contents[0].strip() for item in div_value[:95]]
# In the previous version I used del to quickly remove duplicates '1 500.00' in list
# del list_data[12], list_data[30], list_data[48], list_data[66], list_data[84]
# Of course I know better way ... Sorry)
new_list_data = [j for i, j in enumerate(list_data) if i not in [12, 31, 50, 69, 88]]
main_data = [tuple(new_list_data[i:i + 18]) for i in range(0, len(new_list_data), 18)]

conn = sqlite3.connect('dtrading')
cur = conn.cursor()
sql_statement = 'INSERT INTO Energy VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
cur.executemany(sql_statement, main_data)
conn.commit()

# More simple example with requests (I didn't notice him)
# If carefully use developer tools, we can find better link. I'll show you the main idea.
# import requests
#
# url = 'https://epbets.ueex.com.ua/public/PublicHandler.ashx?CommandName=jPositions&id_auc=3294127&info=Y&lan=ua&fl_FullNumber=&fl_Direction=&fl_Owner=&fl_Goods=&fl_DeliveryType=&empty_filter=Y'
# r = requests.get(url).json()
# for item in r.get('rows'):
#     print(item)


