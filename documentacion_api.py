''''
    En aca veremos la documentacion para que tenemos para nuestro FastAPI para describir nuestros servicios REST
    para ver la documentacion simplemente nos vamos a la ruta acompañado de /docs
    ejemplo
        http://192.168.1.3:5000/docs
'''

from fastapi import FastAPI

app = FastAPI()
#titulo en mi pagina web que es parecido al Swagger
app.title = "Mi primera aplicacion con FASTAPI"
#version que aparece en mi web documentacion
app.version = "1.0.0"

#aca creamos un end point
@app.get('/',tags=['Home'])
def home():
    return "Documentacion en Fast API"

#aca creamos un end point
@app.get('/home',tags=['Home'])
def home():
    return "Documentacion en Fast API otro end point"