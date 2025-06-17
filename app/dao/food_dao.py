
import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor
from typing import Optional, List, Dict, Any
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

class DatabaseConnection:
    _instance = None

    def __new__(cls, db_url: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = psycopg2.connect(db_url, cursor_factory=DictCursor)
        return cls._instance

    def get_cursor(self):
        return self.connection.cursor()





class FoodDAO:
    def __init__(self, connection):
        self.conn = connection

    def create(self, name, description=None, allergy=None, main_image_id=None):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO food (name, description, allergy, main_image_id, created_at)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id_food
            """, (name, description, allergy, main_image_id, datetime.utcnow()))
            id_food = cur.fetchone()[0]
            self.conn.commit()
            return id_food

    def get(self, id_food):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM food WHERE id_food = %s", (id_food,))
            return cur.fetchone()

    def update(self, id_food, **kwargs):
        fields, values = [], []
        for k, v in kwargs.items():
            fields.append(f"{k} = %s")
            values.append(v)
        values.append(id_food)
        set_clause = ", ".join(fields)
        with self.conn.cursor() as cur:
            cur.execute(f"UPDATE food SET {set_clause} WHERE id_food = %s", values)
            self.conn.commit()

    def delete(self, id_food):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM food WHERE id_food = %s", (id_food,))
            self.conn.commit()


class PersonDAO:
    def __init__(self, connection):
        self.conn = connection

    def create(self, name, age=None):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO person (name, age, created_at)
                VALUES (%s, %s, %s)
                RETURNING id_per
            """, (name, age, datetime.utcnow()))
            id_per = cur.fetchone()[0]
            self.conn.commit()
            return id_per

    def get(self, id_per):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM person WHERE id_per = %s", (id_per,))
            return cur.fetchone()

    def update(self, id_per, **kwargs):
        fields, values = [], []
        for k, v in kwargs.items():
            fields.append(f"{k} = %s")
            values.append(v)
        values.append(id_per)
        set_clause = ", ".join(fields)
        with self.conn.cursor() as cur:
            cur.execute(f"UPDATE person SET {set_clause} WHERE id_per = %s", values)
            self.conn.commit()

    def delete(self, id_per):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM person WHERE id_per = %s", (id_per,))
            self.conn.commit()
    def get_all(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM person")
            return cur.fetchall()



class ImageDAO:
    def __init__(self, connection):
        self.conn = connection

    def create(self, url):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO image (url, created_at)
                VALUES (%s, %s)
                RETURNING id_img
            """, (url, datetime.utcnow()))
            id_img = cur.fetchone()[0]
            self.conn.commit()
            return id_img

    def get(self, id_img):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM image WHERE id_img = %s", (id_img,))
            return cur.fetchone()

    def update(self, id_img, **kwargs):
        fields, values = [], []
        for k, v in kwargs.items():
            fields.append(f"{k} = %s")
            values.append(v)
        values.append(id_img)
        set_clause = ", ".join(fields)
        with self.conn.cursor() as cur:
            cur.execute(f"UPDATE image SET {set_clause} WHERE id_img = %s", values)
            self.conn.commit()

    def delete(self, id_img):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM image WHERE id_img = %s", (id_img,))
            self.conn.commit()
    def get_all(self):
         with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM image")
            return cur.fetchall()


class IngredientDAO:
    def __init__(self, connection):
        self.conn = connection

    def create(self, name):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO ingredient (name, created_at)
                VALUES (%s, %s)
                RETURNING id_ing
            """, (name, datetime.utcnow()))
            id_ing = cur.fetchone()[0]
            self.conn.commit()
            return id_ing

    def get(self, id_ing):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM ingredient WHERE id_ing = %s", (id_ing,))
            return cur.fetchone()

    def update(self, id_ing, **kwargs):
        fields, values = [], []
        for k, v in kwargs.items():
            fields.append(f"{k} = %s")
            values.append(v)
        values.append(id_ing)
        set_clause = ", ".join(fields)
        with self.conn.cursor() as cur:
            cur.execute(f"UPDATE ingredient SET {set_clause} WHERE id_ing = %s", values)
            self.conn.commit()

    def delete(self, id_ing):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM ingredient WHERE id_ing = %s", (id_ing,))
            self.conn.commit()
    def get_all(self):
         with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM ingredient")
            return cur.fetchall()


