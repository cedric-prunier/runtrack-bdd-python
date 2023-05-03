import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Egypte3813", database="LaPlateforme"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a SELECT query to retrieve the names and capacities from the salles table
mycursor.execute("SELECT nom, capacite FROM salles")

# Fetch all the rows returned by the query
result = mycursor.fetchall()

# Convert the result into a list
result_list = list(result)

# Display the result in a formatted list
print(result_list)


"""-- commande terminal
SELECT nom, capacite FROM salles;"""
