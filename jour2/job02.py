import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Egypte3813", database="LaPlateforme"
)

# Create a cursor object
mycursor = mydb.cursor()

# Create the etage table
mycursor.execute(
    "CREATE TABLE etage (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255) NOT NULL, numero INT NOT NULL, superficie INT NOT NULL)"
)

# Create the salles table
mycursor.execute(
    "CREATE TABLE salles (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255) NOT NULL, id_etage INT NOT NULL, capacite INT NOT NULL)"
)

# Commit the changes
mydb.commit()


# commande terminal
# -- Create the etage table
"""CREATE TABLE etage (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(255),
  numero INT,
  superficie INT
);

-- Create the salles table
CREATE TABLE salles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(255),
  id_etage INT,
  capacite INT
);
"""
