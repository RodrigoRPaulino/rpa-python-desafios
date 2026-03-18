import pandas as pd
from app.models.item import Cliente

class ExcelService:
    def read_clientes(self, path):
        df = pd.read_excel(path, dtype=str)

        print("=== DATAFRAME ===")
        print(df)

        clientes = []

        for _, row in df.iterrows():
            cliente = Cliente(
                nome=row["nome"],
                email=row["email"]
            )
            clientes.append(cliente)

        return clientes  # ✅ FORA DO LOOP