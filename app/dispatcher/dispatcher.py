from app.services.excel_service import ExcelService
from app.services.database_service import DatabaseService

class Dispatcher:
    def __init__(self):
        self.excel = ExcelService()
        self.db = DatabaseService()

    def run(self):
        clientes = self.excel.read_clientes("data/clientes.xlsx")
        
        for cliente in clientes:
            try:
                print(f"Inserindo: {cliente.nome} - {cliente.email}")
                self.db.insert_cliente(cliente)
            except Exception as e:
                print(f"Erro ao inserir {cliente.nome}: {e}")

        print(f"{len(clientes)} clientes carregados com sucesso!")