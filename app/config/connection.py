import logging

import mysql.connector
from app.config.settings import settings


logger = logging.getLogger(__name__)


class Connection:
    """Clase encargada de conectar y crear la tabla base del ejercicio"""

    _DATABASE = settings.DATABASE
    _USUERNAME = settings.USUERNAME
    _PASSWORD = settings.PASSWORD
    _BD_PORT = settings.BD_PORT
    _HOST = settings.HOST

    @classmethod
    def get_connection(cls):
        """Crea la conexion con la base de datos

        Returns:
            connection: Objeto conector a la base de datos
        """
        try:
            connection = mysql.connector.connect(
                host=cls._HOST,
                user=cls._USUERNAME,
                password=cls._PASSWORD,
                database=cls._DATABASE,
            )
            logger.info(f"Se crea conexion exitosa {connection}")
            return connection
        except Exception as e:
            logger.error(
                f"Ocurrio un error al intentar realizar conexion con la base de datos {e}"
            )

    @classmethod
    def close_conection(cls):
        cls.get_connection().close()
