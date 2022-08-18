# Importa el módulo sqlite3
import sqlite3

# Crea un objeto de conexión a la base de datos SQLite
con = sqlite3.connect("db.sqlite3")

# Con la conexión, crea un objeto cursor
cur = con.cursor()

# El resultado de "cursor.execute" puede ser iterado por fila
for row in cur.execute('SELECT * FROM species;'):
    print(row)

# No te olvides de cerrar la conexión
con.close()