import uvicorn
import Server

# Server initialisieren
server = Server()

# Ereignis-Handler hinzufügen
@server.get_app().on_event("startup")
async def startup_event():
    server.initialize_database()
   # server.logger.info("Server gestartet und bereit.")
    print("Server wird gestartet..")

@server.get_app().on_event("shutdown")
async def shutdown_event():
   # server.logger.info("Server wird heruntergefahren.")
   print("Server wird heruntergefahren")

# FastAPI-App bereitstellen
app = server.get_app()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
