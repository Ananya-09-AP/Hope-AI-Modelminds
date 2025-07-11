import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

class CartPredictionModel:
    """ML-like model for predicting cart abandonment"""
    
    def __init__(self):
        self.abandonment_threshold = 0.6
        self.confidence_base = 0.7
    
    def predict_abandonment(self, cart_data: List[Dict], user_data: Dict) -> Optional[Dict]:
        """Predict cart abandonment probability"""
        if not cart_data:
            return None
        
        probability = 0
        factors = []
        
        # Time-based factors
        session_duration = self._get_session_duration(user_data)
        if session_duration > 10:
            probability += 0.3
            factors.append('Long session duration')
        
        # Cart-based factors
        cart_value = sum(item['price'] * item['quantity'] for item in cart_data)
        if cart_value > 20000:
            probability += 0.2
            factors.append('High cart value')
        
        if len(cart_data) > 5:
            probability += 0.15
            factors.append('Many items in cart')
        
        # User behavior factors
        if user_data.get('behavior_score', 0.5) < 0.5:
            probability += 0.25
            factors.append('Low engagement score')
        
        if user_data.get('previous_purchases', 0) == 0:
            probability += 0.1
            factors.append('First-time visitor')
        
        # Inactivity factor
        time_since_last_action = self._get_time_since_last_action(user_data)
        if time_since_last_action > 1:
            probability += 0.4
            factors.append('Inactive for 1+ minute')
        
        # Normalize probability
        probability = min(probability, 1.0)
        
        return {
            'probability': probability,
            'confidence': random.uniform(self.confidence_base, 1.0),
            'factors': factors,
            'timestamp': datetime.now()
        }
    
    def _get_session_duration(self, user_data: Dict) -> float:
        """Calculate session duration in minutes"""
        session_start = user_data.get('session_start', datetime.now())
        if isinstance(session_start, str):
            session_start = datetime.fromisoformat(session_start)
        return (datetime.now() - session_start).total_seconds() / 60
    
    def _get_time_since_last_action(self, user_data: Dict) -> float:
        """Calculate time since last interaction in minutes"""
        last_interaction = user_data.get('last_interaction', datetime.now())
        if isinstance(last_interaction, str):
            last_interaction = datetime.fromisoformat(last_interaction)
        return (datetime.now() - last_interaction).total_seconds() / 60