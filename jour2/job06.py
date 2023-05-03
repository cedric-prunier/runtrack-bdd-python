import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Egypte3813", database="LaPlateforme"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SELECT query to calculate the total superficie of all the étages
mycursor.execute("SELECT SUM(capacite) AS 'capacite_totale' FROM salles")

# Fetch the row returned by the query
result = mycursor.fetchone()

# Display the result in a formatted message
capacite_totale = result[0]
message = f"La capacité de toutes les salles est de: {capacite_totale} "
print(message)
