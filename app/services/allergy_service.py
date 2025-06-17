from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Dict, List, Optional
from app.orm.models import PersonFood, Food

class AllergyAnalyzer:
    @staticmethod
    def analyze_allergy_risk(db: Session, person_id: int, threshold: Optional[float] = None) -> Dict:
        """
        Analyse le risque d'allergie basé sur la consommation alimentaire
        
        Args:
            db: Session SQLAlchemy
            person_id: ID de la personne à analyser
            threshold: Seuil personnalisé pour l'évaluation du risque
            
        Returns:
            Dict: Résultats détaillés de l'analyse avec probabilités
        """
        try:
            # 1. Requête optimisée pour les consommations à risque
            consumptions = db.query(
                Food.id_food,
                Food.name,
                Food.allergy,
                func.sum(PersonFood.quantity).label('total_quantity'),
                func.count().label('consumption_count')
            ).join(
                PersonFood,
                PersonFood.food_id == Food.id_food
            ).filter(
                PersonFood.person_id == person_id,
                Food.allergy.isnot(None)
            ).group_by(
                Food.id_food,
                Food.name,
                Food.allergy
            ).all()

            if not consumptions:
                return {
                    'person_id': person_id,
                    'allergy_probability': "0%",
                    'risk_factors': [],
                    'interpretation': "Aucune consommation d'aliments allergènes détectée"
                }

            # 2. Calcul dynamique du seuil
            avg_consumption = sum(c.total_quantity for c in consumptions) / len(consumptions)
            dynamic_threshold = threshold if threshold is not None else avg_consumption * 1.5

            # 3. Analyse des résultats
            risk_data = []
            total_weighted_risk = 0
            
            for food in consumptions:
                # Calcul du score de risque pondéré
                time_factor = min(food.consumption_count / 10, 1.0)
                quantity_factor = min(food.total_quantity / dynamic_threshold, 2.0)
                risk_score = round(time_factor * quantity_factor, 2)
                
                risk_data.append({
                    'food_id': food.id_food,
                    'food_name': food.name,
                    'allergen': food.allergy,
                    'total_consumed': food.total_quantity,
                    'consumption_count': food.consumption_count,
                    'risk_score': risk_score
                })
                
                total_weighted_risk += risk_score

            # 4. Calcul de la probabilité globale
            max_possible_risk = len(risk_data) * 2.0  # 2.0 étant le facteur max
            probability = min((total_weighted_risk / max_possible_risk) * 100, 100)

            # 5. Détection des allergènes principaux
            main_allergens = sorted(
                [item for item in risk_data if item['risk_score'] > 0.7],
                key=lambda x: x['risk_score'],
                reverse=True
            )

            return {
                'person_id': person_id,
                'allergy_probability': f"{probability:.1f}%",
                'risk_factors': risk_data,
                'main_allergens': main_allergens[:3],
                'interpretation': AllergyAnalyzer._get_interpretation(probability),
                'threshold_used': dynamic_threshold
            }

        except Exception as e:
            return {
                'error': str(e),
                'message': "Une erreur est survenue lors de l'analyse"
            }

    @staticmethod
    def _get_interpretation(probability: float) -> str:
        """Retourne une interprétation textuelle avec gradation"""
        ranges = [
            (0, 20, "Risque négligeable"),
            (20, 40, "Risque faible"),
            (40, 60, "Risque modéré - Surveillance conseillée"),
            (60, 80, "Risque élevé - Consultation recommandée"),
            (80, 101, "Risque très élevé - Consultation urgente")
        ]
        
        for min_val, max_val, message in ranges:
            if min_val <= probability < max_val:
                return message
        return "Évaluation non disponible"