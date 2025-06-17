
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import Config
from dotenv import load_dotenv

load_dotenv()

# Configuration de la base de données
DATABASE_URL = Config.DB_URL
engine = create_engine(DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définissez 'db' comme alias de scoped_session pour la compatibilité
db_session = scoped_session(SessionLocal)
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """Initialise la base de données"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Générateur de session pour les dépendances"""
    try:
        yield db_session
    finally:
        db_session.remove()








# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from app.config import Config
# import os
# from dotenv import load_dotenv

# # Charger les variables d'environnement depuis .env
# load_dotenv()

# # Exemple : postgresql://username:password@localhost:5432/dbname
# DATABASE_URL = Config.DB_URL

# # Créer l'engine SQLAlchemy
# engine = create_engine(DATABASE_URL)

# # Création du session maker (à utiliser dans les dépendances)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base pour déclarer les modèles ORM
# Base = declarative_base()

# # ✅ AJOUTER CETTE LIGNE - c'est ce qui manquait !
# db = SessionLocal()

# # Optionnel : une fonction utilitaire à utiliser dans les routes/services (meilleure pratique)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Alternative recommandée : fonction pour obtenir une session
# def get_db_session():
#     """Retourne une nouvelle session de base de données"""
#     return SessionLocal()

# # Fonction pour fermer la session globale (à appeler à la fin de l'app)
# def close_db():
#     """Ferme la session globale de base de données"""
#     global db
#     if db:
#         db.close()









# # from sqlalchemy import create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy.orm import sessionmaker
# # from app.config import Config
# # import os
# # from dotenv import load_dotenv

# # # Charger les variables d'environnement depuis .env
# # load_dotenv()

# # # Exemple : postgresql://username:password@localhost:5432/dbname
# # DATABASE_URL = Config.DB_URL

# # # Créer l'engine SQLAlchemy
# # engine = create_engine(DATABASE_URL)

# # # Création du session maker (à utiliser dans les dépendances)
# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # # Base pour déclarer les modèles ORM
# # Base = declarative_base()

# # # ➕ Ajouter ceci pour permettre `from app.utils.database import db_session`
# # db_session = SessionLocal()

# # # ➕ Optionnel : une fonction utilitaire à utiliser dans les routes/services (meilleure pratique)
# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()
