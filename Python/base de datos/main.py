import mysql.connector

# Conexion

database = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd ="root",
    database="python"


)

cursor = database.cursor()

#conexion a sido correcta
#print(database)
""" 
cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASE")

for bd in cursor:
    print(bd)
"""

# crear tabla

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS python.vehiculos(
	id int(10) auto_increment NOT NULL,
	marca varchar(10) NOT NULL,
	modelo varchar(10) NOT NULL,
	precio FLOAT(10,2) NOT NULL,
	CONSTRAINT vehiculos_PK PRIMARY KEY (id)
)

""")
               
# insertar data               

# cursor.execute(INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500 )")
coches = [ 
    ('Seat', 'Ibiza', 5000 ),
    ('Reanaut', 'clio', 15000 ),
    ('citrone', 'saxo', 2000 ),
    ('mercedes', 'clase C', 35000 )

]
#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()