class FoodIngredientDAO:
    def __init__(self, connection):
        self.conn = connection

    def create(self, food_id, ingredient_id, quantity):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO food_ingredient (food_id, ingredient_id, quantity)
                VALUES (%s, %s, %s)
            """, (food_id, ingredient_id, quantity))
            self.conn.commit()

    def get(self, food_id, ingredient_id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT * FROM food_ingredient
                WHERE food_id = %s AND ingredient_id = %s
            """, (food_id, ingredient_id))
            return cur.fetchone()

    def update(self, food_id, ingredient_id, quantity):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE food_ingredient SET quantity = %s
                WHERE food_id = %s AND ingredient_id = %s
            """, (quantity, food_id, ingredient_id))
            self.conn.commit()

    def delete(self, food_id, ingredient_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM food_ingredient WHERE food_id = %s AND ingredient_id = %s
            """, (food_id, ingredient_id))
            self.conn.commit()


class FoodImageDAO:
    def __init__(self, connection):
        self.conn = connection

    def create(self, food_id, image_id, is_primary=False):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO food_image (food_id, image_id, is_primary)
                VALUES (%s, %s, %s)
            """, (food_id, image_id, is_primary))
            self.conn.commit()

    def get(self, food_id, image_id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT * FROM food_image WHERE food_id = %s AND image_id = %s
            """, (food_id, image_id))
            return cur.fetchone()

    def update(self, food_id, image_id, is_primary):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE food_image SET is_primary = %s WHERE food_id = %s AND image_id = %s
            """, (is_primary, food_id, image_id))
            self.conn.commit()

    def delete(self, food_id, image_id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM food_image WHERE food_id = %s AND image_id = %s
            """, (food_id, image_id))
            self.conn.commit()


class PersonFoodDAO:
    def __init__(self, connection):
        self.conn = connection

    def create(self, person_id, food_id, consumption_date=None, quantity=1):
        consumption_date = consumption_date or datetime.utcnow()
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO person_food (person_id, food_id, consumption_date, quantity)
                VALUES (%s, %s, %s, %s)
            """, (person_id, food_id, consumption_date, quantity))
            self.conn.commit()

    def get(self, person_id, food_id, consumption_date):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT * FROM person_food
                WHERE person_id = %s AND food_id = %s AND consumption_date = %s
            """, (person_id, food_id, consumption_date))
            return cur.fetchone()

    def update(self, person_id, food_id, consumption_date, quantity):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE person_food SET quantity = %s
                WHERE person_id = %s AND food_id = %s AND consumption_date = %s
            """, (quantity, person_id, food_id, consumption_date))
            self.conn.commit()

    def delete(self, person_id, food_id, consumption_date):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM person_food
                WHERE person_id = %s AND food_id = %s AND consumption_date = %s
            """, (person_id, food_id, consumption_date))
            self.conn.commit()

# class FoodDAO:
#     def __init__(self, db_url: str):
#         self.db = DatabaseConnection(db_url)

#     def create_food(self, name: str, description: Optional[str] = None,
#                     allergy: Optional[str] = None, main_image_id: Optional[int] = None) -> Dict[str, Any]:
#         query = """
#             INSERT INTO Food (name, description, allergy, main_image_id)
#             VALUES (%s, %s, %s, %s)
#             RETURNING *
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (name, description, allergy, main_image_id))
#             result = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(result)

#     def get_food_by_id(self, food_id: int) -> Optional[Dict[str, Any]]:
#         query = "SELECT * FROM Food WHERE id_food = %s"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (food_id,))
#             result = cursor.fetchone()
#             return dict(result) if result else None

#     def get_all_foods(self) -> List[Dict[str, Any]]:
#         query = "SELECT * FROM Food"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query)
#             return [dict(row) for row in cursor.fetchall()]

#     def update_food(self, food_id: int, **kwargs) -> Optional[Dict[str, Any]]:
#         if not kwargs:
#             return None
#         keys = list(kwargs.keys())
#         values = list(kwargs.values())
#         set_clause = ", ".join(f"{key} = %s" for key in keys)
#         query = f"UPDATE Food SET {set_clause} WHERE id_food = %s RETURNING *"
#         values.append(food_id)
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, values)
#             result = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(result) if result else None

