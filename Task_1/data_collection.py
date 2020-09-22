from bs4 import BeautifulSoup
import sqlite3

html = open('UEEX.html').read()
soup = BeautifulSoup(html, "html.parser")
div_value = soup.find_all('div', class_='value')
list_data = [item.contents[0].strip() for item in div_value[:95]]
del list_data[12], list_data[30], list_data[48], list_data[66], list_data[84]
main_data = [tuple(list_data[i:i+18]) for i in range(0, len(list_data), 18)]

conn = sqlite3.connect('dtrading')
cur = conn.cursor()
sql_statement = 'INSERT INTO Energy VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
cur.executemany(sql_statement, main_data)
conn.commit()
