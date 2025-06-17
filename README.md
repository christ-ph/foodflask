# API de Gestion Alimentaire

Il s'agit d'une API RESTful développée avec **Flask** et **SQLAlchemy** pour gérer des données relatives à des aliments, des personnes et leur consommation. L'application met en place un modèle de données relationnel complet et expose des endpoints pour interagir avec ces données.

Une fonctionnalité clé de cette API est un service d'analyse qui peut évaluer les risques d'allergies pour une personne en se basant sur les aliments qu'elle a consommés.

## ✨ Fonctionnalités

-   **Gestion des Entités** : Opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) complètes pour :
    -   `Foods` (Plats)
    -   `Persons` (Personnes)
    -   `Ingredients` (Ingrédients)
    -   `Images` (Images)
-   **Relations Complexes** : Gère les relations many-to-many entre :
    -   Les plats et leurs ingrédients (`FoodIngredient`).
    -   Les plats et leurs images (`FoodImage`).
    -   Les personnes et les plats qu'elles ont consommés (`PersonFood`).
-   **Analyse d'Allergies** : Un endpoint dédié (`/api/persons/<id>/allergy-analysis`) pour analyser les risques d'allergies potentiels d'une personne.
-   **Initialisation Automatique** : Le script de lancement (`run.py`) crée automatiquement le schéma de la base de données.
-   **Peuplement de la Base (Seeding)** : Les données initiales sont chargées depuis un fichier JSON (`japanese_food_data.json`) au démarrage pour avoir un environnement de test prêt à l'emploi.

## 🏗️ Structure du Projet

```
.
├── app/
│   ├── __init__.py             # Factory de l'application Flask
│   ├── api/
│   │   └── orm_routes.py       # Définition des routes de l'API
│   ├── orm/
│   │   ├── models.py           # Modèles de données SQLAlchemy
│   │   └── crud.py             # Fonctions d'accès à la base (CRUD)
│   ├── services/
│   │   ├── allergy_service.py  # Logique métier pour l'analyse des allergies
│   │   └── storage.py          # Script pour peupler la base de données
│   ├── utils/
│   │   ├── database.py         # Configuration de la session SQLAlchemy
│   │   └── init_db.py          # Script pour initialiser les tables
│   └── data/
│       └── japanese_food_data.json # Données initiales
├── .env                        # Fichier de configuration (variables d'environnement)
├── config.py                   # Fichier de configuration de l'application
├── requirements.txt            # Dépendances Python
└── run.py                      # Point d'entrée pour lancer l'application
```

## 🚀 Installation et Lancement

Suivez ces étapes pour mettre en place et lancer le projet localement.

### Prérequis

-   Python 3.8+
-   `pip`
-   Un serveur de base de données PostgreSQL en cours d'exécution.

### 1. Cloner le Dépôt

```bash
git clone <url-du-depot>
cd <nom-du-dossier>
```

### 2. Créer un Environnement Virtuel

Il est fortement recommandé d'utiliser un environnement virtuel.

```bash
# Pour Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Pour Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Installer les Dépendances

Créez un fichier `requirements.txt` avec le contenu suivant :

```txt
Flask
SQLAlchemy
psycopg2-binary
python-dotenv
```

Puis installez les dépendances :

```bash
pip install -r requirements.txt
```

### 4. Configurer les Variables d'Environnement

Créez un fichier nommé `.env` à la racine du projet et ajoutez votre chaîne de connexion à la base de données.

**Exemple de fichier `.env` :**

```
DATABASE_URL=postgresql://VOTRE_USER:VOTRE_MOT_DE_PASSE@localhost:5432/VOTRE_DB_NAME
```

Assurez-vous que la base de données (`VOTRE_DB_NAME`) existe sur votre serveur PostgreSQL.

### 5. Lancer l'Application

Exécutez la commande suivante. Le script va automatiquement :
1.  Créer toutes les tables dans la base de données.
2.  Peupler les tables avec les données du fichier JSON.
3.  Démarrer le serveur de développement Flask.

```bash
python run.py
```

Vous devriez voir une sortie indiquant que les tables ont été créées, que les données ont été insérées, et que le serveur est en cours d'exécution sur `http://127.0.0.1:5000/`.

## 📖 Documentation de l'API

Tous les endpoints sont préfixés par `/api`.

---

### Endpoints `Food`

| Méthode | URL | Description |
| :------ | :-- | :---------- |
| `GET` | `/api/foods` | Récupère la liste de tous les plats. |
| `GET` | `/api/foods/<int:food_id>` | Récupère les détails d'un plat spécifique. |
| `POST` | `/api/food` | Crée un nouveau plat. |
| `PUT` | `/api/foods/<int:food_id>` | Met à jour un plat existant. |
| `DELETE` | `/api/foods/<int:food_id>` | Supprime un plat. |

**Exemple de payload pour `POST /api/food` :**
```json
{
    "name": "Okonomiyaki",
    "description": "Crêpe japonaise salée contenant divers ingrédients.",
    "allergy": "Gluten, Œuf",
    "main_image_id": 1
}
```

---

### Endpoints `Person`

| Méthode | URL | Description |
| :------ | :-- | :---------- |
| `GET` | `/api/persons` | Récupère la liste de toutes les personnes. |
| `GET` | `/api/persons/<int:person_id>` | Récupère les détails d'une personne. |
| `POST` | `/api/persons` | Crée une nouvelle personne. |
| `PUT` | `/api/persons/<int:person_id>` | Met à jour une personne. |
| `DELETE` | `/api/persons/<int:person_id>` | Supprime une personne. |

**Exemple de payload pour `POST /api/persons` :**
```json
{
    "name": "Kenji Tanaka",
    "age": 28
}
```
---

### Endpoints `Ingredient`

| Méthode | URL | Description |
| :------ | :-- | :---------- |
| `GET` | `/api/ingredients` | Récupère tous les ingrédients. |
| `POST` | `/api/ingredients` | Crée un nouvel ingrédient. |
| `DELETE` | `/api/ingredients/<int:id>`| Supprime un ingrédient. |

---

### Endpoint d'Analyse d'Allergie

Cet endpoint spécial analyse tous les aliments consommés par une personne et retourne un résumé des allergènes potentiels auxquels elle a été exposée.

| Méthode | URL | Description |
| :------ | :-- | :---------- |
| `GET` | `/api/persons/<int:person_id>/allergy-analysis` | Analyse le risque allergique pour une personne. |

**Exemple de réponse pour `GET /api/persons/1/allergy-analysis` :**
```json
{
    "person_id": 1,
    "person_name": "Yuki Yamamoto",
    "potential_allergens": {
        "Gluten": 2,
        "Soja": 1,
        "Poisson": 1
    },
    "summary": "Personne a été exposée à Gluten (2 fois), Soja (1 fois), Poisson (1 fois)."
}
```