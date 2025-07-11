"""Cart management service"""
from datetime import datetime
from typing import Dict, List, Any

class CartService:
    """Handle cart operations and calculations"""
    
    def __init__(self):
        self.free_shipping_threshold = 20000
        self.tax_rate = 0.18
        self.shipping_cost = 499
    
    def add_to_cart(self, cart: List[Dict], product: Dict) -> List[Dict]:
        """Add product to cart"""
        # Check if product already exists
        for item in cart:
            if item['id'] == product['id']:
                item['quantity'] += 1
                item['last_interaction'] = datetime.now()
                return cart
        
        # Add new item
        cart_item = {
            'id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'quantity': 1,
            'image': product['image'],
            'added_at': datetime.now(),
            'last_interaction': datetime.now()
        }
        cart.append(cart_item)
        return cart
    
    def remove_from_cart(self, cart: List[Dict], product_id: str) -> List[Dict]:
        """Remove product from cart"""
        return [item for item in cart if item['id'] != product_id]
    
    def update_quantity(self, cart: List[Dict], product_id: str, quantity: int) -> List[Dict]:
        """Update quantity of item in cart"""
        if quantity <= 0:
            return self.remove_from_cart(cart, product_id)
        
        for item in cart:
            if item['id'] == product_id:
                item['quantity'] = quantity
                item['last_interaction'] = datetime.now()
                break
        return cart
    
    def calculate_cart_totals(self, cart: List[Dict]) -> Dict[str, float]:
        """Calculate cart totals"""
        subtotal = sum(item['price'] * item['quantity'] for item in cart)
        shipping = 0 if subtotal >= self.free_shipping_threshold else self.shipping_cost
        tax = subtotal * self.tax_rate
        total = subtotal + shipping + tax
        
        return {
            'subtotal': subtotal,
            'shipping': shipping,
            'tax': tax,
            'total': total,
            'item_count': sum(item['quantity'] for item in cart)
        }
    
    def get_shipping_progress(self, cart: List[Dict]) -> Dict[str, Any]:
        """Get free shipping progress"""
        subtotal = sum(item['price'] * item['quantity'] for item in cart)
        
        if subtotal >= self.free_shipping_threshold:
            return {
                'qualified': True,
                'remaining': 0,
                'progress': 1.0
            }
        else:
            remaining = self.free_shipping_threshold - subtotal
            progress = subtotal / self.free_shipping_threshold
            return {
                'qualified': False,
                'remaining': remaining,
                'progress': progress
            }