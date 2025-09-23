'''
    PARAMETROS DE RUTA SON LOS VALORES QUE PODEMOS PASAR DENTRO DE LA URL
'''
from fastapi import FastAPI
api = FastAPI()

@api.get('/',tags = ['Home'])
def home():
 return "Hola Ricardo"


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
 }
]
#
@api.get('/movies',tags=['Home'])
def get_movies():
 return movies

#debemos añadir el parametro id como parametros de la funcion
@api.get('/movie/{id}',tags=['Home'])
def get_movies(id: int):
    return id

#ahora lo adaptaremos a nuestro movies debemos recorrerlo con un for esto nos ayudara a poder buscarlo por un id
@api.get('/movies/{id}',tags=['Pelis'])
def get_movies_id(id:int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return[]

