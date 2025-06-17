from app.config import Config
# from app.dao.food_dao import FoodDAO
from app.orm.crud import get_all_foods


# class FoodsServices:
#     @staticmethod
#     def get_all():
#         return get_all_foods() if Config.MODE == 'ORM' else FoodDAO.get_all()
    