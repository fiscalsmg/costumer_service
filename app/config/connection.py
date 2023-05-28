import logging

import mysql.connector

logger = logging.getLogger(__name__)


class Connection:
    """Clase encargada de conectar y crear la tabla base del ejercicio"""

    _DATABASE = "clientdb"
    _USUERNAME = "admin"
    _PASSWORD = "16091106"
    _BD_PORT = "3306"
    _HOST = "database-1.cv056iak7inx.us-east-2.rds.amazonaws.com"

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
