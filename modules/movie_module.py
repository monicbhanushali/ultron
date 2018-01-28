from imdb import IMDb
ia = IMDb()

the_matrix = ia.get_keyword('dystopia', results=5)
print(ia.get_top250_movies())
