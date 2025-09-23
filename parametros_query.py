'''
    Estos parametros son diferentes a los parametros de ruta
    ejemplo PARAMETROS RUTA
    localhost:5000/movies/123   de esta forma especificamos el parametro ruta
    pero los parametros query no va unicamente su valor si no la clave y el valor
    ejemplo PARAMETROS QUERY
    localhost:5000/movies/?id=123
    notamos que este parametro query tiene que ir seguido de un signo de interrogacion
    los podemos detectar de la siguiente forma que esta en el metodo get_movie_query
'''
from fastapi import FastAPI

api = FastAPI()
movies = [
    {
        "id": 1,
        "title": "Superman",
        "overview": "Una nueva pelicula para este 2025 de Superman",
        "year": 2025,
        "rating": 8.2,
        "category": "superhero"
    },
    {
        "id": 2,
        "title": "Batman",
        "overview": "Batman con Robert Pattinson",
        "year": 2023,
        "rating": 9,
        "category": "superhero"
    },
    {
        "id": 3,
        "title": "Toy Story",
        "overview": "Woody y Buzz se adentran en una nueva aventura",
        "year": 2022,
        "rating": 8.6,
        "category": "Animacion"
    }
]
#en el path debe tener una barra al final asi sabemos que es parametro query
@api.get('/movies/',tags=['Peliculas'])
#la forma para definir un parametro en FAST API es añadirlo dentro de la funcion
def get_movie_query(category:str):
    return category

#si queremos añadir mas de un parametro QR lo podemos hacer añadiendolo en la funcion
@api.get('/movie/',tags=['Peliculas'])
def get_movie_query_mas_parametros(category:str, year:int):
    return year
#ahora usaremos categoria para filtrar uno de los parametros query
@api.get('/movies/categoria/',tags=['Peliculas'])
def get_movies_by_category(category :str,year:int):
    for movie in movies:
        if(movie['category'] == category):
            return movie
    return []
