import sqlite3

conn = sqlite3.connect('honeypot.db')
print('Recent attacks:')
for row in conn.execute('SELECT timestamp, ip_address, username, password FROM attacks ORDER BY timestamp DESC LIMIT 5'):
    print(row)
conn.close()