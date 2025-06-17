

import json
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.orm.models import *
from app.config import Config  

# Créer la session
engine = create_engine(Config.DB_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Charger le JSON
with open('app/data/japanese_food_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

try:
    # Insert Images
    image_map = {}
    for idx, img in enumerate(data['images'], start=1):
        existing_image = session.query(Image).filter_by(url=img['url']).first()
        if existing_image:
            image_map[idx] = existing_image.id_img
            continue

        image = Image(
            url=img['url']
        )
        session.add(image)
        session.flush()  # pour obtenir image.id_img
        image_map[idx] = image.id_img
    
    session.commit()

    # Insert Foods
    food_map = {}
    for idx, f in enumerate(data['foods'], start=1):
        existing_food = session.query(Food).filter_by(name=f['name']).first()
        if existing_food:
            food_map[idx] = existing_food.id_food
            continue

        food = Food(
            name=f['name'],
            description=f['description'],
            allergy=f['allergy'],
            main_image_id=image_map[f['main_image_id']]
        )
        session.add(food)
        session.flush()
        food_map[idx] = food.id_food
    
    session.commit()

    # Insert Ingredients
    ingredient_map = {}
    for idx, ing in enumerate(data['ingredients'], start=1):
        existing_ingredient = session.query(Ingredient).filter_by(name=ing['name']).first()
        if existing_ingredient:
            ingredient_map[idx] = existing_ingredient.id_ing
            continue

        ingredient = Ingredient(
            name=ing['name']
        )
        session.add(ingredient)
        session.flush()
        ingredient_map[idx] = ingredient.id_ing
    
    session.commit()

    # Insert FoodIngredient associations
    for fi in data['food_ingredients']:
        existing_fi = session.query(FoodIngredient).filter_by(
            food_id=food_map[fi['food_id']],
            ingredient_id=ingredient_map[fi['ingredient_id']]
        ).first()
        if existing_fi:
            continue

        food_ingredient = FoodIngredient(
            food_id=food_map[fi['food_id']],
            ingredient_id=ingredient_map[fi['ingredient_id']],
            quantity=fi['quantity']
        )
        session.add(food_ingredient)
    
    session.commit()

    # Insert FoodImage associations
    for fi in data['food_images']:
        existing_fimg = session.query(FoodImage).filter_by(
            food_id=food_map[fi['food_id']],
            image_id=image_map[fi['image_id']]
        ).first()
        if existing_fimg:
            continue

        food_image = FoodImage(
            food_id=food_map[fi['food_id']],
            image_id=image_map[fi['image_id']],
            is_primary=fi['is_primary']
        )
        session.add(food_image)
    
    session.commit()

    # Insert Persons
    person_map = {}
    for idx, p in enumerate(data['persons'], start=1):
        existing_person = session.query(Person).filter_by(name=p['name'], age=p['age']).first()
        if existing_person:
            person_map[idx] = existing_person.id_per
            continue

        person = Person(
            name=p['name'],
            age=p['age']
        )
        session.add(person)
        session.flush()
        person_map[idx] = person.id_per
    
    session.commit()

    # Insert PersonFood associations
    for pf in data['person_food']:
        existing_pf = session.query(PersonFood).filter_by(
            person_id=person_map[pf['person_id']],
            food_id=food_map[pf['food_id']]
        ).first()
        if existing_pf:
            continue

        person_food = PersonFood(
            person_id=person_map[pf['person_id']],
            food_id=food_map[pf['food_id']],
            # consumption_date=datetime.fromisoformat(pf['consumption_date']),  # à activer si présent
            consumption_date=datetime.now(),  # fallback pour test
            quantity=pf['quantity']
        )
        session.add(person_food)
    
    session.commit()

    print("✅ Insertion terminée avec succès ! (Pas de doublons)")

except Exception as e:
    session.rollback()
    print(f"❌ Erreur : {e}")

finally:
    session.close()





























# import json
# from datetime import datetime
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from app.orm.models import *
# from app.config import Config  

# # Créer la session
# engine = create_engine(Config.DB_URL)
# SessionLocal = sessionmaker(bind=engine)
# session = SessionLocal()

# # Charger le JSON
# with open('app/data/japanese_food_data.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# try:
#     # Insert Images
#     image_map = {}
#     for idx, img in enumerate(data['images'], start=1):
#         image = Image(
#             url=img['url']
#         )
#         session.add(image)
#         session.flush()  # pour obtenir image.id_img
#         image_map[idx] = image.id_img  # on mappe l'index logique → id réel
    
#     session.commit()

#     # Insert Foods
#     food_map = {}
#     for idx, f in enumerate(data['foods'], start=1):
#         food = Food(
#             name=f['name'],
#             description=f['description'],
#             allergy=f['allergy'],
#             main_image_id=image_map[f['main_image_id']]  # ici on remappe avec le vrai id_img
#         )
#         session.add(food)
#         session.flush()
#         food_map[idx] = food.id_food
    
#     session.commit()

#     # Insert Ingredients
#     ingredient_map = {}
#     for idx, ing in enumerate(data['ingredients'], start=1):
#         ingredient = Ingredient(
#             name=ing['name']
#         )
#         session.add(ingredient)
#         session.flush()
#         ingredient_map[idx] = ingredient.id_ing
    
#     session.commit()

#     # Insert FoodIngredient associations
#     for fi in data['food_ingredients']:
#         food_ingredient = FoodIngredient(
#             food_id=food_map[fi['food_id']],  # on remappe l'id réel
#             ingredient_id=ingredient_map[fi['ingredient_id']],  # idem
#             quantity=fi['quantity']
#         )
#         session.add(food_ingredient)
    
#     session.commit()

#     # Insert FoodImage associations
#     for fi in data['food_images']:
#         food_image = FoodImage(
#             food_id=food_map[fi['food_id']],  # remap id réel
#             image_id=image_map[fi['image_id']],  # remap id réel
#             is_primary=fi['is_primary']
#         )
#         session.add(food_image)
    
#     session.commit()

#     # Insert Persons
#     person_map = {}
#     for idx, p in enumerate(data['persons'], start=1):
#         person = Person(
#             name=p['name'],
#             age=p['age']
#         )
#         session.add(person)
#         session.flush()
#         person_map[idx] = person.id_per
    
#     session.commit()

#     # Insert PersonFood associations
#     for pf in data['person_food']:
#         person_food = PersonFood(
#             person_id=person_map[pf['person_id']],  # remap id réel
#             food_id=food_map[pf['food_id']],  # remap id réel
#             # consumption_date=datetime.fromisoformat(pf['consumption_date']),
#             quantity=pf['quantity']
#         )
#         session.add(person_food)
    
#     session.commit()

#     print("✅ Insertion terminée avec succès !")

# except Exception as e:
#     session.rollback()
#     print(f"❌ Erreur : {e}")

# finally:
#     session.close()








# import json
# from datetime import datetime
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from app.orm.models import *
# from app.config import Config  

# # Créer la session
# engine = create_engine(Config.DB_URL)
# SessionLocal = sessionmaker(bind=engine)
# session = SessionLocal()

# # Charger le JSON
# with open('app/data/japanese_food_data.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# try:
#     # Insert Images
#     image_map = {}
#     for img in data['images']:
#         image = Image(
#             # id_img=img['id_img'],
#             url=img['url'],
#             # created_at=datetime.fromisoformat(img['created_at'])
#         )
#         session.add(image)
#         image_map[image.id_img] = image
    
#     session.commit()

#     # Insert Foods
#     food_map = {}
#     for f in data['foods']:
#         food = Food(
#             # id_food=f['id_food'],
#             name=f['name'],
#             description=f['description'],
#             allergy=f['allergy'],
#             main_image_id=f['main_image_id'],
#             # created_at=datetime.fromisoformat(f['created_at'])
#         )
#         session.add(food)
#         food_map[food.id_food] = food
    
#     session.commit()

#     # Insert Ingredients
#     ingredient_map = {}
#     for ing in data['ingredients']:
#         ingredient = Ingredient(
#             # id_ing=ing['id_ing'],
#             name=ing['name'],
#             # created_at=datetime.fromisoformat(ing['created_at'])
#         )
#         session.add(ingredient)
#         ingredient_map[ingredient.id_ing] = ingredient
    
#     session.commit()

#     # Insert FoodIngredient associations
#     for fi in data['food_ingredients']:
#         food_ingredient = FoodIngredient(
#             food_id=fi['food_id'],
#             ingredient_id=fi['ingredient_id'],
#             quantity=fi['quantity']
#         )
#         session.add(food_ingredient)
    
#     session.commit()

#     # Insert FoodImage associations
#     for fi in data['food_images']:
#         food_image = FoodImage(
#             food_id=fi['food_id'],
#             image_id=fi['image_id'],
#             is_primary=fi['is_primary']
#         )
#         session.add(food_image)
    
#     session.commit()

#     # Insert Persons
#     person_map = {}
#     for p in data['persons']:
#         person = Person(
#             # id_per=p['id_per'],
#             name=p['name'],
#             age=p['age'],
#             # created_at=datetime.fromisoformat(p['created_at'])
#         )
#         session.add(person)
#         person_map[person.id_per] = person
    
#     session.commit()

#     # Insert PersonFood associations
#     for pf in data['person_food']:
#         person_food = PersonFood(
#             person_id=pf['person_id'],
#             food_id=pf['food_id'],
#             consumption_date=datetime.fromisoformat(pf['consumption_date']),
#             quantity=pf['quantity']
#         )
#         session.add(person_food)
    
#     session.commit()

#     print("✅ Insertion terminée avec succès !")

# except Exception as e:
#     session.rollback()
#     print(f"❌ Erreur : {e}")

# finally:
#     session.close()
