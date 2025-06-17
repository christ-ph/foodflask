from flask import Blueprint

bp = Blueprint('dao', __name__)

@bp.route('/')
def home():
    return "Hello from DAO"
