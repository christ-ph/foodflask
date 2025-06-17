from flask import Blueprint

# bp = Blueprint('api', __name__)
api_bp = Blueprint('api', __name__)
# Import APRÈS la création du blueprint
from . import orm_routes



# from flask import Blueprint

# # Blueprint principal
# bp = Blueprint('orm', __name__)

# # Import des routes (à faire APRÈS la création du blueprint)
# from . import orm_routes, dao_routes




# from flask import Blueprint

# # Blueprint principal
# api_bp = Blueprint('api', __name__)

# # Import des routes (à faire APRÈS la création du blueprint)
# from . import orm_routes, dao_routes