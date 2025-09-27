from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse
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
api = FastAPI()
@api.get('/movies',tags=['Movies'])
def get_movies():
    return movies
#le pasaremos un parametro de tipo path y este sera el id que se encuentra al lado de movies {id}
#con el put vamos a modificar
@api.put('/movies/{id}',tags=['Movies'])
#le indicaremos que pelicula vamos a modificar en los parametros
def update_movie(
    id:int,
    title:str = Body() ,
    overview:str = Body() ,
    year:int  = Body(),
    rating:float = Body() ,
    category:str = Body()
):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
    return movies

#con el delete vamos a eliminar
@api.delete('/movies/{id}',tags = ['Movies'])
def delete_movie(id:int):
    for movie in movies:
        #recordemos que el id es el id de la ruta
        if movie['id'] == id:
            movies.remove(movie)
    return movies