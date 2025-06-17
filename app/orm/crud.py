from .models import Food ,Person,Image,Ingredient,FoodImage,FoodIngredient,PersonFood
from app.utils.database import SessionLocal
from app.utils.database import db_session

from sqlalchemy.exc import SQLAlchemyError



# operation grud pour les foods
def create_food(name,description,allergy,main_image_id=None):
    new_food = Food(name=name,description=description,allergy=allergy,main_image_id=main_image_id)
    db_session.add(new_food)
    db_session.commit()
    return new_food

def get_food_by_id(food_id):
    return db_session.query(Food).get(food_id)

def get_all_food():
    return db_session.query(Food).all()

def update_food(food_id,**kwargs):
    food= get_food_by_id(food_id)
    if not food:
        for key ,value in kwargs.items():
            setattr(food,key,value)
        db_session.commit()
        return food


def delete_food(food_id):
    food = db_session.query(Food).get(food_id)
    if food:
        # Supprime d'abord tous ses ingrédients
        db_session.query(FoodIngredient).filter(FoodIngredient.food_id == food_id).delete()
        # Maintenant, vous pouvez supprimer le Food
        db_session.delete(food)
        db_session.commit()
        return True
    return False
# def delete_food(db_session, food_id):
#     food = get_food_by_id(food_id)
#     if food:
#         db_session.delete(food)
#         db_session.commit()

#     return food



# operation grud pour les persons

def create_person(name,age):
    new_person = Person(name=name,age=age)
    db_session.add(new_person)
    db_session.commit()
    return new_person

def get_person_by_id(per_id):
    return db_session.query(Person).get(per_id)

def get_all_person():
    return db_session.query(Person).all()

def update_person(person_id, **kwargs):
    person = get_person_by_id(person_id)
    if not person:
        return None
    for key, value in kwargs.items():
        setattr(person, key, value)
    db_session.commit()
    return person

def delete_person(person_id):
    person = get_person_by_id(person_id)
    if person:
        db_session.delete(person)
        db_session.commit()
    return person


# operation grud pour les images

def create_image(url):
    image = Image(url=url)
    db_session.add(image)
    db_session.commit()
    return image

def get_image_by_id(image_id):
    return db_session.query(Image).get(image_id)

def get_all_images():
    return db_session.query(Image).all()

def update_image(image_id, **kwargs):
    image = get_image_by_id(image_id)
    if not image:
        return None
    for key, value in kwargs.items():
        setattr(image, key, value)
    db_session.commit()
    return image

def delete_image(image_id):
    image = get_image_by_id(image_id)
    if image:
        db_session.delete(image)
        db_session.commit()
    return image


# operation grud pour les ingredient


def create_food_ingredient(food_id, ingredient_id, quantity):
    link = FoodIngredient(food_id=food_id, ingredient_id=ingredient_id, quantity=quantity)
    db_session.add(link)
    db_session.commit()
    return link

def get_food_ingredient(food_id, ingredient_id):
    return db_session.query(FoodIngredient).get((food_id, ingredient_id))

def get_all_food_ingredient():
    return db_session.query(FoodIngredient).all()

def update_food_ingredient(food_id, ingredient_id, quantity):
    link = get_food_ingredient(food_id, ingredient_id)
    if not link:
        return None
    link.quantity = quantity
    db_session.commit()
    return link

def delete_food_ingredient(food_id, ingredient_id):
    link = get_food_ingredient(food_id, ingredient_id)
    if link:
        db_session.delete(link)
        db_session.commit()
    return link

def get_ingredient_by_id(ingredient_id):
    return db_session.query(Ingredient).get(ingredient_id)

# operation grud pour les foodimage

def create_food_image(food_id, image_id, is_primary=False):
    link = FoodImage(food_id=food_id, image_id=image_id, is_primary=is_primary)
    db_session.add(link)
    db_session.commit()
    return link

def get_food_image(food_id, image_id):
    return db_session.query(FoodImage).get((food_id, image_id))

def get_all_food_images():
    return db_session.query(FoodImage).all()

def update_food_image(food_id, image_id, is_primary):
    link = get_food_image(food_id, image_id)
    if not link:
        return None
    link.is_primary = is_primary
    db_session.commit()
    return link

def delete_food_image(food_id, image_id):
    link = get_food_image(food_id, image_id)
    if link:
        db_session.delete(link)
        db_session.commit()
    return link



# operation grud pour les persons nouritue

def create_person_food(person_id, food_id, consumption_date, quantity=1):
    pf = PersonFood(person_id=person_id, food_id=food_id, consumption_date=consumption_date, quantity=quantity)
    db_session.add(pf)
    db_session.commit()
    return pf

def get_person_food(person_id, food_id):
    return db_session.query(PersonFood).get((person_id, food_id))

def get_all_person_food():
    return db_session.query(PersonFood).all()

def update_person_food(person_id, food_id,quantity):
    pf = get_person_food(person_id, food_id)
    if not pf:
        return None
    pf.quantity = quantity
    db_session.commit()
    return pf

def delete_person_food(person_id, food_id):
    pf = get_person_food(person_id, food_id)
    if pf:
        db_session.delete(pf)
        db_session.commit()
    return pf


def create_ingredient(name: str):
    """Crée un nouvel ingrédient"""
    try:
        new_ingredient = Ingredient(name=name)
        db_session.add(new_ingredient)
        db_session.commit()
        return new_ingredient
    except SQLAlchemyError as e:
        db_session.rollback()
        raise e

def get_ingredient_by_id(ingredient_id: int):
    """Récupère un ingrédient par son ID"""
    return db_session.query(Ingredient).get(ingredient_id)

def get_all_ingredient():
    """Récupère tous les ingrédients"""
    return db_session.query(Ingredient).all()

def update_ingredient(ingredient_id: int, **kwargs):
    """Met à jour un ingrédient"""
    try:
        ingredient = db_session.query(Ingredient).get(ingredient_id)
        if not ingredient:
            return None
            
        for key, value in kwargs.items():
            setattr(ingredient, key, value)
            
        db_session.commit()
        return ingredient
    except SQLAlchemyError as e:
        db_session.rollback()
        raise e

def delete_ingredient(ingredient_id: int):
    """Supprime un ingrédient"""
    try:
        ingredient = db_session.query(Ingredient).get(ingredient_id)
        if not ingredient:
            return False
            
        db_session.delete(ingredient)
        db_session.commit()
        return True
    except SQLAlchemyError as e:
        db_session.rollback()
        raise e





