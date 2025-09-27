'''
    EN ESTA CLASE VEREMOS EL EJEMPLO DE UN POST CON FAST API
    para registrar los datos importamos desde fast API un metodo que nos ayudara a convertir estos valores a valores que vienen dentro del cuerpo de la peticion
    que se conoce como REQUEST BODY tambien debemos importa fastapi.response

'''
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

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

#dentro de post tenemos que indicarle la URL y tambien le colocamos los tags
@api.post('/movies',tags=['Movies'])
#colocaremos los datos que vamos a recibir
#al colocar el parametro int = Body() le decimos que estamos conviertiendo este parametro query a un valor que va ser recibido como el cuerpo de la peticion
def createMovie(
        id:int = Body(),
        title:str = Body() ,
        overview:str = Body() ,
        year:int  = Body(),
        rating:float = Body() ,
        category:str = Body()
):
    #aca accedemos a los datos que queremos insertar en nuestro listado de peliculas
    #en este caso insertaremos un diccionario
    movies.append({
        'id':id,
        'title':title,
        'overview':overview,
        'year':year,
        'rating':rating,
        'category':category
    })
    return movies
