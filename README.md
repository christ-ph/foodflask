
# API de Gestion et d'Analyse Alimentaire

| | |
| :--- | :--- |
| **Réalisé par** | [Dado Christ Pharel] |
| **Matricule** | [23V2256] |
| **Sous la supervision de** | [Dr. Azanzi Jiomekong] |
| **ue** | [INF222] |
| **Année Académique** | [2024-2025] |



## 1. Rapport Complet du Projet

### Objectif Principal
Ce projet a pour but de développer une API RESTful robuste, construite avec **Flask** et **SQLAlchemy**, pour gérer des données relatives à des aliments, des personnes et leur consommation. L'objectif final est de fournir une fonctionnalité clé : un service d'analyse capable d'évaluer les risques d'allergie pour une personne en se basant sur son historique de consommation.

### Architecture de l'Application
L'application suit une architecture en couches, une pratique standard pour garantir la séparation des préoccupations, la maintenabilité et l'évolutivité du code.

-   **Couche Présentation (API)** : Gérée par `app/api/orm_routes.py`, elle expose les endpoints REST pour les interactions client. Elle est responsable de la validation des requêtes HTTP et de la sérialisation des réponses au format JSON.
-   **Couche Logique Métier (Services)** : Située dans `app/services/`, elle contient la logique métier complexe. Le service `AllergyAnalyzer` est au cœur de cette couche, orchestrant les calculs de risque en se basant sur les données de consommation.
-   **Couche d'Accès aux Données (ORM)** : Le dossier `app/orm/` gère toute la communication avec la base de données PostgreSQL.
    -   **`models.py`** : Définit le schéma de la base de données à l'aide de l'ORM **SQLAlchemy**, modélisant les entités (`Food`, `Person`, etc.) et leurs relations complexes (many-to-many).
    -   **`crud.py`** : Centralise les opérations atomiques (Create, Read, Update, Delete) pour chaque modèle, ce qui rend le code des routes plus propre et réutilisable.
-   **Configuration (`app/config.py`)** : Centralise toutes les variables de configuration. Elle est conçue pour lire des variables d'environnement (via un fichier `.env`), ce qui permet une portabilité parfaite entre un environnement de développement local et un déploiement conteneurisé avec Docker.

### Structure du Projet
```
Code_Source/
├── app/
│   ├── __init__.py             # Factory de l'application Flask
│   ├── api/
│   │   └── orm_routes.py       # Définition des routes de l'API
│   ├── config.py               # Fichier de configuration
│   ├── data/
│   │   └── japanese_food_data.json # Données d'initialisation
│   ├── orm/
│   │   ├── crud.py             # Fonctions d'accès à la base (CRUD)
│   │   └── models.py           # Modèles de données SQLAlchemy
│   ├── services/
│   │   ├── allergy_service.py  # Logique métier pour l'analyse des allergies
│   │   └── storage.py          # Script pour peupler la base de données
│   └── utils/
│       ├── database.py         # Configuration de la session SQLAlchemy
│       └── init_db.py          # Script pour créer les tables
├── .env.example                # Fichier d'exemple pour la configuration
├── requirements.txt            # Dépendances Python
└── run.py                      # Point d'entrée pour lancer l'application
```

---

## 2. Instructions d'Installation et d'Exécution

Suivez ces étapes pour mettre en place et lancer le projet sur votre machine locale.

### Prérequis
-   Python 3.10 ou une version supérieure
-   `pip` (le gestionnaire de paquets de Python)
-   Un serveur de base de données **PostgreSQL** en cours d'exécution.

### Étape 1 : Préparation de l'Environnement
1.  Ouvrez un terminal et naviguez jusqu'au dossier `Code_Source`.

2.  Il est fortement recommandé de créer et d'activer un environnement virtuel pour isoler les dépendances :
    ```bash
    # Créer l'environnement
    python -m venv venv

    # Activer l'environnement
    # Sur Windows: venv\Scripts\activate
    # Sur macOS/Linux: source venv/bin/activate
    ```

### Étape 2 : Installation des Dépendances
Installez toutes les bibliothèques Python requises en une seule commande :
```bash
pip install -r requirements.txt
```

### Étape 3 : Configuration de la Base de Données
1.  Créez un fichier nommé `.env` à la racine du dossier `Code_Source`.

2.  Copiez-y le contenu ci-dessous et remplacez les valeurs par celles de votre configuration PostgreSQL locale.
    ```env
    # Fichier: Code_Source/.env
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=foods
    DB_USER=christ
    DB_PASSWORD=123456
    ```
    *Assurez-vous que la base de données (`foods` ou le nom que vous avez choisi) existe bien sur votre serveur PostgreSQL.*

### Étape 4 : Lancement de l'Application
Lancez le serveur de développement Flask avec la commande suivante :
```bash
python run.py
```
Ce script effectuera les actions suivantes au démarrage :
1.  **Création des tables** : Le schéma de la base de données sera créé s'il n'existe pas.
2.  **Démarrage du serveur** : Le serveur web sera lancé et accessible.

