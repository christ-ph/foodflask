from flask import Blueprint, request, jsonify
from sqlalchemy import func
from ..orm.models import *
from ..orm.crud import *
from ..utils.database import db_session
from . import api_bp 
from app.services.allergy_service import AllergyAnalyzer


# bp = Blueprint('orm', __name__)



@api_bp.route('/test')
def test():
    return jsonify({"status": "working"}), 200


# ==================== FOOD ROUTES ====================
@api_bp.route('/foods', methods=['GET'])
# @api_bp.route('/foods', methods=['GET'])
# def get_foods():
#     foods = get_all_food()
#     return jsonify([food.to_dict() for food in foods])

def get_foods():
    try:
        foods = get_all_food()
        return jsonify([{
            'id_food': food.id_food,
            'name': food.name,
            'description': food.description
        } for food in foods])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/food', methods=['POST'])
def create_food_route():
    data = request.get_json()
    food = create_food(
        name=data['name'],
        description=data.get('description', ''),
        allergy=data.get('allergy', ''),
        main_image_id=data.get('main_image_id')
    )
    return jsonify(food.to_dict()), 201

@api_bp.route('/foods/<int:food_id>', methods=['GET'])
def get_food_route(food_id):
    food = get_food_by_id(food_id)
    if not food:
        return jsonify({'error': 'Food not found'}), 404
    return jsonify(food.to_dict())

@api_bp.route('/foods', methods=['GET'])
def get_all_foods_route():
    foods = get_all_food()
    return jsonify([food.to_dict() for food in foods])

@api_bp.route('/foods/<int:food_id>', methods=['PUT'])
def update_food_route(food_id):
    data = request.get_json()
    food = update_food(
        food_id,
        name=data.get('name'),
        description=data.get('description'),
        allergy=data.get('allergy'),
        main_image_id=data.get('main_image_id')
    )
    if not food:
        return jsonify({'error': 'Food not found'}), 404
    return jsonify(food.to_dict())

@api_bp.route('/foods/<int:food_id>', methods=['DELETE'])
def delete_food_route(food_id):
    if not delete_food(food_id):
        return jsonify({'error': 'Food not found'}), 404
    return jsonify({'message': 'Food deleted successfully'}), 200

# ==================== PERSON ROUTES ====================
@api_bp.route('/persons', methods=['POST'])
def create_persons():
    data = request.get_json()
    person = create_person(
        name=data['name'],
        age=data['age']
    )
    return jsonify(person.to_dict()), 201

@api_bp.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = get_person_by_id(person_id)
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify(person.to_dict())

@api_bp.route('/persons', methods=['GET'])
def get_all_persons():
    persons = get_all_person()
    return jsonify([person.to_dict() for person in persons])

@api_bp.route('/persons/<int:person_id>', methods=['PUT'])
def update_persons(person_id):
    data = request.get_json()
    person = update_person(
        person_id,
        name=data.get('name'),
        age=data.get('age')
    )
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    return jsonify(person.to_dict())

@api_bp.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_persons(person_id):
    if not delete_person(person_id):
        return jsonify({'error': 'Person not found'}), 404
    return jsonify({'message': 'Person deleted successfully'}), 200


# ==================== IMAGE ROUTES ====================
@api_bp.route('/images', methods=['POST'])
def create_images():
    data = request.get_json()
    image = create_image(url=data['url'])
    return jsonify(image.to_dict()), 201

