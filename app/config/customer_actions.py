import logging
from typing import List

from app.config.connection import Connection
from app.schemas.input_data_client import (
    Costumer,
    InputDataClient,
    UpdateInputDataClient,
)


logger = logging.getLogger(__name__)


class ClientDAO:
    _SELECT = "SELECT * FROM clientes ORDER BY telefono"
    _INSERT = "INSERT INTO clientes (telefono, nombre, apellido, edad) VALUES (%s,%s, %s,%s)"
    _UPDATE = "UPDATE clientes SET nombre=%s, apellido=%s, edad=%s WHERE telefono = %s"
    _DELETE = "DELETE FROM clientes WHERE telefono = %s"

    @classmethod
    def create_customers_table(cls):
        con: Connection = Connection.get_connection()
        cursor = con.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS clientes (telefono VARCHAR(255) PRIMARY KEY, nombre VARCHAR(255), apellido VARCHAR(255), edad INT)"
        )
        con.commit()
        cursor.close()

    @classmethod
    def selection(cls):
        cls.create_customers_table()
        con: Connection = Connection.get_connection()
        cursor = con.cursor()
        cursor.execute(cls._SELECT)
        records = cursor.fetchall()

        costumers: List[InputDataClient] = []
        for record in records:
            costumer: InputDataClient = InputDataClient(
                telefono=record[0],
                nombreClient=Costumer(nombre=record[1], apellido=record[2]),
                edad=record[3],
            )

            costumers.append(costumer)

        con.commit()
        cursor.close()
        logger.info(f"Se leen registros {costumers}")
        return costumers

    @classmethod
    def insertion(cls, costumer: InputDataClient):
        cls.create_customers_table()
        con: Connection = Connection.get_connection()
        cursor = con.cursor()
        values = (
            costumer.telefono,
            costumer.nombreClient.nombre,
            costumer.nombreClient.apellido,
            costumer.edad,
        )
        cursor.execute(cls._INSERT, values)
        con.commit()
        cursor.close()
        logger.info(f"Cliente insertado {costumer}")
        return costumer

    @classmethod
    def updated(cls, costumer: UpdateInputDataClient, id_phone: int):
        cls.create_customers_table()
        con: Connection = Connection.get_connection()
        cursor = con.cursor()
        values = (
            costumer.nombreClient.nombre,
            costumer.nombreClient.apellido,
            costumer.edad,
            id_phone,
        )
        cursor.execute(cls._UPDATE, values)
        con.commit()
        cursor.close()
        logger.info(f"Campos actualizados {costumer}")
        return costumer

    @classmethod
    def delete(cls, id_phone: int):
        cls.create_customers_table()
        con: Connection = Connection.get_connection()
        cursor = con.cursor()
        values = (id_phone,)
        cursor.execute(cls._DELETE, values)
        con.commit()
        cursor.close()
        logger.info(f"Cliente eliminado {id_phone}")
        return {"deleteCostumer": id_phone}
