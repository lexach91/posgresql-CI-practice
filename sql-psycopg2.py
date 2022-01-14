from unittest import result
from matplotlib.pyplot import connect
import psycopg2


# Connect to the "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all the records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# cursor.execute(f'SELECT * FROM "Artist" WHERE "Name" = \'Queen\'')

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 51')


# Fetch the results (multiple)
# results = cursor.fetchall()

# Fetch the results (single)
results = cursor.fetchone()

# Close the connection
connection.close()

# Print the results
for result in results:
    print(result)