@api_bp.route('/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
    image = get_image_by_id(image_id)
    if not image:
        return jsonify({'error': 'Image not found'}), 404
    return jsonify(image.to_dict())

@api_bp.route('/images', methods=['GET'])
def get_all_image():
    images = get_all_images()
    return jsonify([image.to_dict() for image in images])

@api_bp.route('/images/<int:image_id>', methods=['PUT'])
def update_images(image_id):
    data = request.get_json()
    image = update_image(image_id, url=data.get('url'))
    if not image:
        return jsonify({'error': 'Image not found'}), 404
    return jsonify(image.to_dict())

@api_bp.route('/images/<int:image_id>', methods=['DELETE'])
def delete_images(image_id):
    if not delete_image(image_id):
        return jsonify({'error': 'Image not found'}), 404
    return jsonify({'message': 'Image deleted successfully'}), 200

# ==================== INGREDIENT ROUTES ====================
@api_bp.route('/ingredients', methods=['POST'])
def create_ingredients():
    data = request.get_json()
    ingredient = create_ingredient(
        name=data['name'],
        unit=data.get('unit', 'g')
    )
    return jsonify(ingredient.to_dict()), 201

@api_bp.route('/ingredients/<int:ingredient_id>', methods=['GET'])
def get_ingredient(ingredient_id):
    ingredient = get_ingredient_by_id(ingredient_id)
    if not ingredient:
        return jsonify({'error': 'Ingredient not found'}), 404
    return jsonify(ingredient.to_dict())

@api_bp.route('/ingredients', methods=['GET'])
def get_all_ingredients():
    ingredients = get_all_ingredient()
    return jsonify([ingredient.to_dict() for ingredient in ingredients])

@api_bp.route('/ingredients/<int:ingredient_id>', methods=['PUT'])
def update_ingredients(ingredient_id):
    data = request.get_json()
    ingredient = update_ingredient(
        ingredient_id,
        name=data.get('name'),
        unit=data.get('unit')
    )
    if not ingredient:
        return jsonify({'error': 'Ingredient not found'}), 404
    return jsonify(ingredient.to_dict())

@api_bp.route('/ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredients(ingredient_id):
    if not delete_ingredient(ingredient_id):
        return jsonify({'error': 'Ingredient not found'}), 404
    return jsonify({'message': 'Ingredient deleted successfully'}), 200



# ==================== FOOD INGREDIENT ROUTES ====================
@api_bp.route('/food-ingredients', methods=['POST'])
def create_food_ingredients():
    data = request.get_json()
    link = create_food_ingredient(
        food_id=data['food_id'],
        ingredient_id=data['ingredient_id'],
        quantity=data['quantity']
    )
    return jsonify(link.to_dict()), 201

@api_bp.route('/food-ingredients/<int:food_id>/<int:ingredient_id>', methods=['GET'])
def get_food_ingredients(food_id, ingredient_id):
    link = get_food_ingredient(food_id, ingredient_id)
    if not link:
        return jsonify({'error': 'Food-Ingredient link not found'}), 404
    return jsonify(link.to_dict())

@api_bp.route('/food-ingredients/<int:food_id>/<int:ingredient_id>', methods=['DELETE'])
def delete_food_ingredients(food_id, ingredient_id):
    if not delete_food_ingredient(food_id, ingredient_id):
        return jsonify({'error': 'Food-Ingredient link not found'}), 404
    return jsonify({'message': 'Link deleted successfully'}), 200



# ==================== PERSON FOOD ROUTES ====================
@api_bp.route('/person-foods', methods=['POST'])
def create_person_food():
    data = request.get_json()
    pf = create_person_food(
        person_id=data['person_id'],
        food_id=data['food_id'],
        consumption_date=data['consumption_date'],
        quantity=data.get('quantity', 1)
    )
    return jsonify(pf.to_dict()), 201

# @api_bp.route('/person-foods/<int:person_id>/<int:food_id>', methods=['GET'])
# def get_person_foods(person_id, food_id, desired_date):
#     record = db_session.query(PersonFood).filter(
#         PersonFood.person_id == person_id,
#         PersonFood.food_id == food_id,
#     ).first()

#     if not record:
#         return { "error": "Consumption record not found" }

#     return record.to_dict()
# # def get_person_foods(person_id, food_id):
#     pf = get_person_food(person_id, food_id)
#     # if not pf:
#     #     return jsonify({'error': 'Consumption record not found'}), 404
#     return jsonify(pf.to_dict()['quantity'])

@api_bp.route('/person-foods/<int:person_id>/<int:food_id>', methods=['DELETE'])
def delete_person_foods(person_id, food_id):
    if not delete_person_food(person_id, food_id):
        return jsonify({'error': 'Consumption record not found'}), 404
    return jsonify({'message': 'Record deleted successfully'}), 200



@api_bp.route('/persons/<int:person_id>/allergy-analysis', methods=['GET'])
def analyze_person_allergy(person_id):
    try:
        # Flask utilise db_session au lieu de Session de FastAPI
        result = AllergyAnalyzer.analyze_allergy_risk(db_session, person_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400