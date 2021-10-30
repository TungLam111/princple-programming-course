from typing import List, Optional, Tuple, Union

Movie = Tuple[str, str, int]

def find_movie(search_term: Union[str, None], movies: List[Movie]) -> Union[Movie, None]:
	if movies is None:
		return None
	for title, director, year in movies:
		if title == search_term:
			return (title, director, year)

def show_movies(movies: List[Movie]) :
	if movies is None:
		return
	for movie in movies:
		print_movie(movie)

def print_movie(movie: Union[None, Movie]) -> Union[None]:
	if movie is None:
		return None
	title, director, year = movie
	print(f"{title} ({year}), by {director}")

movies: List[Movie] = [
	("Finding Nemo", "Andrew Stanton", 2005),
	("Inside Out", "Pete Docter", 2015),
	("Toy Story 3", "Lee Unkrich", 2010)
]

show_movies([None, None])
show_movies(None)
show_movies(movies)

search_result = find_movie("Finding Nemo", movies)
if search_result:
	print_movie(search_result)
else:
	print("Couldn't find movie.")


search_result = find_movie(None, movies)
if search_result:
	print_movie(search_result)
else:
	print("Couldn't find movie.")

search_result = find_movie("Finding Nemo", None)
if search_result:
	print_movie(search_result)
else:
	print("Couldn't find movie.")

search_result = find_movie(None, None)
if search_result:
	print_movie(search_result)
else:
	print("Couldn't find movie.")