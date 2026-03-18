from app.services.database_service import DatabaseService

class Worker:
    def __init__(self):
        self.db = DatabaseService()

    def process(self):
        cursor = self.db.conn.cursor()

        cursor.execute(
            """SELECT  id,nome,email FROM clientes
            WHERE status = 'PENDING'
            """
        )
        rows = cursor.fetchall()

        for row in rows:
            print(f"Processando Cliente: {row.nome}")

            # simulação de processamento
            cursor.execute("""
                UPDATE clientes
                SET status = 'DONE'
                WHERE id = ?
            """, row.id)

        self.db.conn.commit()