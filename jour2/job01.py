import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Egypte3813", database="LaPlateforme"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SELECT query to retrieve all the students
mycursor.execute("SELECT * FROM etudiants")

# Fetch all the rows returned by the query
result = mycursor.fetchall()

# Display the result in the console
for row in result:
    print(row)
