import csv
import mysql.connector

datuBaze = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "123456",
    database = "datubaze1",
    charset = "utf8mb4"
)
print(datuBaze)

kursors = datuBaze.cursor()

kursors.execute("CREATE TABLE IF NOT EXISTS csv(Vārds VARCHAR(255), Uzvārds VARCHAR(255), Pilsēta VARCHAR(255))")
"""
with open("Datubazes_dati.csv", "r", newline="", encoding="utf-8") as dati:
    saturs = csv.reader(dati)
    next(saturs) # izlaiž lasīšanā pirmo rindu
    for rinda in saturs:
        vards, uzvards, pilseta = rinda

        kursors.execute("INSERT INTO csv (Vārds, Uzvārds, Pilsēta) VALUES (%s, %s, %s)", (vards,uzvards,pilseta))
datuBaze.commit()
dati.close()
"""
pilsetasMeklesana = input("Ievadiet pilsētu pēc kuras meklēt (Rīga, Jelgava): ")
kursors.execute("SELECT * FROM csv WHERE Pilsēta = %s", (pilsetasMeklesana,))
rezultati = kursors.fetchall()
for i in rezultati:
    print(*i)
