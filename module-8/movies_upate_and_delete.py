import mysql.connector

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# Establish a connection to the database
db = mysql.connector.connect(**config)
print("\n Database user {} connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.

    # Inner join query
    cursor.execute("""
        SELECT film.film_name AS Name, 
               film.film_director AS Director, 
               genre.genre_name AS Genre, 
               studio.studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)

    # Get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --\n".format(title))

    # Iterate over the film dataset and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Create a cursor object
cursor = db.cursor()

# Insert a new film
cursor.execute("""
    INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES (4, 'Split', 2016, 117, 'M. Night Shyamalan', 2, 1)
""")

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

#Updating Alien
cursor.execute("""
    UPDATE film
    SET genre_id = 1
    WHERE film_id = 2
""")

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

#Deleting Gladiator
cursor.execute("""
    DELETE FROM film
    WHERE film_id = 1
""")

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

cursor.close()
db.close()
