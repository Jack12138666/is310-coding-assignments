#list of favorite movies
favorite_movies = [
    ("The Matrix", 1999),
    ("The Dark Knight", 2008),
    ("Inception", 2010),
    ("Interstellar", 2014),
    ("Avatar", 2009)
]


#check release year
def check_movie(movie):
    name, year = movie

    if year < 2000:
        print("This movie was released before 2000")
        return None
    else:
        print("This movie was released after 2000")
        return name


#empty list
recent_movies = []

#loop through movies
for movie in favorite_movies:
    result = check_movie(movie)

    if result is not None:
        recent_movies.append(result)

#print the list
print(recent_movies)