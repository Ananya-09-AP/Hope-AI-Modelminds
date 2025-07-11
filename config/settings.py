"""Application configuration and settings"""

# Application Settings
APP_NAME = "Click&Cart"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI-Powered E-Commerce Platform with Smart Cart Recovery"

# E-commerce Settings
FREE_SHIPPING_THRESHOLD = 20000  # ₹20,000
TAX_RATE = 0.18  # 18% GST
SHIPPING_COST = 499  # ₹499

# ML Model Settings
ABANDONMENT_THRESHOLD = 0.6  # 60% probability threshold
INTERVENTION_DELAY_MINUTES = 1  # Trigger interventions after 1 minute of inactivity
CONFIDENCE_THRESHOLD = 0.7  # Minimum confidence for predictions

# Session Settings
SESSION_TIMEOUT_MINUTES = 30
MAX_CART_ITEMS = 50
MAX_QUANTITY_PER_ITEM = 10

# UI Settings
PRODUCTS_PER_PAGE = 12
MAX_SEARCH_RESULTS = 100
CHART_HEIGHT = 400
SIDEBAR_WIDTH = 300

# Currency Settings
CURRENCY_SYMBOL = "₹"
CURRENCY_CODE = "INR"
LOCALE = "en-IN"

# Image Settings
DEFAULT_PRODUCT_IMAGE = "https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?auto=compress&cs=tinysrgb&w=400"
IMAGE_PLACEHOLDER = "https://via.placeholder.com/400x300?text=No+Image"

# Color Scheme
COLORS = {
    'primary': '#f97316',      # Orange
    'secondary': '#ea580c',    # Dark Orange
    'success': '#10b981',      # Green
    'warning': '#f59e0b',      # Yellow
    'error': '#ef4444',        # Red
    'info': '#3b82f6',         # Blue
    'gray': '#6b7280',         # Gray
    'light_gray': '#f3f4f6',   # Light Gray
    'dark_gray': '#374151'     # Dark Gray
}

# Streamlit Page Config
PAGE_CONFIG = {
    'page_title': f"{APP_NAME} - {APP_DESCRIPTION}",
    'page_icon': "🛒",
    'layout': "wide",
    'initial_sidebar_state': "expanded"
}

# Data Import Settings
SUPPORTED_FILE_TYPES = ['csv', 'json']
MAX_FILE_SIZE_MB = 10
MAX_IMPORT_RECORDS = 10000

# Analytics Settings
DEFAULT_TIME_RANGES = ['Today', 'This Week', 'This Month', 'Last 3 Months']
CHART_COLORS = ['#f97316', '#ea580c', '#fb923c', '#fed7aa']

# Intervention Settings
INTERVENTION_TYPES = [
    {
        'type': 'discount',
        'min_value': 5,
        'max_value': 25,
        'weight': 0.4
    },
    {
        'type': 'free_shipping',
        'min_value': 0,
        'max_value': 0,
        'weight': 0.3
    },
    {
        'type': 'limited_time',
        'min_value': 0,
        'max_value': 0,
        'weight': 0.3
    }
]

# Email Settings (for future use)
EMAIL_SETTINGS = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'use_tls': True,
    'sender_name': APP_NAME,
    'sender_email': 'noreply@smartmart.com'
}

# API Settings (for future integrations)
API_SETTINGS = {
    'rate_limit': 1000,  # requests per hour
    'timeout': 30,       # seconds
    'retry_attempts': 3
}

# Security Settings
SECURITY_SETTINGS = {
    'session_cookie_secure': True,
    'session_cookie_httponly': True,
    'csrf_protection': True,
    'max_login_attempts': 5,
    'password_min_length': 8
}

# Logging Settings
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file_path': 'logs/smartmart.log',
    'max_file_size': '10MB',
    'backup_count': 5
}