#     def delete_food(self, food_id: int) -> bool:
#         query = "DELETE FROM Food WHERE id_food = %s RETURNING id_food"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (food_id,))
#             deleted = cursor.fetchone() is not None
#             self.db.connection.commit()
#             return deleted


# class PersonDAO:
#     def __init__(self, db_url: str):
#         self.db = DatabaseConnection(db_url)

#     def create_person(self, name: str, age: int) -> Dict[str, Any]:
#         query = "INSERT INTO Person (name, age) VALUES (%s, %s) RETURNING *"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (name, age))
#             result = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(result)

#     def get_person_by_id(self, person_id: int) -> Optional[Dict[str, Any]]:
#         query = "SELECT * FROM Person WHERE id_per = %s"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (person_id,))
#             result = cursor.fetchone()
#             return dict(result) if result else None

#     def get_all_person(self) -> List[Dict[str, Any]]:
#         query = "SELECT * FROM Person"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query)
#             return [dict(row) for row in cursor.fetchall()]

#     def update_person(self, person_id: int, **kwargs) -> Optional[Dict[str, Any]]:
#         if not kwargs:
#             return None
#         keys = list(kwargs.keys())
#         values = list(kwargs.values())
#         set_clause = ", ".join(f"{key} = %s" for key in keys)
#         query = f"UPDATE Person SET {set_clause} WHERE id_per = %s RETURNING *"
#         values.append(person_id)
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, values)
#             result = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(result) if result else None

#     def delete_person(self, person_id: int) -> bool:
#         query = "DELETE FROM Person WHERE id_per = %s RETURNING id_per"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (person_id,))
#             deleted = cursor.fetchone() is not None
#             self.db.connection.commit()
#             return deleted
        



# #class ingrediant

# class IngredientDAO:
#     def __init__(self, db_url: str):
#         self.db = DatabaseConnection(db_url)

#     def create_ingredient(self, name: str, unit: str) -> Dict[str, Any]:
#         query = "INSERT INTO ingredient (name, unit) VALUES (%s, %s) RETURNING *"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (name, unit))
#             result = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(result)

#     def get_ingredient_by_id(self, ingredient_id: int) -> Optional[Dict[str, Any]]:
#         query = "SELECT * FROM ingredient WHERE id = %s"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (ingredient_id,))
#             row = cursor.fetchone()
#             return dict(row) if row else None

#     def get_all_ingredients(self) -> List[Dict[str, Any]]:
#         query = "SELECT * FROM ingredient"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query)
#             return [dict(row) for row in cursor.fetchall()]

#     def update_ingredient(self, ingredient_id: int, **kwargs) -> Optional[Dict[str, Any]]:
#         if not kwargs:
#             return None
#         keys, values = list(kwargs.keys()), list(kwargs.values())
#         set_clause = ", ".join(f"{k} = %s" for k in keys)
#         query = f"UPDATE ingredient SET {set_clause} WHERE id = %s RETURNING *"
#         values.append(ingredient_id)
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, values)
#             row = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(row) if row else None

#     def delete_ingredient(self, ingredient_id: int) -> bool:
#         query = "DELETE FROM ingredient WHERE id = %s RETURNING id"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (ingredient_id,))
#             deleted = cursor.fetchone() is not None
#             self.db.connection.commit()
#             return deleted
        




# #pour image



# class FoodImageDAO:
#     def __init__(self, db_url: str):
#         self.db = DatabaseConnection(db_url)

#     def create_food_image(self, food_id: int, image_id: int, is_primary: bool = False) -> Dict[str, Any]:
#         query = """
#             INSERT INTO food_image (food_id, image_id, is_primary)
#             VALUES (%s, %s, %s) RETURNING *
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (food_id, image_id, is_primary))
#             result = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(result)

#     def get_food_image(self, food_id: int, image_id: int) -> Optional[Dict[str, Any]]:
#         query = "SELECT * FROM food_image WHERE food_id = %s AND image_id = %s"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (food_id, image_id))
#             row = cursor.fetchone()
#             return dict(row) if row else None

#     def update_food_image(self, food_id: int, image_id: int, is_primary: bool) -> Optional[Dict[str, Any]]:
#         query = """
#             UPDATE food_image SET is_primary = %s
#             WHERE food_id = %s AND image_id = %s
#             RETURNING *
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (is_primary, food_id, image_id))
#             row = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(row) if row else None

