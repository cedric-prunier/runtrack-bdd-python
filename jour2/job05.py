import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Egypte3813", database="LaPlateforme"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SELECT query to calculate the total superficie of all the étages
mycursor.execute("SELECT SUM(superficie) AS 'superficie_totale' FROM etage")

# Fetch the row returned by the query
result = mycursor.fetchone()

# Display the result in a formatted message
superficie_totale = result[0]
message = f"La superficie de La Plateforme est de {superficie_totale} m2"
print(message)


# SELECT SUM(superficie) AS 'superficie_totale' FROM etage;
