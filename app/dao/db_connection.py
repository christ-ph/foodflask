
import psycopg2
from psycopg2.extras import DictCursor
import logging
from app.config import Config

logger = logging.getLogger(__name__)

class DatabaseConnection:
    _instance = None

    def __new__(cls, db_url: str =Config.DB_URL):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_connection(db_url)
        return cls._instance

    def _initialize_connection(self, db_url: str):
        try:
            self.connection = psycopg2.connect(
                db_url,
                cursor_factory=DictCursor
            )
            self._verify_or_create_tables()
            logger.info("Database connection established and tables verified")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise

    def _verify_or_create_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS person (
                id_per SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS image (
                id_img SERIAL PRIMARY KEY,
                url VARCHAR(255) NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS food (
                id_food SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                allergy TEXT,
                main_image_id INTEGER REFERENCES image(id_img)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ingredient (
                id_ing SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                unit VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS food_ingredient (
                food_id INTEGER REFERENCES food(id_food) ON DELETE CASCADE,
                ingredient_id INTEGER REFERENCES ingredient(id_ing) ON DELETE CASCADE,
                quantity FLOAT,
                PRIMARY KEY (food_id, ingredient_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS food_image (
                food_id INTEGER REFERENCES food(id_food) ON DELETE CASCADE,
                image_id INTEGER REFERENCES image(id_img) ON DELETE CASCADE,
                is_primary BOOLEAN DEFAULT FALSE,
                PRIMARY KEY (food_id, image_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS person_food (
                person_id INTEGER REFERENCES person(id_per) ON DELETE CASCADE,
                food_id INTEGER REFERENCES food(id_food) ON DELETE CASCADE,
                consumption_date DATE NOT NULL,
                quantity INTEGER DEFAULT 1,
                PRIMARY KEY (person_id, food_id)
            )
            """
        ]

        with self.connection.cursor() as cursor:
            try:
                for table_sql in tables:
                    cursor.execute(table_sql)
                self.connection.commit()
                logger.info("All tables created or verified successfully")
                logger.info(f"Existing tables: {self.list_tables()}")
            except Exception as e:
                self.connection.rollback()
                logger.error(f"Error during table creation: {e}")
                raise

    def list_tables(self):
        """Liste les tables existantes dans le schéma public"""
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)
            return [row["table_name"] for row in cursor.fetchall()]

    def get_cursor(self):
        if self.connection.closed:
            self._initialize_connection(Config.DB_URL)
        return self.connection.cursor()

    def close(self):
        if hasattr(self, 'connection') and not self.connection.closed:
            self.connection.close()
            logger.info("Database connection closed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()






















# import psycopg2
# from psycopg2.extras import DictCursor
# import logging
# from app.config import Config

# logger = logging.getLogger(__name__)

# class DatabaseConnection:
#     _instance = None

#     def __new__(cls, db_url: str = Config.DB_URL):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance._initialize_connection(db_url)
#         return cls._instance

#     def _initialize_connection(self, db_url: str):
#         """Établit la connexion et initialise la base de données"""
#         try:
#             self.connection = psycopg2.connect(
#                 db_url,
#                 cursor_factory=DictCursor
#             )
#             self._verify_or_create_tables()
#             logger.info("Database connection established and tables verified")
#         except Exception as e:
#             logger.error(f"Database connection failed: {e}")
#             raise

#     def _verify_or_create_tables(self):
#         """Crée les tables si elles n'existent pas"""
#         tables = [
#             """
#             CREATE TABLE IF NOT EXISTS person (
#                 id_per SERIAL PRIMARY KEY,
#                 name VARCHAR(100) NOT NULL,
#                 age INTEGER
#             )
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS image (
#                 id_img SERIAL PRIMARY KEY,
#                 url VARCHAR(255) NOT NULL
#             )
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS food (
#                 id_food SERIAL PRIMARY KEY,
#                 name VARCHAR(100) NOT NULL,
#                 description TEXT,
#                 allergy TEXT,
#                 main_image_id INTEGER REFERENCES image(id_img)
#             )
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS ingredient (
#                 id_ing SERIAL PRIMARY KEY,
#                 name VARCHAR(100) NOT NULL,
#                 unit VARCHAR(20)
#             )
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS food_ingredient (
#                 food_id INTEGER REFERENCES food(id_food) ON DELETE CASCADE,
#                 ingredient_id INTEGER REFERENCES ingredient(id_ing) ON DELETE CASCADE,
#                 quantity FLOAT,
#                 PRIMARY KEY (food_id, ingredient_id)
#             )
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS food_image (
#                 food_id INTEGER REFERENCES food(id_food) ON DELETE CASCADE,
#                 image_id INTEGER REFERENCES image(id_img) ON DELETE CASCADE,
#                 is_primary BOOLEAN DEFAULT FALSE,
#                 PRIMARY KEY (food_id, image_id)
#             )
#             """,
#             """
#             CREATE TABLE IF NOT EXISTS person_food (
#                 person_id INTEGER REFERENCES person(id_per) ON DELETE CASCADE,
#                 food_id INTEGER REFERENCES food(id_food) ON DELETE CASCADE,
#                 consumption_date DATE NOT NULL,
#                 quantity INTEGER DEFAULT 1,
#                 PRIMARY KEY (person_id, food_id, consumption_date)
#             )
#             """
#         ]

#         with self.connection.cursor() as cursor:
#             try:
#                 for table_sql in tables:
#                     cursor.execute(table_sql)
#                 self.connection.commit()
#                 logger.info("All tables created or verified successfully")
#             except Exception as e:
#                 self.connection.rollback()
#                 logger.error(f"Error during table creation: {e}")
#                 raise

#     def get_cursor(self):
#         """Retourne un curseur pour exécuter des requêtes SQL"""
#         if self.connection.closed:
#             self._initialize_connection(Config.DB_URL)
#         return self.connection.cursor()

#     def close(self):
#         """Ferme la connexion proprement"""
#         if hasattr(self, 'connection') and not self.connection.closed:
#             self.connection.close()
#             logger.info("Database connection closed")

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()

#     def __del__(self):
#         self.close()


# def create_tables():
#     """Fonction externe pour créer les tables sans utiliser le shell"""
#     try:
#         DatabaseConnection()
#         logger.info("Tables creation check completed.")
#     except Exception as e:
#         logger.error(f"Table creation failed: {e}")
#         raise







# # import psycopg2
# # from psycopg2.extras import DictCursor
# # import logging
# # from app.config import Config.DB_URL

# # logger = logging.getLogger(__name__)

# # class DatabaseConnection:
# #     _instance = None

# #     def __new__(cls, db_url: str = Config.DB_URL):
# #         if cls._instance is None:
# #             cls._instance = super().__new__(cls)
# #             cls._instance._initialize_connection(db_url)
# #         return cls._instance

# #     def _initialize_connection(self, db_url: str):
# #         """Établit la connexion et crée les tables si elles n'existent pas"""
# #         try:
# #             self.connection = psycopg2.connect(
# #                 db_url,
# #                 cursor_factory=DictCursor
# #             )
# #             self._verify_or_create_tables()
# #             logger.info("Database connection established and tables verified")
# #         except Exception as e:
# #             logger.error(f"Database connection failed: {e}")
# #             raise

# #     def _verify_or_create_tables(self):
# #         """Vérifie et crée les tables si nécessaire"""
# #         tables = [
# #             """
# #             CREATE TABLE IF NOT EXISTS Person (
# #                 id_per SERIAL PRIMARY KEY,
# #                 name VARCHAR(100) NOT NULL,
# #                 age INTEGER
# #             )
# #             """,
# #             """
# #             CREATE TABLE IF NOT EXISTS Image (
# #                 id_img SERIAL PRIMARY KEY,
# #                 url VARCHAR(255) NOT NULL
# #             )
# #             """,
# #             """
# #             CREATE TABLE IF NOT EXISTS Food (
# #                 id_food SERIAL PRIMARY KEY,
# #                 name VARCHAR(100) NOT NULL,
# #                 description TEXT,
# #                 allergy TEXT,
# #                 main_image_id INTEGER REFERENCES Image(id_img)
# #             )
# #             """,
# #             """
# #             CREATE TABLE IF NOT EXISTS Ingredient (
# #                 id_ing SERIAL PRIMARY KEY,
# #                 name VARCHAR(100) NOT NULL,
# #                 unit VARCHAR(20)
# #             )
# #             """,
# #             """
# #             CREATE TABLE IF NOT EXISTS Food_Ingredient (
# #                 food_id INTEGER REFERENCES Food(id_food) ON DELETE CASCADE,
# #                 ingredient_id INTEGER REFERENCES Ingredient(id_ing) ON DELETE CASCADE,
# #                 quantity FLOAT,
# #                 PRIMARY KEY (food_id, ingredient_id)
# #             )
# #             """,
# #             """
# #             CREATE TABLE IF NOT EXISTS Food_Image (
# #                 food_id INTEGER REFERENCES Food(id_food) ON DELETE CASCADE,
# #                 image_id INTEGER REFERENCES Image(id_img) ON DELETE CASCADE,
# #                 is_primary BOOLEAN DEFAULT FALSE,
# #                 PRIMARY KEY (food_id, image_id)
# #             )
# #             """,
# #             """
# #             CREATE TABLE IF NOT EXISTS Person_Food (
# #                 person_id INTEGER REFERENCES Person(id_per) ON DELETE CASCADE,
# #                 food_id INTEGER REFERENCES Food(id_food) ON DELETE CASCADE,
# #                 consumption_date DATE NOT NULL,
# #                 quantity INTEGER DEFAULT 1,
# #                 PRIMARY KEY (person_id, food_id, consumption_date)
# #             )
# #             """
# #         ]

# #         with self.connection.cursor() as cursor:
# #             try:
# #                 # Commence une transaction
# #                 for table_sql in tables:
# #                     cursor.execute(table_sql)
# #                 self.connection.commit()
# #                 logger.info("All tables created successfully")
# #             except Exception as e:
# #                 self.connection.rollback()
# #                 logger.error(f"Error during table creation: {e}")
# #                 raise

# #     def get_cursor(self):
# #         """Retourne un nouveau curseur pour exécuter des requêtes"""
# #         if self.connection.closed:
# #             self._initialize_connection(Config.DB_URL)
# #         return self.connection.cursor()

# #     def close(self):
# #         """Ferme proprement la connexion"""
# #         if hasattr(self, 'connection') and not self.connection.closed:
# #             self.connection.close()
# #             logger.info("Database connection closed")

# #     def __enter__(self):
# #         """Permet l'utilisation en contexte with"""
# #         return self

# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         """Ferme la connexion à la sortie du contexte"""
# #         self.close()

# #     def __del__(self):
# #         """Destructeur qui ferme la connexion"""
# #         self.close()


# # def create_table():
# #     """Fonction utilitaire pour créer les tables"""
# #     try:
# #         db = DatabaseConnection()
# #         logger.info("Tables created successfully")
# #     except Exception as e:
# #         logger.error(f"Failed to create tables: {e}")
# #         raise