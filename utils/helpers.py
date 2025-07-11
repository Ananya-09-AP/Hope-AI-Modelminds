"""Utility functions and helpers"""
import streamlit as st
from datetime import datetime, timedelta
from typing import Dict, List, Any

def format_currency(amount: float) -> str:
    """Format amount as Indian currency"""
    return f"₹{amount:,.0f}"

def format_percentage(value: float) -> str:
    """Format value as percentage"""
    return f"{value:.1f}%"

def format_datetime(dt: datetime) -> str:
    """Format datetime for display"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def format_time_ago(dt: datetime) -> str:
    """Format datetime as time ago"""
    now = datetime.now()
    diff = now - dt
    
    if diff.days > 0:
        return f"{diff.days} day{'s' if diff.days > 1 else ''} ago"
    elif diff.seconds > 3600:
        hours = diff.seconds // 3600
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    else:
        return "Just now"

def calculate_discount(original_price: float, discount_percent: float) -> Dict[str, float]:
    """Calculate discount amount and final price"""
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    
    return {
        'original_price': original_price,
        'discount_percent': discount_percent,
        'discount_amount': discount_amount,
        'final_price': final_price,
        'savings': discount_amount
    }

def get_star_rating(rating: float) -> str:
    """Convert numeric rating to star display"""
    full_stars = int(rating)
    half_star = 1 if rating - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    
    return "⭐" * full_stars + "⭐" * half_star + "☆" * empty_stars

def validate_email(email: str) -> bool:
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    """Basic phone validation for Indian numbers"""
    import re
    # Remove spaces and special characters
    clean_phone = re.sub(r'[^\d+]', '', phone)
    
    # Check for Indian mobile number patterns
    patterns = [
        r'^\+91[6-9]\d{9}$',  # +91 followed by 10 digits starting with 6-9
        r'^[6-9]\d{9}$',      # 10 digits starting with 6-9
        r'^0[6-9]\d{9}$'      # 0 followed by 10 digits starting with 6-9
    ]
    
    return any(re.match(pattern, clean_phone) for pattern in patterns)

def generate_order_id() -> str:
    """Generate unique order ID"""
    import random
    import string
    
    timestamp = int(datetime.now().timestamp())
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"ORD{timestamp}{random_suffix}"

def safe_divide(numerator: float, denominator: float, default: float = 0) -> float:
    """Safe division with default value"""
    try:
        return numerator / denominator if denominator != 0 else default
    except (TypeError, ZeroDivisionError):
        return default

def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def get_color_for_status(status: str) -> str:
    """Get color code for status"""
    colors = {
        'completed': '#10b981',    # green
        'processing': '#f59e0b',   # yellow
        'failed': '#ef4444',       # red
        'pending': '#6b7280',      # gray
        'cancelled': '#ef4444'     # red
    }
    return colors.get(status.lower(), '#6b7280')

def create_progress_bar(current: float, total: float, height: int = 20) -> str:
    """Create HTML progress bar"""
    percentage = min((current / total) * 100, 100) if total > 0 else 0
    
    return f"""
    <div style="
        width: 100%;
        height: {height}px;
        background-color: #e5e7eb;
        border-radius: {height//2}px;
        overflow: hidden;
    ">
        <div style="
            width: {percentage}%;
            height: 100%;
            background-color: #f97316;
            transition: width 0.3s ease;
        "></div>
    </div>
    """

def display_metric_card(title: str, value: str, change: str = "", icon: str = "📊"):
    """Display a metric card with styling"""
    change_color = "green" if change.startswith("+") else "red" if change.startswith("-") else "gray"
    
    st.markdown(f"""
    <div style="
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        text-align: center;
    ">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="font-size: 1.5rem; font-weight: bold; color: #1f2937;">{value}</div>
        <div style="color: #6b7280; margin-bottom: 0.25rem;">{title}</div>
        {f'<div style="color: {change_color}; font-size: 0.875rem;">{change}</div>' if change else ''}
    </div>
    """, unsafe_allow_html=True)