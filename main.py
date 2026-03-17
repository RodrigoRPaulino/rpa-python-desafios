from app.services.database_service import DatabaseService

if __name__ == "__main__":
    db = DatabaseService()
    print(db.test_connection())