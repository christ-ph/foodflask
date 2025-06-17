

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.database import Base

class Person(Base):
    __tablename__ = 'person'
    
    id_per = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    foods = relationship("Food", secondary="person_food", back_populates="persons")
    
    def to_dict(self):
        return {
            'id_per': self.id_per,
            'name': self.name,
            'age': self.age,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Food(Base):
    __tablename__ = "food"
    
    id_food = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)
    allergy = Column(String(100))
    main_image_id = Column(Integer, ForeignKey('image.id_img'))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    main_image = relationship("Image", foreign_keys=[main_image_id])
    ingredients = relationship("FoodIngredient", back_populates="food")
    images = relationship("FoodImage", back_populates="food")
    persons = relationship("Person", secondary="person_food", back_populates="foods")
    
    def to_dict(self):
        return {
            'id_food': self.id_food,
            'name': self.name,
            'description': self.description,
            'allergy': self.allergy,
            'main_image_id': self.main_image_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'main_image': self.main_image.to_dict() if self.main_image else None
        }

class PersonFood(Base):
    __tablename__ = 'person_food'
    
    person_id = Column(Integer, ForeignKey('person.id_per'), primary_key=True)
    food_id = Column(Integer, ForeignKey('food.id_food'), primary_key=True)
    consumption_date = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Integer, default=1)
    
    def to_dict(self):
        return {
            'person_id': self.person_id,
            'food_id': self.food_id,
            'consumption_date': self.consumption_date.isoformat() if self.consumption_date else None,
            'quantity': self.quantity
        }

class Image(Base):
    __tablename__ = 'image'
    
    id_img = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    food_images = relationship("FoodImage", back_populates="image")
    
    def to_dict(self):
        return {
            'id_img': self.id_img,
            'url': self.url,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Ingredient(Base):
    __tablename__ = 'ingredient'
    
    id_ing = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    food_ingredients = relationship("FoodIngredient", back_populates="ingredient")
    
    def to_dict(self):
        return {
            'id_ing': self.id_ing,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class FoodIngredient(Base):
    __tablename__ = "food_ingredient"
    
    food_id = Column(Integer, ForeignKey("food.id_food"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredient.id_ing"), primary_key=True)
    quantity = Column(Float)

    food = relationship("Food", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="food_ingredients")
    
    def to_dict(self):
        return {
            'food_id': self.food_id,
            'ingredient_id': self.ingredient_id,
            'quantity': self.quantity,
            'ingredient': self.ingredient.to_dict() if self.ingredient else None
        }

class FoodImage(Base):
    __tablename__ = "food_image"
    
    food_id = Column(Integer, ForeignKey("food.id_food"), primary_key=True)
    image_id = Column(Integer, ForeignKey("image.id_img"), primary_key=True)
    is_primary = Column(Boolean, default=False)

    food = relationship("Food", back_populates="images")
    image = relationship("Image", back_populates="food_images")
    
    def to_dict(self):
        return {
            'food_id': self.food_id,
            'image_id': self.image_id,
            'is_primary': self.is_primary,
            'image': self.image.to_dict() if self.image else None
        }