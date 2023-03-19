from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Define movies and user preferences
movie_data = [
    {
        "title": "The Shawshank Redemption",
        "genre": ["Drama"],
        "actors": ["Tim Robbins", "Morgan Freeman"],
        "director": "Frank Darabont",
        "year": 1994,
        "rating": 9.3
    },
    {
        "title": "The Godfather",
        "genre": ["Drama", "Crime"],
        "actors": ["Marlon Brando", "Al Pacino", "James Caan"],
        "director": "Francis Ford Coppola",
        "year": 1972,
        "rating": 9.2
    },
    {
        "title": "The Dark Knight",
        "genre": ["Action", "Crime", "Drama"],
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "director": "Christopher Nolan",
        "year": 2008,
        "rating": 9.0
    },
    {
        "title": "The Godfather: Part II",
        "genre": ["Drama", "Crime"],
        "actors": ["Al Pacino", "Robert De Niro", "Robert Duvall"],
        "director": "Francis Ford Coppola",
        "year": 1974,
        "rating": 9.0
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "genre": ["Action", "Adventure", "Drama"],
        "actors": ["Elijah Wood", "Viggo Mortensen", "Ian McKellen"],
        "director": "Peter Jackson",
        "year": 2003,
        "rating": 8.9
    },
    {
        "title": "Pulp Fiction",
        "genre": ["Crime", "Drama"],
        "actors": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
        "director": "Quentin Tarantino",
        "year": 1994,
        "rating": 8.9
    }
]

# Prompt the user to input information about their favorite movie
user_title = input("Enter the title of your favorite movie: ")
user_genre = input("Enter the genre(s) of your favorite movie, separated by commas: ")
user_actors = input("Enter the name(s) of the actor(s) in your favorite movie, separated by commas: ")
user_director = input("Enter the name of the director of your favorite movie: ")
user_year = input("Enter the year your favorite movie was released: ")


fav_genres = ["Drama", "Crime"]
fav_directors = ["Christopher Nolan"]
fav_years = [1994, 1993]

# Filter relevant movies
rel_movies = []
for movie in movie_data:
    if any(genre in fav_genres for genre in movie["genre"]) and movie["director"] in fav_directors and movie["year"] in fav_years:
        rel_movies.append(movie)

# Calculate scores for each movie
scores = []
for movie in rel_movies:
    score = 0
    if any(genre in fav_genres for genre in movie["genre"]):
        score += 1
    if movie["director"] in fav_directors:
        score += 1
    if any(str(movie["year"]) in fav_years for fav_year in fav_years):
        score += 1
    scores.append(score)

# Recommendation
if not rel_movies:
    print("Sorry, we couldn't find any movies that match your preferences.")
else:
    max_score = max(scores)
    top_movies = [rel_movies[i] for i in range(len(scores)) if scores[i] == max_score]

    if len(top_movies) == 1:
        print("We recommend you watch", top_movies[0]["title"])
    else:
        print("We recommend you watch one of these movies:")
        for movie in top_movies:
            i=0
            print("We recommend you watch", top_movies[0]["title"])
            i+=1


