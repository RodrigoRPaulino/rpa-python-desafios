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
            "TrustServerCertificate=yes;"
        )