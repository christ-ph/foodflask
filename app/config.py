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
    DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?connect_timeout=10"

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