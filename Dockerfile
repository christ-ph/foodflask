

FROM python:3.10-slim




WORKDIR /app

COPY requirements.txt .

# RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000

CMD ["python", "run.py"]




#  Dockerfile

# FROM python:3.10-slim

# # Installer les dépendances système
# RUN apt-get update && apt-get install -y \
#     libpq-dev gcc curl && \
#     apt-get clean

# # Créer le dossier de l'app
# WORKDIR /app

# # Copier les fichiers
# COPY . /app

# # Installer les dépendances Python
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# # Créer dossier des médias s'il n'existe pas
# RUN mkdir -p /app/uploads/images

# # Exposer le port
# EXPOSE 5000

# # Commande de lancement
# CMD ["python", "run.py"]
