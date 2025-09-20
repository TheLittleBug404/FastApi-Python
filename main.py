'''
    Al crear nuestra aplicacion este automaticamente nos lo creara en el puerto 8000
    para ocupar un nuevo puerto utilizamos el comando uvicorn main:app --port puerto_a_utilizar
    ejemplo con el puerto 5000
    uvicorn main:app --port 5000
    para añadir los cambios que hacemos utilizaremos el comando uvicorn main:app --port puerto_a_utilizar --reload
    reload nos ayuda a ejecutar nuestra aplicacion sin tener que detenerlo y volverlo a cargar
    Si queremos ejecutar nuestra aplicacion en red a otro dispositivo a un computador celular etc que este conectado
    a loa misma red que tenemos para esto le tenemos que colocar un host a nuestro comando
    ejemplo
    uvicorn main:app --host 0.0.0.0 --port 5000 --reload
    para acceder con mi ip desde el computador seria
    uvicorn main:app --host 192.168.1.15 --port 5000 --reload
'''
from fastapi import FastAPI
app = FastAPI()
#debemos colocarle / para que esta vaya a nuestro home o ruta principal
@app.get('/')
def home():
    return "Hola Mundo Ricardo Jauregui Lima"
