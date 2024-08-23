import mysql.connector

datuBaze = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "123456",
    database = "datubaze1",
    charset = "utf8mb4"
)
#print(datuBaze)

# Izveidot datu bāzi
# 1. Izveido kursoru
kursors = datuBaze.cursor()

# 2. Izveido pašu datu bāzi
kursors.execute("CREATE DATABASE IF NOT EXISTS datubaze1")

# Izvada datu bāžu sarakstu no savienojuma
kursors.execute("SHOW DATABASES")
for x in kursors:
    print(x)

# Izveido tabulu datu bāzē
# Izmanto uzreiz .execute()
kursors.execute("CREATE TABLE IF NOT EXISTS dati (id INT PRIMARY KEY, Vards VARCHAR(255), Vecums INT)")
# Sadala sql un vertibas atsevišķi
sql = "CREATE TABLE IF NOT EXISTS dati2 (id INT PRIMARY KEY, Vards VARCHAR(255), Vecums INT)"
kursors.execute(sql)

# Tabulai pievieno ierakstus
#kursors.execute("INSERT INTO dati (id, Vards, Vecums) VALUES (%s, %s, %s)", (3, "Jana", 35))
datuBaze.commit()

# Izvada tabulas datus konsolē
kursors.execute("SELECT * FROM dati")
for x in kursors:
    print(*x)

# Izdzēst ierakstu
kursors.execute("DELETE FROM dati WHERE id = 2")
datuBaze.commit()