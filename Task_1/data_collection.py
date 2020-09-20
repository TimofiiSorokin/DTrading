from bs4 import BeautifulSoup
import sqlite3

html = open('UEEX.html').read()
soup = BeautifulSoup(html, "html.parser")
div_value = soup.find_all('div', class_='value')
table_data = [item.contents[0].strip() for item in div_value[:95]]
del table_data[12], table_data[30], table_data[48], table_data[66], table_data[84]
rrr = [tuple(table_data[i:i+18]) for i in range(0, len(table_data), 18)]

conn = sqlite3.connect('dtrading')
cur = conn.cursor()
sql_statement = 'INSERT INTO Energy VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
cur.executemany(sql_statement, rrr)
conn.commit()