L'API devrait être en cours d'exécution à l'adresse **`http://127.0.0.1:5000`**.

### Étape 5 (Optionnelle) : Peuplement de la Base de Données
Pour remplir la base de données avec des données d'exemple, ouvrez un **nouveau terminal** (en gardant le serveur en cours d'exécution dans le premier) et exécutez la commande suivante :
```bash
python -m app.services.storage
```
Vous verrez des messages confirmant que les données ont bien été insérées.

---

## 3. Documentation de l'API

Tous les endpoints sont préfixés par `/api`. L'URL de base pour les tests locaux est `http://127.0.0.1:5000`.

### Endpoint d'Analyse d'Allergie (Fonctionnalité Clé)

| Méthode | URL                                         | Description                                    |
| :------ | :------------------------------------------ | :--------------------------------------------- |
| `GET`   | `/api/persons/<int:person_id>/allergy-analysis` | Analyse le risque allergique pour une personne. |

**Exemple de test :**
```bash
curl http://127.0.0.1:5000/api/persons/4/allergy-analysis
```

---

### Endpoints `Food`

| Méthode | URL                   | Description                       |
| :------ | :-------------------- | :-------------------------------- |
| `GET`   | `/api/foods`          | Récupère la liste de tous les plats. |
| `GET`   | `/api/foods/<int:id>` | Récupère un plat spécifique.      |
| `POST`  | `/api/foods`          | Crée un nouveau plat.             |
| `PUT`   | `/api/foods/<int:id>` | Met à jour un plat existant.      |
| `DELETE`| `/api/foods/<int:id>` | Supprime un plat.                 |

**Exemples d'utilisation :**
-   **GET** un plat spécifique :
    ```bash
    curl http://127.0.0.1:5000/api/foods/1
    ```
-   **POST** un nouveau plat :
    ```bash
    curl -X POST http://127.0.0.1:5000/api/foods \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Miso Soup",
        "description": "Traditional Japanese soup.",
        "allergy": "Soja",
        "main_image_id": 1
    }'
    ```

---

### Endpoints `Person`

| Méthode | URL                    | Description                      |
| :------ | :--------------------- | :------------------------------- |
| `GET`   | `/api/persons`         | Récupère la liste des personnes. |
| `GET`   | `/api/persons/<int:id>`| Récupère une personne spécifique.|
| `POST`  | `/api/persons`         | Crée une nouvelle personne.      |
| `PUT`   | `/api/persons/<int:id>`| Met à jour une personne.         |
| `DELETE`| `/api/persons/<int:id>`| Supprime une personne.           |

**Exemples d'utilisation :**
-   **GET** une personne spécifique :
    ```bash
    curl http://127.0.0.1:5000/api/persons/1
    ```
-   **POST** une nouvelle personne :
    ```bash
    curl -X POST http://127.0.0.1:5000/api/persons \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Yuki Tanaka",
        "age": 25
    }'
    ```
---

### Endpoints `Ingredient`

| Méthode | URL                       | Description                          |
| :------ | :------------------------ | :----------------------------------- |
| `GET`   | `/api/ingredients`        | Récupère tous les ingrédients.       |
| `GET`   | `/api/ingredients/<int:id>` | Récupère un ingrédient spécifique.   |
| `POST`  | `/api/ingredients`        | Crée un nouvel ingrédient.           |
| `PUT`   | `/api/ingredients/<int:id>` | Met à jour un ingrédient.            |
| `DELETE`| `/api/ingredients/<int:id>` | Supprime un ingrédient.              |

**Exemples d'utilisation :**
-   **GET** un ingrédient spécifique :
    ```bash
    curl http://127.0.0.1:5000/api/ingredients/1
    ```
-   **POST** un nouvel ingrédient :
    ```bash
    curl -X POST http://127.0.0.1:5000/api/ingredients \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Tofu"
    }'
    ```
---

### Endpoints `Image`

| Méthode | URL                   | Description                          |
| :------ | :-------------------- | :----------------------------------- |
| `GET`   | `/api/images`         | Récupère toutes les images.          |
| `GET`   | `/api/images/<int:id>`| Récupère une image spécifique.       |
| `POST`  | `/api/images`         | Crée une nouvelle référence d'image. |
| `PUT`   | `/api/images/<int:id>`| Met à jour une image.                |
| `DELETE`| `/api/images/<int:id>`| Supprime une image.                  |

**Exemples d'utilisation :**
-   **GET** une image spécifique :
    ```bash
    curl http://127.0.0.1:5000/api/images/1
    ```
-   **POST** une nouvelle image :
    ```bash
    curl -X POST http://127.0.0.1:5000/api/images \
    -H "Content-Type: application/json" \
    -d '{
        "url": "/media/new_image.jpg"
    }'
    ```
```