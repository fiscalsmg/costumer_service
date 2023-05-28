from app.config.customer_actions import ClientDAO
from app.schemas.input_data_client import (
    InputDataClient,
    UpdateInputDataClient,
)


def lambda_handler(event, context):
    print(event)
    path: str = event.get("path")
    method: str = event.get("httpMethod")

    if method == "GET" and path == "/clients":
        costumers: ClientDAO = ClientDAO.selection()
        return costumers
    elif method == "POST" and path == "/save/clients":
        custumer: InputDataClient = event.get("InputDataClient")
        costumers: ClientDAO = ClientDAO.insertion(costumer=custumer)
        return costumers
    elif method == "PUT" and path.startswith("/client/"):
        phone_number: int = event.get("phoneNumber")
        input: UpdateInputDataClient = event.get("updateInputDataClient")
        costumers: ClientDAO = ClientDAO.updated(
            costumer=input, id_phone=phone_number
        )
        return costumers
    elif method == "DELETE" and path.startswith("/client/"):
        phone_number: int = event.get("phoneNumber")
        costumers: ClientDAO = ClientDAO.delete(id_phone=phone_number)
        return costumers
    else:
        return {"statusCode": 404, "body": "Ruta no encontrada"}
