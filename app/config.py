import os
from pathlib import Path
from dotenv import load_dotenv

# Charge les variables d'environnement
load_dotenv()

# Répertoire de base du projet (compatible local/Docker)
BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    # === Configuration de la base de données ===
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "foods")
    DB_USER = os.getenv("DB_USER", "christ")
    DB_PASS = os.getenv("DB_PASSWORD", "123456")

    # URL SQLAlchemy
    DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?connect_timeout=10"

    # === Mode d'application et sécurité ===
    MODE = os.getenv("APP_MODE", "ORM")
    SECRET_KEY = os.getenv("SECRET_KEY", "votre_cle_secrete_ici")

    # === Chemins (upload et logs)
    UPLOAD_FOLDER = Path(os.getenv("UPLOAD_FOLDER", BASE_DIR / "uploads/images"))
    LOG_FILE = BASE_DIR / "logs" / "app.log"

    @classmethod
    def check_db_connection(cls):
        """Teste la connexion à la base de données"""
        import sqlalchemy
        from sqlalchemy.exc import OperationalError

        try:
            engine = sqlalchemy.create_engine(cls.DB_URL)
            with engine.connect():
                print("✅ Connexion à la base réussie.")
                return True
        except OperationalError as e:
            print(f"❌ Erreur de connexion à la base : {e}")
            return False

# === Création des répertoires nécessaires ===
Config.UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
Config.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)


# import os
# from pathlib import Path
# from dotenv import load_dotenv

# # Charge les variables d'environnement depuis un fichier .env s'il existe
# load_dotenv()

# class Config:
#     # === Configuration de la base de données ===
#     DB_HOST = os.getenv("DB_HOST", "localhost")
#     DB_PORT = os.getenv("DB_PORT", "5432")
#     DB_NAME = os.getenv("DB_NAME", "foods")  # ✅ S'assurer que 'foods' est le nom par défaut
#     DB_USER = os.getenv("DB_USER", "christ")
#     DB_PASS = os.getenv("DB_PASSWORD", "123456")

#     # URL SQLAlchemy (ORM)
#     DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?connect_timeout=10"

#     # === Mode d'application ===
#     MODE = os.getenv("APP_MODE", "ORM")
#     SECRET_KEY = os.getenv("SECRET_KEY", "votre_cle_secrete_ici")

#     # === Dossier d'upload des fichiers ===
#     UPLOAD_FOLDER = Path(os.getenv("UPLOAD_FOLDER", "uploads/images"))
#     UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

#     # === Fichier de log ===
#     LOG_FILE = Path("logs/app.log")
#     LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
#     Config.UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
#     config.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

#     @classmethod
#     def check_db_connection(cls):
#         """Teste la connexion à la base de données"""
#         import sqlalchemy
#         from sqlalchemy.exc import OperationalError

#         try:
#             engine = sqlalchemy.create_engine(cls.DB_URL)
#             with engine.connect():
#                 print("✅ Connexion à la base réussie.")
#                 return True
#         except OperationalError as e:
#             print(f"❌ Erreur de connexion à la base : {e}")
#             return False


# import os
# from pathlib import Path
# from dotenv import load_dotenv

# # Charge les variables d'environnement
# load_dotenv()

# class Config:
#     # Configuration DB
#     DB_HOST = os.getenv("DB_HOST", "localhost")
#     DB_PORT = os.getenv("DB_PORT", "5432")
#     DB_NAME = os.getenv("DB_NAME", "foods")
#     DB_USER = os.getenv("DB_USER", "christ")
#     DB_PASS = os.getenv("DB_PASSWORD", "123456")
    
#     # URL de connexion
#     DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?connect_timeout=10"
    
#     # App config
#     MODE = os.getenv("APP_MODE", "ORM")
#     SECRET_KEY = os.getenv("SECRET_KEY", "votre_cle_secrete_ici")
    
#     # Uploads
#     UPLOAD_FOLDER = Path(os.getenv("UPLOAD_FOLDER", "uploads/images"))
#     UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
    
#     # Logging
#     LOG_FILE = Path("logs/app.log")
#     LOG_FILE.parent.mkdir(exist_ok=True)

#     @classmethod
#     def check_db_connection(cls):
#         """Vérifie que la connexion DB est fonctionnelle"""
#         import sqlalchemy
#         from sqlalchemy.exc import OperationalError
        
#         try:
#             engine = sqlalchemy.create_engine(cls.DB_URL)
#             with engine.connect() as conn:
#                 return True
#         except OperationalError as e:
#             print(f"Erreur de connexion DB: {e}")
#             return False


# import os
# from pathlib import Path

# class Config:
#     # Configuration flexible pour les différents environnements
#     DB_HOST = os.getenv("DB_HOST", "localhost")  # "db" dans Docker, "localhost" en local
#     DB_PORT = os.getenv("DB_PORT", "5432")
#     DB_NAME = os.getenv("DB_NAME", "foods")
#     DB_USER = os.getenv("DB_USER", "christ")
#     DB_PASS = os.getenv("DB_PASSWORD", "123456")
    
#     DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
#     MODE = os.getenv("APP_MODE", "ORM")
#     UPLOAD_FOLDER = Path(os.getenv("UPLOAD_FOLDER", "uploads/images"))
#     UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)



# import os
# from pathlib import Path

# class Config:
#     # Configuration flexible pour les différents environnements
#     DB_HOST = os.getenv("DB_HOST", "localhost")  # "db" dans Docker, "localhost" en local
#     DB_PORT = os.getenv("DB_PORT", "5432")       # Port par défaut PostgreSQL
#     DB_NAME = os.getenv("DB_NAME", "foods")
#     DB_USER = os.getenv("DB_USER", "christ")
#     DB_PASS = os.getenv("DB_PASSWORD", "123456")
    
#     # Construction de l'URL de connexion
#     DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
#     MODE = os.getenv("APP_MODE", "ORM")  # 'ORM' ou 'DAO'
    
#     # Configuration des uploads
#     UPLOAD_FOLDER = Path(os.getenv("UPLOAD_FOLDER", "uploads/images"))
#     UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
# import os
# from pathlib import Path

# class Config:
#     DB_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://christ:123456@localhost:5432/foods")
#     MODE = 'ORM'  # dao ou orm

#     UPLOAD_FOLDER = Path("uploads/images")
#     UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


# import os
# from pathlib import Path


# class Config:
#     DB_URL = os.getenv("BD_URL","postgresql://christ:123456@localhost:5432/foods")
#     MODE = 'ORM' # dao ou orm

#     UPLOAD_FOLDER = Path("uploads/images")
#     UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)



# class StorageConfig:
#     # Chemins absolus
#     BASE_DIR = Path(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#     MEDIA_ROOT = BASE_DIR / "media"
    
#     # Sous-dossiers
#     PATHS = {
#         'sushi': MEDIA_ROOT / "sushi",
#         # 'ingredients': MEDIA_ROOT / "ingredients",
#         # 'users': MEDIA_ROOT / "users",
#         # 'temp': MEDIA_ROOT / "temp"
#     }
    
#     # Types autorisés
#     ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp'}
#     MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

#     @classmethod
#     def init_storage(cls):
#         """Crée les dossiers s'ils n'existent pas"""
#         for path in cls.PATHS.values():
#             path.mkdir(parents=True, exist_ok=True)

# # Initialisation au démarrage
# StorageConfig.init_storage()
    
