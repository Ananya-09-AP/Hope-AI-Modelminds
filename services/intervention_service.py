"""Intervention management service"""
import random
from datetime import datetime
from typing import Dict, List, Any, Optional

class InterventionService:
    """Handle cart abandonment interventions"""
    
    def __init__(self):
        self.intervention_types = [
            {
                'type': 'discount',
                'message': 'Don\'t miss out! Get 15% off your entire order!',
                'value': 15
            },
            {
                'type': 'discount',
                'message': 'Limited time: 20% off everything in your cart!',
                'value': 20
            },
            {
                'type': 'free_shipping',
                'message': 'Free shipping on your order - no minimum required!',
                'value': 0
            },
            {
                'type': 'limited_time',
                'message': 'Hurry! These items are selling fast. Complete your purchase now!',
                'value': 0
            },
            {
                'type': 'discount',
                'message': 'Special offer: 10% off + free shipping on your order!',
                'value': 10
            }
        ]
    
    def should_trigger_intervention(self, prediction: Dict) -> bool:
        """Determine if intervention should be triggered"""
        if not prediction:
            return False
        return prediction.get('probability', 0) > 0.6
    
    def generate_intervention(self, cart_value: float, user_data: Dict) -> Dict:
        """Generate an intervention based on cart and user data"""
        intervention_template = random.choice(self.intervention_types)
        
        intervention = {
            'id': f"INT_{int(datetime.now().timestamp())}",
            'type': intervention_template['type'],
            'message': intervention_template['message'],
            'value': intervention_template['value'],
            'cart_value': cart_value,
            'timestamp': datetime.now(),
            'success': False,
            'user_id': user_data.get('id', 'unknown')
        }
        
        # Customize message based on cart value
        if intervention['type'] == 'discount' and cart_value > 0:
            savings = cart_value * (intervention['value'] / 100)
            intervention['savings'] = savings
            intervention['message'] += f" Save ₹{savings:,.0f} on your order!"
        
        return intervention
    
    def apply_intervention(self, intervention: Dict) -> Dict:
        """Mark intervention as successfully applied"""
        intervention['success'] = True
        intervention['applied_at'] = datetime.now()
        return intervention
    
    def get_intervention_stats(self, interventions: List[Dict]) -> Dict:
        """Get statistics about interventions"""
        if not interventions:
            return {
                'total': 0,
                'successful': 0,
                'success_rate': 0,
                'total_savings': 0
            }
        
        successful = [i for i in interventions if i.get('success', False)]
        total_savings = sum(i.get('savings', 0) for i in successful)
        
        return {
            'total': len(interventions),
            'successful': len(successful),
            'success_rate': len(successful) / len(interventions) * 100,
            'total_savings': total_savings
        }