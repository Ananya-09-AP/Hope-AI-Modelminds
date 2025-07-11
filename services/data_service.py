"""Data import and export service"""
import pandas as pd
import json
from typing import Dict, List, Any, Optional
from io import StringIO

class DataService:
    """Handle data import/export operations"""
    
    def __init__(self):
        pass
    
    def import_csv_data(self, csv_content: str) -> List[Dict]:
        """Import data from CSV content"""
        try:
            df = pd.read_csv(StringIO(csv_content))
            return df.to_dict('records')
        except Exception as e:
            raise ValueError(f"Error parsing CSV: {str(e)}")
    
    def import_json_data(self, json_content: str) -> List[Dict]:
        """Import data from JSON content"""
        try:
            data = json.loads(json_content)
            if isinstance(data, list):
                return data
            else:
                return [data]
        except Exception as e:
            raise ValueError(f"Error parsing JSON: {str(e)}")
    
    def transform_to_products(self, data: List[Dict], mapping: Dict[str, str]) -> List[Dict]:
        """Transform imported data to product format"""
        products = []
        
        for item in data:
            try:
                product = {
                    'id': str(item.get(mapping.get('id', 'id'), len(products) + 1)),
                    'name': item.get(mapping.get('name', 'name'), 'Unknown Product'),
                    'price': float(item.get(mapping.get('price', 'price'), 0)),
                    'category': item.get(mapping.get('category', 'category'), 'General'),
                    'description': item.get(mapping.get('description', 'description'), 'No description available'),
                    'image': item.get(mapping.get('image', 'image'), 'https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?auto=compress&cs=tinysrgb&w=400'),
                    'rating': float(item.get(mapping.get('rating', 'rating'), 4.0)),
                    'reviews': int(item.get(mapping.get('reviews', 'reviews'), 100))
                }
                products.append(product)
            except (ValueError, TypeError) as e:
                # Skip invalid records
                continue
        
        return products
    
    def transform_to_users(self, data: List[Dict], mapping: Dict[str, str]) -> List[Dict]:
        """Transform imported data to user format"""
        users = []
        
        for item in data:
            try:
                user = {
                    'id': str(item.get(mapping.get('id', 'id'), len(users) + 1)),
                    'name': item.get(mapping.get('name', 'name'), 'Anonymous User'),
                    'email': item.get(mapping.get('email', 'email'), 'user@example.com'),
                    'behavior_score': float(item.get(mapping.get('behavior_score', 'behavior_score'), 0.5)),
                    'previous_purchases': int(item.get(mapping.get('previous_purchases', 'previous_purchases'), 0)),
                    'avg_session_time': float(item.get(mapping.get('avg_session_time', 'avg_session_time'), 10.0))
                }
                users.append(user)
            except (ValueError, TypeError) as e:
                # Skip invalid records
                continue
        
        return users
    
    def export_to_csv(self, data: List[Dict]) -> str:
        """Export data to CSV format"""
        if not data:
            return ""
        
        df = pd.DataFrame(data)
        return df.to_csv(index=False)
    
    def export_to_json(self, data: List[Dict]) -> str:
        """Export data to JSON format"""
        return json.dumps(data, indent=2, default=str)
    
    def validate_product_data(self, products: List[Dict]) -> Dict[str, Any]:
        """Validate imported product data"""
        valid_products = []
        errors = []
        
        required_fields = ['name', 'price']
        
        for i, product in enumerate(products):
            product_errors = []
            
            # Check required fields
            for field in required_fields:
                if not product.get(field):
                    product_errors.append(f"Missing {field}")
            
            # Validate price
            try:
                price = float(product.get('price', 0))
                if price < 0:
                    product_errors.append("Price cannot be negative")
            except (ValueError, TypeError):
                product_errors.append("Invalid price format")
            
            if product_errors:
                errors.append(f"Row {i+1}: {', '.join(product_errors)}")
            else:
                valid_products.append(product)
        
        return {
            'valid_products': valid_products,
            'errors': errors,
            'total_processed': len(products),
            'valid_count': len(valid_products),
            'error_count': len(errors)
        }