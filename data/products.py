"""Product data and management"""

SAMPLE_PRODUCTS = [
    {
        'id': '1',
        'name': 'Apple iPhone 15 Pro Max, 256GB, Natural Titanium',
        'price': 99999,
        'category': 'Electronics',
        'description': 'The most advanced iPhone ever with titanium design, A17 Pro chip, and professional camera system.',
        'image': 'https://images.pexels.com/photos/788946/pexels-photo-788946.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.8,
        'reviews': 2547
    },
    {
        'id': '2',
        'name': 'Samsung 65" QLED 4K Smart TV with Alexa Built-in',
        'price': 74999,
        'category': 'Electronics',
        'description': 'Quantum Dot technology delivers brilliant colors and exceptional detail in 4K resolution.',
        'image': 'https://images.pexels.com/photos/1201996/pexels-photo-1201996.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.6,
        'reviews': 1823
    },
    {
        'id': '3',
        'name': 'Nike Air Max 270 Running Shoes - Men\'s',
        'price': 12499,
        'category': 'Sports',
        'description': 'Comfortable running shoes with Max Air unit for exceptional cushioning and style.',
        'image': 'https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.5,
        'reviews': 956
    },
    {
        'id': '4',
        'name': 'KitchenAid Stand Mixer, 5-Qt, Empire Red',
        'price': 31699,
        'category': 'Home & Kitchen',
        'description': 'Professional-grade stand mixer perfect for baking and cooking enthusiasts.',
        'image': 'https://images.pexels.com/photos/4226796/pexels-photo-4226796.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.9,
        'reviews': 3421
    },
    {
        'id': '5',
        'name': 'Sony WH-1000XM5 Wireless Noise Canceling Headphones',
        'price': 33299,
        'category': 'Electronics',
        'description': 'Industry-leading noise cancellation with premium sound quality and 30-hour battery life.',
        'image': 'https://images.pexels.com/photos/3394650/pexels-photo-3394650.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.7,
        'reviews': 2156
    },
    {
        'id': '6',
        'name': 'Levi\'s 501 Original Fit Jeans - Men\'s',
        'price': 5829,
        'category': 'Clothing',
        'description': 'Classic straight-leg jeans with the original fit that started it all.',
        'image': 'https://images.pexels.com/photos/1598507/pexels-photo-1598507.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.3,
        'reviews': 1245
    },
    {
        'id': '7',
        'name': 'Instant Pot Duo 7-in-1 Electric Pressure Cooker, 6 Qt',
        'price': 6659,
        'category': 'Home & Kitchen',
        'description': 'Multi-functional cooker that replaces 7 kitchen appliances in one.',
        'image': 'https://images.pexels.com/photos/4226796/pexels-photo-4226796.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.4,
        'reviews': 1876
    },
    {
        'id': '8',
        'name': 'The North Face Venture 2 Jacket - Women\'s',
        'price': 8329,
        'category': 'Clothing',
        'description': 'Waterproof, breathable jacket perfect for outdoor adventures.',
        'image': 'https://images.pexels.com/photos/1040945/pexels-photo-1040945.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.2,
        'reviews': 743
    },
    {
        'id': '9',
        'name': 'Amazon Echo Dot (5th Gen) Smart Speaker with Alexa',
        'price': 4159,
        'category': 'Electronics',
        'description': 'Compact smart speaker with improved audio and voice control for your smart home.',
        'image': 'https://images.pexels.com/photos/4790268/pexels-photo-4790268.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.6,
        'reviews': 3254
    },
    {
        'id': '10',
        'name': 'Fitbit Charge 5 Advanced Fitness & Health Tracker',
        'price': 16659,
        'category': 'Sports',
        'description': 'Advanced fitness tracker with built-in GPS, stress management, and health insights.',
        'image': 'https://images.pexels.com/photos/437037/pexels-photo-437037.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.1,
        'reviews': 2187
    },
    {
        'id': '11',
        'name': 'Ninja Foodi Personal Blender with Cups',
        'price': 6659,
        'category': 'Home & Kitchen',
        'description': 'Powerful personal blender perfect for smoothies, shakes, and frozen drinks.',
        'image': 'https://images.pexels.com/photos/4226796/pexels-photo-4226796.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.3,
        'reviews': 1432
    },
    {
        'id': '12',
        'name': 'Adidas Ultraboost 22 Running Shoes - Women\'s',
        'price': 15829,
        'category': 'Sports',
        'description': 'Premium running shoes with responsive Boost midsole and Primeknit upper.',
        'image': 'https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg?auto=compress&cs=tinysrgb&w=400',
        'rating': 4.7,
        'reviews': 1654
    }
]

class ProductManager:
    """Manage product data and operations"""
    
    def __init__(self):
        self.products = SAMPLE_PRODUCTS.copy()
    
    def get_all_products(self):
        """Get all products"""
        return self.products
    
    def get_product_by_id(self, product_id: str):
        """Get product by ID"""
        return next((p for p in self.products if p['id'] == product_id), None)
    
    def search_products(self, query: str):
        """Search products by name or description"""
        query = query.lower()
        return [p for p in self.products 
                if query in p['name'].lower() or query in p['description'].lower()]
    
    def filter_by_category(self, category: str):
        """Filter products by category"""
        if category == 'All':
            return self.products
        return [p for p in self.products if p['category'] == category]
    
    def get_categories(self):
        """Get all unique categories"""
        categories = set(p['category'] for p in self.products)
        return ['All'] + sorted(list(categories))
    
    def sort_products(self, products, sort_by: str):
        """Sort products by specified criteria"""
        if sort_by == "Price: Low to High":
            return sorted(products, key=lambda x: x['price'])
        elif sort_by == "Price: High to Low":
            return sorted(products, key=lambda x: x['price'], reverse=True)
        elif sort_by == "Rating":
            return sorted(products, key=lambda x: x['rating'], reverse=True)
        elif sort_by == "Name":
            return sorted(products, key=lambda x: x['name'])
        else:  # Featured
            return products
    
    def add_product(self, product: dict):
        """Add a new product"""
        self.products.append(product)
    
    def add_products(self, products: list):
        """Add multiple products"""
        self.products.extend(products)