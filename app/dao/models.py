from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

@dataclass
class Ingredient:
    id_ing: Optional[int]
    name: str
    created_at: Optional[datetime] = None

@dataclass
class Image:
    id_img: Optional[int]
    # food_id: Optional[int]  # nullable ici car pas toujours précisé à la création
    url: str
    created_at: Optional[datetime] = None

@dataclass
class FoodImage:
    image_id: int
    is_primary: bool = False
    


@dataclass
class Food:
    id_food: Optional[int]
    name: str
    description: Optional[str]
    allergy: Optional[str]
    created_at: Optional[datetime] = None
    main_image_id: Optional[int] = None
    images: Optional[List[Image]] = None
    ingredients: Optional[List['FoodIngredient']] = None
    food_images: Optional[List[FoodImage]] = None 

@dataclass
class Person:
    id_per: Optional[int]
    name: str
    age: int
    created_at: Optional[datetime] = None

@dataclass
class FoodIngredient:
    food_id: int
    ingredient_id: int
    quantity: Optional[float] = None

@dataclass
class PersonFood:
    person_id: int
    food_id: int
    consumption_date: Optional[datetime] = None
    quantity: int = 1
