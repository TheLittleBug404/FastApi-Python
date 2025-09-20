'''
aprendiendo un poco mas con el get podemos ver que podemos enviar diferentes tipos de respuestas como un string diccionarios etc
tambien podemos enviar una respuesta html para eso debemos importar desde FAST API.response
'''

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
#Este end point me retorna una respuesta de tipo String
@app.get('/',tags=['Home'])

def home():
    return "Hola Home"

#este end point me retorna una respuesta de tipo diccionario
@app.get('/movies',tags=['Home'])

def home():
    return {
        "id": 1,
        "titulo": "Batman"
    }

#en este end point retornaremos un html
@app.get('/respuestaHTML',tags=['HTML'])
#dentro de HTMLResponse debemos enviar la etiqueta html que queremos enveiar
def home():
    return HTMLResponse('<h1> Hola Mundo</<h1>')

#ahora armaremos nuestro ejemplo para poder colocar nuestro listado de peliculas
movies = [
    {
        "id" : 1,
        "title" : "Superman",
        "overview" : "Una nueva pelicula para este 2025 de Superman",
        "year" : 2025,
        "rating" : 8.2,
        "category" : "superhero"
    }
]
#aca retornaremos la lista de movies
@app.get('/peliculas',tags=['Home'])
def home():
    return movies
