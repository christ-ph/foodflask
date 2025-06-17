

from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialisation DB
    from .utils.database import init_db
    init_db()
    
    # Enregistrement des blueprints
    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

# from flask import Flask
# from .config import Config
# from .utils.database import init_db

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
    
#     # Initialisation DB
#     with app.app_context():
#         init_db()
    
#     # Enregistrement des blueprints
#     from .api import bp as api_blueprint
#     app.register_blueprint(api_blueprint, url_prefix='/orm' )
    
#     return app


# from flask import Flask
# from .config import Config
# from .utils.database import init_db

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
    
#     # Initialisation de la DB
#     with app.app_context():
#         init_db()
    
#     # Enregistrement des blueprints
#     from .api import bp as api_blueprint
#     app.register_blueprint(api_blueprint)
    
#     @app.teardown_appcontext
#     def shutdown_session(exception=None):
#         from .utils.database import db
#         db.remove()
    
#     return app




# from flask import Flask
# from .config import Config
# from .utils.database import init_db

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
    
#     # Initialisation de la DB
#     with app.app_context():
#         init_db()
    
#     # Enregistrement des blueprints
#     from .api import bp as api_blueprint
#     app.register_blueprint(api_blueprint)
    
#     @app.teardown_appcontext
#     def shutdown_session(exception=None):
#         from .utils.database import db_session
#         db_session.remove()
    
#     return app


# def register_blueprints(app):
#     """Enregistre tous les blueprints"""
#     from .api.dao_routes import bp as dao_bp
#     from .api.orm_routes import bp as orm_bp
    
#     app.register_blueprint(dao_bp, url_prefix='/dao')
#     app.register_blueprint(orm_bp, url_prefix='/orm')











# from flask import Flask
# from .config import Config
# from app.utils.database import get_db_session, Base
# db = get_db_session()

# # Création de l'application Flask
# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
    
#     # Initialisation des extensions (DB, etc.)
#     init_extensions(app)
    
#     # Enregistrement des blueprints
#     register_blueprints(app)
    
#     return app






# # from flask import Blueprint
# # from flask import Flask
# # from .config import Config

# # # Blueprint principal
# # api_bp = Blueprint('api', __name__)
# # app = Flask(__name__)
# # app.config.from_object(Config)

# # # importation des routes
# # from .api import dao_routes,orm_routes
# # app.register_blueprint(dao_routes.bp,url_prefix = '/dao')
# # app.register_blueprint(orm_routes.bp,url_prefix = '/orm')
