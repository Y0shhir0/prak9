import csv
import sqlite3

con = sqlite3.connect('WBb3.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Client(
    id integer primary key autoincrement,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS  Postavshik(
    id integer primary key autoincrement,
    Number integer,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Tovar(
    id integer primary key autoincrement,
    Name text,
    idPostavshik integer references Postavshik(id),
    count integer,
    idClient integer references Client(id)
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS  Rabotnik(
    id integer primary key autoincrement,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS  Postavki(
    id integer primary key autoincrement,
    datetim text,
    idPostavshik integer references Postavshik(id),
    idTovar integer references Tovar(id),
    count integer,
    idRabotnik integer references Rabotnik(id)
    )
    ''')



# with open('client.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['f'] and row['i'] and row['o']:
#             cur.execute("INSERT INTO Client(f, i, o) VALUES (?, ?, ?)", (row['f'], row['i'], row['o']))
#
# with open('Postavshik.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['Number'] and row['f'] and row['i'] and row['o']:
#             cur.execute("INSERT INTO Postavshik(Number,f, i, o) VALUES (?,?, ?, ?)", (row['Number'],row['f'], row['i'], row['o']))
#
# with open('Tovar.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['Name'] and row['idPostavshik'] and row['count'] and row['idClient']:
#             cur.execute("INSERT INTO Tovar(Name,idPostavshik,count,idClient) VALUES (?,?, ?, ?)", (row['Name'],row['idPostavshik'], row['count'], row['idClient']))
#
#
# with open('Rabotnik.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['f'] and row['i'] and row['o']:
#             cur.execute("INSERT INTO Rabotnik(f, i, o) VALUES (?, ?, ?)", (row['f'], row['i'], row['o']))
#
# with open('Postavki.csv', 'r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row['datetim'] and row['idPostavshik'] and row['idTovar'] and row['count'] and row['idRabotnik']:
#             cur.execute("INSERT INTO Postavki(datetim, idPostavshik, idTovar, count, idRabotnik) VALUES (?, ?, ?, ?, ?)", (row['datetim'], row['idPostavshik'], row['idTovar'], row['count'], row['idRabotnik']))
# con.commit()
#


cur.execute("select * from Postavki")
records = cur.fetchall()
print(records)
cur.execute("select * from Rabotnik")
records = cur.fetchall()
print(records)
cur.execute("select * from Tovar")
records = cur.fetchall()
print(records)
cur.execute("select * from Postavshik")
records = cur.fetchall()
print(records)
cur.execute("select * from client")
records = cur.fetchall()
print(records)


cur.execute('''select * from Client''')
with open ("C:/Users/Denis/Desktop/out/outClient.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(cur)

cur.execute('''select * from Postavshik''')
with open("C:/Users/Denis/Desktop/out/outPostavshik.csv", 'w', newline='') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
     csv_writer.writerow([i[0] for i in cur.description])
     csv_writer.writerows(cur)


cur.execute('''select * from Tovar''')
with open("C:/Users/Denis/Desktop/out/outTovar.csv", 'w', newline='') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
     csv_writer.writerow([i[0] for i in cur.description])
     csv_writer.writerows(cur)


cur.execute('''select * from Rabotnik''')
with open("C:/Users/Denis/Desktop/out/outRabotnik.csv", 'w', newline='') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
     csv_writer.writerow([i[0] for i in cur.description])
     csv_writer.writerows(cur)

cur.execute('''select * from Postavki''')
with open("C:/Users/Denis/Desktop/out/outPostavki.csv", 'w', newline='') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=",", lineterminator='\r')
     csv_writer.writerow([i[0] for i in cur.description])
     csv_writer.writerows(cur)


con.commit()
con.close()