from typing import NamedTuple

class Movie(NamedTuple):
    id: int
    title: str
    rating: float
    certified_fresh: bool

def movie_function(movies: list[Movie], limit=10) -> list[Movie]:
    filtered_movies = [movie for movie in movies if movie.certified_fresh]
    filtered_movies.sort(key=lambda movie: movie.rating, reverse=True)
    return filtered_movies[:limit]

movies = [
    Movie(1, "The Shawshank Redemption", 5, True),
    Movie(2, "The Godfather", 7, True),
    Movie(3, "The Dark Knight", 9.0, True),
    Movie(4, "12 Angry Men", 6.5, True),
    Movie(5, "Schindler's List", 8.9, True),
    Movie(6, "Pulp Fiction", 10, True),
    Movie(7, "The Lord of the Rings: The Return of the King", 9.5, True),
    Movie(8, "The Good, the Bad and the Ugly", 10, True),
    Movie(9, "Fight Club", 9.9, True),
    Movie(10, "Forrest Gump", 4, True),
    Movie(11, "Inception", 6.8, True),
    Movie(12, "The Matrix", 8.7, True),
]

highest_rated_movies = movie_function(movies, limit=10)

print("Highest Rated Certified Fresh Movies:")
for movie in highest_rated_movies:
    print(f"{movie.title} - Rating: {movie.rating}")