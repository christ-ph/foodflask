
from app import create_app
from app.utils.init_db import init_db
from app.services.storage import *
# from app.utils.database import db, Base
# from app.dao.db_connection import DatabaseConnection

init_db()
# Création de l'application
app = create_app()


# Initialisation de la base de données
# with app.app_context():
#     # Création des tables
#     Base.metadata.create_all(bind=db.engine)
    
#     # Vérification des tables
#     bd = DatabaseConnection()
#     print("Tables existantes :", bd.list_tables())

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000, debug=True)


# from app import app
# from app.utils.database import Base, engine
# from app.dao.db_connection import DatabaseConnection
# from app.api import bp as api_blueprint


# bd = DatabaseConnection()
# Base.metadata.create_all(bind=engine)
# app.register_blueprint(api_blueprint)


# if __name__ == "__main__":
#     print("tables existantes :",bd.list_tables())
#     app.run(host='0.0.0.0',port=5000,debug=True)