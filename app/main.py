import logging
import sys

from fastapi import FastAPI

from mangum import Mangum


from app.schemas.input_data_client import (
    InputDataClient,
    UpdateInputDataClient,
)
from app.config.customer_actions import ClientDAO

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


app: FastAPI = FastAPI(
    title="Ejercicio consula clientes",
    description="Ejercicio 2 prueba practica",
    docs_url="/docs",
)


@app.get("/")
def home():
    return {"message": "Hola!"}


# Obtener todos los clientes
@app.get("/clients")
def get_client():
    costumers: ClientDAO = ClientDAO.selection()
    return costumers


# Crear un nuevo cliente
@app.post("/save/clients")
def crate_client(input: InputDataClient):
    costumers: ClientDAO = ClientDAO.insertion(costumer=input)
    return costumers


# Actualizar los datos por numero de telefono
@app.put("/client/{phone_number}")
def update_client(phone_number: int, input: UpdateInputDataClient):
    costumers: ClientDAO = ClientDAO.updated(costumer=input, id_phone=phone_number)
    return costumers


# Eliminar de la bd por numero de telefono
@app.delete("/client/{phone_number}")
def delete_cliente(phone_number: int):
    costumers: ClientDAO = ClientDAO.delete(id_phone=phone_number)
    return costumers


handler = Mangum(app)
