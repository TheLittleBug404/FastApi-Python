from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional,List

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

class MovieClass(BaseModel):
    id : int
    title: str
    overview : str
    year: int
    rating: float
    category:str

class MovieUpdate(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str


@api.get('/movies',tags = ['Movies'])
def get_movies() -> List[MovieClass]:
    return movies

@api.get('/movies/{id}',tags=['Movies'])
def get_movie(id:int) ->MovieClass:
    for movie in movies:
        if movie['id'] == id:
            return movie

@api.post('/movies',tags=['Movies'])
def create_movies(movie:MovieClass):
    movies.append(movie.model_dump())
    return movies

@api.put('/movies/{id}',tags= ['Movies'])
def update_movie(id:int, movie : MovieUpdate):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
    return movies

