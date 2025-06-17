from app.utils.database import Base, engine
from app.orm import models as orm_models

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Toutes les tables ont été créées avec succès.")

