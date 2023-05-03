import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Egypte3813", database="LaPlateforme"
)

# Create a cursor object
mycursor = mydb.cursor()

# Insert the data into the etage table
sql = "INSERT INTO etage (nom, numero, superficie) VALUES (%s, %s, %s)"
val = [("RDC", 0, 500), ("R+1", 1, 500)]
mycursor.executemany(sql, val)

# Insert the data into the salles table
sql = "INSERT INTO salles (nom, id_etage, capacite) VALUES (%s, %s, %s)"
val = [
    ("Lounge", 1, 100),
    ("Studio Son", 1, 5),
    ("Broadcasting", 2, 50),
    ("Bocal Peda", 2, 4),
    ("Coworking", 2, 80),
    ("Studio Video", 2, 5),
]
mycursor.executemany(sql, val)

# Commit the changes
mydb.commit()

print(mycursor.rowcount, "rows inserted.")

"""  -- Insert the data into the etage table
INSERT INTO etage (nom, numero, superficie) VALUES
('RDC', 0, 500),
('R+1', 1, 500); 

-- Insert the data into the salles table
INSERT INTO salles (nom, id_etage, capacite) VALUES
('Lounge', 1, 100),
('Studio Son', 1, 5),
('Broadcasting', 2, 50),
('Bocal Peda', 2, 4),
('Coworking', 2, 80),
('Studio Video', 2, 5);


"""
