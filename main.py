from app.dispatcher.dispatcher import Dispatcher
from app.worker.worker import Worker

if __name__ == "__main__":
    
    print("=== DISPATCHER ===")
    dispatcher = Dispatcher()
    dispatcher.run()

    print("=== WORKER ===")
    worker = Worker()
    worker.process()

    print("Finalizado!")