#     def delete_food_image(self, food_id: int, image_id: int) -> bool:
#         query = "DELETE FROM food_image WHERE food_id = %s AND image_id = %s RETURNING food_id"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (food_id, image_id))
#             deleted = cursor.fetchone() is not None
#             self.db.connection.commit()
#             return deleted




# # food ingr


# class FoodIngredientDAO:
#     def __init__(self, db_url: str):
#         self.db = DatabaseConnection(db_url)

#     def create_food_ingredient(self, food_id: int, ingredient_id: int, quantity: float) -> Dict[str, Any]:
#         query = """
#             INSERT INTO food_ingredient (food_id, ingredient_id, quantity)
#             VALUES (%s, %s, %s) RETURNING *
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (food_id, ingredient_id, quantity))
#             result = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(result)

#     def get_food_ingredient(self, food_id: int, ingredient_id: int) -> Optional[Dict[str, Any]]:
#         query = """
#             SELECT * FROM food_ingredient
#             WHERE food_id = %s AND ingredient_id = %s
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (food_id, ingredient_id))
#             row = cursor.fetchone()
#             return dict(row) if row else None

#     def get_all_food_ingredients(self) -> List[Dict[str, Any]]:
#         query = "SELECT * FROM food_ingredient"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query)
#             return [dict(row) for row in cursor.fetchall()]

#     def update_food_ingredient(self, food_id: int, ingredient_id: int, quantity: float) -> Optional[Dict[str, Any]]:
#         query = """
#             UPDATE food_ingredient
#             SET quantity = %s
#             WHERE food_id = %s AND ingredient_id = %s
#             RETURNING *
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (quantity, food_id, ingredient_id))
#             row = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(row) if row else None

#     def delete_food_ingredient(self, food_id: int, ingredient_id: int) -> bool:
#         query = """
#             DELETE FROM food_ingredient
#             WHERE food_id = %s AND ingredient_id = %s
#             RETURNING food_id
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (food_id, ingredient_id))
#             deleted = cursor.fetchone() is not None
#             self.db.connection.commit()
#             return deleted



# from .db_connection import DatabaseConnection
# from typing import Optional, List, Dict, Any
# from datetime import date

# #pour food perso



# from .db_connection import DatabaseConnection
# from typing import Optional, List, Dict, Any
# from datetime import date
# class PersonFoodDAO:
#     def __init__(self, db_url: str):
#         self.db = DatabaseConnection(db_url)

#     def create_person_food(self, person_id: int, food_id: int, consumption_date: date, quantity: int = 1) -> Dict[str, Any]:
#         query = """
#             INSERT INTO person_food (person_id, food_id, consumption_date, quantity)
#             VALUES (%s, %s, %s, %s) RETURNING *
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (person_id, food_id, consumption_date, quantity))
#             result = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(result)

#     def get_person_food(self, person_id: int, food_id: int, consumption_date: date) -> Optional[Dict[str, Any]]:
#         query = """
#             SELECT * FROM person_food
#             WHERE person_id = %s AND food_id = %s AND consumption_date = %s
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (person_id, food_id, consumption_date))
#             row = cursor.fetchone()
#             return dict(row) if row else None

#     def get_all_person_food(self) -> List[Dict[str, Any]]:
#         query = "SELECT * FROM person_food"
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query)
#             return [dict(row) for row in cursor.fetchall()]

#     def update_person_food(self, person_id: int, food_id: int, consumption_date: date, quantity: int) -> Optional[Dict[str, Any]]:
#         query = """
#             UPDATE person_food
#             SET quantity = %s
#             WHERE person_id = %s AND food_id = %s AND consumption_date = %s
#             RETURNING *
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (quantity, person_id, food_id, consumption_date))
#             row = cursor.fetchone()
#             self.db.connection.commit()
#             return dict(row) if row else None

#     def delete_person_food(self, person_id: int, food_id: int, consumption_date: date) -> bool:
#         query = """
#             DELETE FROM person_food
#             WHERE person_id = %s AND food_id = %s AND consumption_date = %s
#             RETURNING person_id
#         """
#         with self.db.get_cursor() as cursor:
#             cursor.execute(query, (person_id, food_id, consumption_date))
#             deleted = cursor.fetchone() is not None
#             self.db.connection.commit()
#             return deleted


