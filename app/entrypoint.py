import logging
import sys
from typing import Any

from fastapi import APIRouter
from app.schemas.input_data_client import (
    InputDataClient,
    UpdateInputDataClient,
)
from app.costumer.lambda_function import lambda_handler


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

app_client = APIRouter()


@app_client.get("/clients")
def get_client():
    event: dict[str, Any] = {"path": "/clients", "httpMethod": "GET"}
    customers = lambda_handler(event=event, context=None)
    return customers


@app_client.post("/save/clients")
def crate_client(input: InputDataClient):
    event: dict[str, Any] = {
        "path": "/save/clients",
        "httpMethod": "POST",
        "InputDataClient": input,
    }
    customers = lambda_handler(event=event, context=None)
    return customers


@app_client.put("/client/{phone_number}")
def update_client(phone_number: int, input: UpdateInputDataClient):
    event: dict[str, Any] = {
        "path": "/client/",
        "httpMethod": "PUT",
        "updateInputDataClient": input,
        "phoneNumber": phone_number,
    }
    customers = lambda_handler(event=event, context=None)
    return customers


@app_client.delete("/client/{phone_number}")
def delete_cliente(phone_number: int):
    event: dict[str, Any] = {
        "path": "/client/",
        "httpMethod": "DELETE",
        "phoneNumber": phone_number,
    }
    customers = lambda_handler(event=event, context=None)
    return customers
