import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseService:

    def __init__(self):
        server = os.getenv("DB_SERVER")
        database = os.getenv("DB_NAME")
        driver = os.getenv("DB_DRIVER")

        self.conn = pyodbc.connect(
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;",
            timeout=20
        )

    def insert_cliente(self, cliente):
        cursor = self.conn.cursor()

        nome = cliente.nome or ""
        email = cliente.email or ""

        cursor.execute(
            """
            INSERT INTO clientes (nome, email)
            VALUES (?, ?)
            """,
            nome,
            email
        )

        self.conn.commit()