from typing import List, Tuple

Movie = Tuple[str, str, int]

def show_movies(movies: List[Movie]):
	for title, director, year in movies:
		print(f"{title} ({year}), by {director}")

movies: List[Movie] = [
	("Finding Nemo", "Andrew Stanton", 2005),
	("Inside Out", "Pete Docter", 2015),
	("Toy Story 3", "Lee Unkrich", 2010)
]

show_movies(movies)