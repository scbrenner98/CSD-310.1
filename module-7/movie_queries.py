import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "movies_user",
    "password" : "popcorn",
    "host" : "127.0.0.1",
    "database" : "movies",
    "raise_on_warnings" : True
 }


db = mysql.connector.connect(**config)
print("\n Database user {} connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))


cursor = db.cursor()

cursor.execute("SELECT * FROM studio")
studio = cursor.fetchall()

cursor.execute("SELECT * FROM genre")
genre = cursor.fetchall()

cursor.execute("SELECT film_name, film_runtime FROM film HAVING film_runtime < 120")
film = cursor.fetchall()

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
director = cursor.fetchall()

print("-- Displaying Studio RECORDS --")
for studio in studio:
    print("Studio ID: {} \nStudio Name: {} \n".format(studio[0], studio[1]))

print("-- Displaying Genre RECORDS --")
for genre in genre:
    print("Genre ID: {} \nGenre Name: {}\n".format(genre[0], genre[1]))

print("-- Displaying Short Film RECORD --")
for film in film:
    print("Film Name: {} \nFilm Runtime: {}\n".format(film[0], film[1]))

print("== Displaying Films By Director --")
for director in director:
    print("Film Name: {} \nFilm Director: {}\n".format(director[0], director[1]))

cursor.close()
db.close()