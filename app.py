import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import time
import random
from typing import Dict, List, Any
import base64
from io import StringIO

# Configure Streamlit page
st.set_page_config(
    page_title="Click&Cart - AI-Powered E-Commerce Platform",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #f97316 0%, #ea580c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .product-card {
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        background: white;
    }
    .cart-item {
        background: #f9fafb;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #f97316;
    }
    .intervention-alert {
        background: #fef3c7;
        border: 1px solid #f59e0b;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .success-alert {
        background: #d1fae5;
        border: 1px solid #10b981;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'session_start': datetime.now() - timedelta(minutes=2),
            'behavior_score': 0.4,
            'previous_purchases': 0
        }
    if 'orders' not in st.session_state:
        st.session_state.orders = []
    if 'interventions' not in st.session_state:
        st.session_state.interventions = []
    if 'products' not in st.session_state:
        st.session_state.products = get_sample_products()
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    if 'last_interaction' not in st.session_state:
        st.session_state.last_interaction = datetime.now()

def get_sample_products():
    return [
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
        }
    ]

def calculate_cart_prediction():
    """Calculate cart abandonment prediction using ML-like logic"""
    if not st.session_state.cart:
        return None
    
    # Calculate factors
    session_duration = (datetime.now() - st.session_state.user_data['session_start']).total_seconds() / 60
    cart_value = sum(item['price'] * item['quantity'] for item in st.session_state.cart)
    time_since_last_interaction = (datetime.now() - st.session_state.last_interaction).total_seconds() / 60
    
    probability = 0
    factors = []
    
    # Time-based factors
    if session_duration > 10:
        probability += 0.3
        factors.append('Long session duration')
    
    if cart_value > 20000:
        probability += 0.2
        factors.append('High cart value')
    
    if len(st.session_state.cart) > 3:
        probability += 0.15
        factors.append('Many items in cart')
    
    if time_since_last_interaction > 1:
        probability += 0.4
        factors.append('Inactive for 1+ minute')
    
    if st.session_state.user_data['behavior_score'] < 0.5:
        probability += 0.25
        factors.append('Low engagement score')
    
    if st.session_state.user_data['previous_purchases'] == 0:
        probability += 0.1
        factors.append('First-time visitor')
    
    probability = min(probability, 1.0)
    
    return {
        'probability': probability,
        'confidence': random.uniform(0.7, 1.0),
        'factors': factors,
        'timestamp': datetime.now()
    }

def add_to_cart(product):
    """Add product to cart"""
    st.session_state.last_interaction = datetime.now()
    
    # Check if product already in cart
    for item in st.session_state.cart:
        if item['id'] == product['id']:
            item['quantity'] += 1
            return
    
    # Add new item to cart
    cart_item = {
        'id': product['id'],
        'name': product['name'],
        'price': product['price'],
        'quantity': 1,
        'image': product['image'],
        'added_at': datetime.now()
    }
    st.session_state.cart.append(cart_item)

def remove_from_cart(product_id):
    """Remove product from cart"""
    st.session_state.cart = [item for item in st.session_state.cart if item['id'] != product_id]
    st.session_state.last_interaction = datetime.now()

def update_cart_quantity(product_id, quantity):
    """Update quantity of item in cart"""
    for item in st.session_state.cart:
        if item['id'] == product_id:
            if quantity <= 0:
                remove_from_cart(product_id)
            else:
                item['quantity'] = quantity
                st.session_state.last_interaction = datetime.now()
            break

def trigger_intervention(prediction):
    """Trigger intervention based on prediction"""
    if prediction and prediction['probability'] > 0.6:
        intervention_types = [
            {'type': 'discount', 'message': 'Get 15% off your entire order!', 'value': 15},
            {'type': 'free_shipping', 'message': 'Free shipping on your order!', 'value': 0},
            {'type': 'limited_time', 'message': 'Limited time: 20% off everything!', 'value': 20}
        ]
        
        intervention = random.choice(intervention_types)
        intervention.update({
            'id': len(st.session_state.interventions) + 1,
            'timestamp': datetime.now(),
            'success': False
        })
        
        st.session_state.interventions.append(intervention)
        return intervention
    return None

def home_page():
    """Home page with navigation and overview"""
    st.markdown("""
    <div class="main-header">
        <h1>🛒 SmartMart - AI-Powered E-Commerce Platform</h1>
        <p>Experience the future of online shopping with intelligent cart recovery and real-time analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Statistics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Users", "10K+", "12%")
    with col2:
        st.metric("Products", "50K+", "8%")
    with col3:
        st.metric("Success Rate", "94%", "5%")
    with col4:
        st.metric("Revenue", "₹2.5Cr", "15%")
    
    st.markdown("---")
    
    # Feature cards
    st.subheader("🚀 Powerful Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("""
            ### 🛒 Smart Shopping Experience
            Browse thousands of products with intelligent recommendations and personalized deals.
            """)
            if st.button("🛍️ Start Shopping", key="shop_btn"):
                st.session_state.page = "shop"
                st.rerun()
    
    with col2:
        with st.container():
            st.markdown("""
            ### 📊 Analytics Dashboard
            Monitor cart abandonment, user behavior, and AI-powered predictions in real-time.
            """)
            if st.button("📈 View Analytics", key="analytics_btn"):
                st.session_state.page = "dashboard"
                st.rerun()
    
    col3, col4 = st.columns(2)
    
    with col3:
        with st.container():
            st.markdown("""
            ### 💳 Checkout Analytics
            Track conversion rates, revenue metrics, and payment method performance.
            """)
            if st.button("💰 Checkout Analytics", key="checkout_btn"):
                st.session_state.page = "checkout_analytics"
                st.rerun()
    
    with col4:
        with st.container():
            st.markdown("""
            ### 📁 Data Management
            Import external datasets, manage products, and configure user data sources.
            """)
            if st.button("⚙️ Data Import", key="import_btn"):
                st.session_state.page = "import"
                st.rerun()

def shopping_page():
    """Shopping page with products and cart"""
    st.title("🛍️ SmartMart Shopping")
    
    # Search and filters
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_query = st.text_input("🔍 Search products", placeholder="Search for products...")
    with col2:
        categories = ['All'] + list(set(product['category'] for product in st.session_state.products))
        selected_category = st.selectbox("📂 Category", categories)
    with col3:
        sort_by = st.selectbox("🔄 Sort by", ["Featured", "Price: Low to High", "Price: High to Low", "Rating"])
    
    # Filter products
    filtered_products = st.session_state.products
    if search_query:
        filtered_products = [p for p in filtered_products if search_query.lower() in p['name'].lower()]
    if selected_category != 'All':
        filtered_products = [p for p in filtered_products if p['category'] == selected_category]
    
    # Sort products
    if sort_by == "Price: Low to High":
        filtered_products = sorted(filtered_products, key=lambda x: x['price'])
    elif sort_by == "Price: High to Low":
        filtered_products = sorted(filtered_products, key=lambda x: x['price'], reverse=True)
    elif sort_by == "Rating":
        filtered_products = sorted(filtered_products, key=lambda x: x['rating'], reverse=True)
    
    # Display products
    st.subheader(f"📦 Products ({len(filtered_products)} items)")
    
    # Product grid
    cols = st.columns(3)
    for idx, product in enumerate(filtered_products):
        with cols[idx % 3]:
            with st.container():
                st.image(product['image'], use_column_width=True)
                st.markdown(f"**{product['name']}**")
                st.markdown(f"⭐ {product['rating']} ({product['reviews']} reviews)")
                st.markdown(f"💰 **₹{product['price']:,}**")
                st.markdown(f"📝 {product['description'][:100]}...")
                
                if st.button(f"🛒 Add to Cart", key=f"add_{product['id']}"):
                    add_to_cart(product)
                    st.success(f"Added {product['name']} to cart!")
                    st.rerun()
    
    # Cart prediction and intervention
    prediction = calculate_cart_prediction()
    if prediction and prediction['probability'] > 0.6:
        intervention = trigger_intervention(prediction)
        if intervention and not any(i['id'] == intervention['id'] and i['success'] for i in st.session_state.interventions):
            st.markdown(f"""
            <div class="intervention-alert">
                <h4>🎁 Special Offer!</h4>
                <p>{intervention['message']}</p>
                <p><strong>Save ₹{sum(item['price'] * item['quantity'] for item in st.session_state.cart) * (intervention['value'] / 100):,.0f} on your order!</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("✅ Apply Offer", key="apply_offer"):
                intervention['success'] = True
                st.success("Offer applied successfully!")
                st.rerun()

def cart_sidebar():
    """Shopping cart in sidebar"""
    with st.sidebar:
        st.header("🛒 Shopping Cart")
        
        if not st.session_state.cart:
            st.info("Your cart is empty")
            return
        
        total_items = sum(item['quantity'] for item in st.session_state.cart)
        cart_value = sum(item['price'] * item['quantity'] for item in st.session_state.cart)
        
        st.metric("Items in Cart", total_items)
        st.metric("Cart Value", f"₹{cart_value:,}")
        
        # Free shipping progress
        free_shipping_threshold = 20000
        if cart_value >= free_shipping_threshold:
            st.success("🚚 You qualify for FREE shipping!")
        else:
            remaining = free_shipping_threshold - cart_value
            progress = cart_value / free_shipping_threshold
            st.progress(progress)
            st.info(f"Add ₹{remaining:,} more for FREE shipping")
        
        st.markdown("---")
        
        # Cart items
        for item in st.session_state.cart:
            st.markdown(f"""
            <div class="cart-item">
                <strong>{item['name']}</strong><br>
                ₹{item['price']:,} × {item['quantity']} = ₹{item['price'] * item['quantity']:,}
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("➖", key=f"dec_{item['id']}"):
                    update_cart_quantity(item['id'], item['quantity'] - 1)
                    st.rerun()
            with col2:
                st.write(f"Qty: {item['quantity']}")
            with col3:
                if st.button("➕", key=f"inc_{item['id']}"):
                    update_cart_quantity(item['id'], item['quantity'] + 1)
                    st.rerun()
            
            if st.button("🗑️ Remove", key=f"remove_{item['id']}"):
                remove_from_cart(item['id'])
                st.rerun()
        
        st.markdown("---")
        
        # Checkout
        shipping = 0 if cart_value >= free_shipping_threshold else 499
        tax = cart_value * 0.18
        total = cart_value + shipping + tax
        
        st.markdown(f"""
        **Order Summary:**
        - Subtotal: ₹{cart_value:,}
        - Shipping: {'FREE' if shipping == 0 else f'₹{shipping:,}'}
        - Tax (18%): ₹{tax:,.0f}
        - **Total: ₹{total:,.0f}**
        """)
        
        if st.button("💳 Proceed to Checkout", type="primary"):
            st.session_state.page = "checkout"
            st.rerun()

def checkout_page():
    """Checkout process"""
    st.title("💳 Secure Checkout")
    
    if not st.session_state.cart:
        st.warning("Your cart is empty!")
        return
    
    # Progress steps
    steps = ["📍 Shipping", "💳 Payment", "📋 Review"]
    if 'checkout_step' not in st.session_state:
        st.session_state.checkout_step = 0
    
    # Progress indicator
    progress_cols = st.columns(len(steps))
    for i, step in enumerate(steps):
        with progress_cols[i]:
            if i <= st.session_state.checkout_step:
                st.success(step)
            else:
                st.info(step)
    
    st.markdown("---")
    
    # Step content
    if st.session_state.checkout_step == 0:
        # Shipping address
        st.subheader("📍 Shipping Address")
        
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name *", value="John Doe")
            email = st.text_input("Email *", value="john@example.com")
            address = st.text_area("Address *", value="123 Main Street")
        with col2:
            phone = st.text_input("Phone *", value="+91 9876543210")
            city = st.text_input("City *", value="Mumbai")
            pincode = st.text_input("PIN Code *", value="400001")
        
        if st.button("Next: Payment →", type="primary"):
            if all([full_name, email, address, phone, city, pincode]):
                st.session_state.shipping_info = {
                    'full_name': full_name, 'email': email, 'address': address,
                    'phone': phone, 'city': city, 'pincode': pincode
                }
                st.session_state.checkout_step = 1
                st.rerun()
            else:
                st.error("Please fill all required fields")
    
    elif st.session_state.checkout_step == 1:
        # Payment method
        st.subheader("💳 Payment Method")
        
        payment_method = st.radio("Select Payment Method", 
                                ["Credit/Debit Card", "UPI", "Cash on Delivery"])
        
        if payment_method == "Credit/Debit Card":
            col1, col2 = st.columns(2)
            with col1:
                card_number = st.text_input("Card Number", placeholder="1234 5678 9012 3456")
                name_on_card = st.text_input("Name on Card")
            with col2:
                expiry = st.text_input("Expiry (MM/YY)", placeholder="12/25")
                cvv = st.text_input("CVV", placeholder="123", type="password")
        
        elif payment_method == "UPI":
            upi_id = st.text_input("UPI ID", placeholder="yourname@paytm")
        
        elif payment_method == "Cash on Delivery":
            st.info("You will pay ₹{:,} in cash upon delivery".format(
                sum(item['price'] * item['quantity'] for item in st.session_state.cart) * 1.18 + 499
            ))
            cod_confirm = st.checkbox("I confirm cash payment on delivery")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Shipping"):
                st.session_state.checkout_step = 0
                st.rerun()
        with col2:
            if st.button("Next: Review →", type="primary"):
                st.session_state.payment_method = payment_method
                st.session_state.checkout_step = 2
                st.rerun()
    
    elif st.session_state.checkout_step == 2:
        # Order review
        st.subheader("📋 Review Your Order")
        
        # Order items
        st.write("**Items:**")
        for item in st.session_state.cart:
            st.write(f"• {item['name']} × {item['quantity']} = ₹{item['price'] * item['quantity']:,}")
        
        # Shipping address
        if 'shipping_info' in st.session_state:
            st.write("**Shipping Address:**")
            info = st.session_state.shipping_info
            st.write(f"{info['full_name']}, {info['address']}, {info['city']} - {info['pincode']}")
        
        # Payment method
        if 'payment_method' in st.session_state:
            st.write(f"**Payment Method:** {st.session_state.payment_method}")
        
        # Order summary
        cart_value = sum(item['price'] * item['quantity'] for item in st.session_state.cart)
        shipping = 0 if cart_value >= 20000 else 499
        tax = cart_value * 0.18
        total = cart_value + shipping + tax
        
        st.markdown(f"""
        **Order Summary:**
        - Subtotal: ₹{cart_value:,}
        - Shipping: {'FREE' if shipping == 0 else f'₹{shipping:,}'}
        - Tax (18%): ₹{tax:,.0f}
        - **Total: ₹{total:,.0f}**
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Payment"):
                st.session_state.checkout_step = 1
                st.rerun()
        with col2:
            if st.button("🔒 Place Order", type="primary"):
                # Process order
                order = {
                    'order_id': f"ORD{int(time.time())}",
                    'items': st.session_state.cart.copy(),
                    'subtotal': cart_value,
                    'shipping': shipping,
                    'tax': tax,
                    'total': total,
                    'payment_method': st.session_state.get('payment_method', 'Unknown'),
                    'order_date': datetime.now(),
                    'status': 'completed'
                }
                
                st.session_state.orders.append(order)
                st.session_state.cart = []
                st.session_state.checkout_step = 0
                
                st.success("🎉 Order placed successfully!")
                st.balloons()
                
                st.markdown(f"""
                <div class="success-alert">
                    <h4>✅ Order Confirmed!</h4>
                    <p><strong>Order ID:</strong> {order['order_id']}</p>
                    <p><strong>Total:</strong> ₹{total:,.0f}</p>
                    <p>Your order will be delivered within 2-3 business days.</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("Continue Shopping"):
                    st.session_state.page = "shop"
                    st.rerun()

def analytics_dashboard():
    """Analytics dashboard with predictions and metrics"""
    st.title("📊 Smart Cart Recovery Dashboard")
    
    # Current session metrics
    prediction = calculate_cart_prediction()
    cart_value = sum(item['price'] * item['quantity'] for item in st.session_state.cart)
    session_duration = (datetime.now() - st.session_state.user_data['session_start']).total_seconds() / 60
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Cart Items", len(st.session_state.cart))
    with col2:
        st.metric("Cart Value", f"₹{cart_value:,}")
    with col3:
        abandonment_risk = prediction['probability'] * 100 if prediction else 0
        st.metric("Abandonment Risk", f"{abandonment_risk:.1f}%", 
                 "HIGH" if abandonment_risk > 50 else "LOW")
    with col4:
        st.metric("Session Duration", f"{session_duration:.1f} min")
    
    st.markdown("---")
    
    # Prediction analysis
    if prediction:
        st.subheader("🤖 ML Prediction Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            # Risk gauge
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = prediction['probability'] * 100,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Abandonment Risk %"},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 50], 'color': "lightgray"},
                        {'range': [50, 80], 'color': "yellow"},
                        {'range': [80, 100], 'color': "red"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90
                    }
                }
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.write("**Risk Factors:**")
            for factor in prediction['factors']:
                st.write(f"⚠️ {factor}")
            
            st.write(f"**Confidence:** {prediction['confidence']:.1%}")
            st.write(f"**Last Updated:** {prediction['timestamp'].strftime('%H:%M:%S')}")
    
    # Interventions history
    st.subheader("🎯 Intervention History")
    if st.session_state.interventions:
        interventions_df = pd.DataFrame([
            {
                'Type': i['type'].title(),
                'Message': i['message'],
                'Value': f"{i['value']}%" if i['value'] > 0 else "N/A",
                'Success': "✅" if i['success'] else "❌",
                'Timestamp': i['timestamp'].strftime('%H:%M:%S')
            }
            for i in st.session_state.interventions
        ])
        st.dataframe(interventions_df, use_container_width=True)
    else:
        st.info("No interventions triggered yet")
    
    # User behavior chart
    st.subheader("📈 Session Activity")
    
    # Generate sample activity data
    activity_data = []
    current_time = st.session_state.user_data['session_start']
    for i in range(int(session_duration)):
        activity_data.append({
            'Time': current_time + timedelta(minutes=i),
            'Activity': random.choice(['Browsing', 'Viewing Product', 'Adding to Cart', 'Idle']),
            'Engagement': random.uniform(0.3, 1.0)
        })
    
    if activity_data:
        activity_df = pd.DataFrame(activity_data)
        fig = px.line(activity_df, x='Time', y='Engagement', 
                     title='User Engagement Over Time',
                     color_discrete_sequence=['#f97316'])
        st.plotly_chart(fig, use_container_width=True)

def checkout_analytics():
    """Checkout analytics dashboard"""
    st.title("💰 Checkout Analytics Dashboard")
    
    if not st.session_state.orders:
        st.info("No orders yet. Complete some purchases to see analytics!")
        return
    
    # Time range filter
    time_range = st.selectbox("📅 Time Range", ["Today", "This Week", "This Month"])
    
    # Calculate metrics
    orders_df = pd.DataFrame(st.session_state.orders)
    total_orders = len(orders_df)
    total_revenue = orders_df['total'].sum()
    avg_order_value = orders_df['total'].mean()
    completed_orders = len(orders_df[orders_df['status'] == 'completed'])
    conversion_rate = (completed_orders / total_orders * 100) if total_orders > 0 else 0
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Orders", total_orders, "↗️ +12%")
    with col2:
        st.metric("Total Revenue", f"₹{total_revenue:,.0f}", "↗️ +18%")
    with col3:
        st.metric("Avg Order Value", f"₹{avg_order_value:,.0f}", "↗️ +8%")
    with col4:
        st.metric("Conversion Rate", f"{conversion_rate:.1f}%", "↗️ +5%")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue over time
        orders_df['date'] = pd.to_datetime(orders_df['order_date']).dt.date
        daily_revenue = orders_df.groupby('date')['total'].sum().reset_index()
        
        fig = px.bar(daily_revenue, x='date', y='total',
                    title='Daily Revenue',
                    color_discrete_sequence=['#f97316'])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Payment methods
        payment_counts = orders_df['payment_method'].value_counts()
        
        fig = px.pie(values=payment_counts.values, names=payment_counts.index,
                    title='Payment Methods Distribution')
        st.plotly_chart(fig, use_container_width=True)
    
    # Order status breakdown
    st.subheader("📊 Order Status Breakdown")
    status_counts = orders_df['status'].value_counts()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        completed = status_counts.get('completed', 0)
        st.metric("✅ Completed", completed)
    with col2:
        processing = status_counts.get('processing', 0)
        st.metric("⏳ Processing", processing)
    with col3:
        failed = status_counts.get('failed', 0)
        st.metric("❌ Failed", failed)
    
    # Recent orders table
    st.subheader("📋 Recent Orders")
    recent_orders = orders_df.sort_values('order_date', ascending=False).head(10)
    
    display_orders = recent_orders[['order_id', 'total', 'payment_method', 'status', 'order_date']].copy()
    display_orders['order_date'] = display_orders['order_date'].dt.strftime('%Y-%m-%d %H:%M')
    display_orders['total'] = display_orders['total'].apply(lambda x: f"₹{x:,.0f}")
    
    st.dataframe(display_orders, use_container_width=True)

def data_import_page():
    """Data import and management"""
    st.title("📁 Data Management & Import")
    
    tab1, tab2, tab3 = st.tabs(["📤 Import Data", "📊 Current Data", "⚙️ Settings"])
    
    with tab1:
        st.subheader("Import External Data")
        
        data_type = st.radio("Data Type", ["Products", "Users", "Orders"])
        
        if data_type == "Products":
            st.write("**Upload Product Data (CSV/JSON)**")
            uploaded_file = st.file_uploader("Choose file", type=['csv', 'json'])
            
            if uploaded_file:
                try:
                    if uploaded_file.name.endswith('.csv'):
                        df = pd.read_csv(uploaded_file)
                    else:
                        df = pd.read_json(uploaded_file)
                    
                    st.write("**Preview:**")
                    st.dataframe(df.head())
                    
                    if st.button("Import Products"):
                        # Convert to product format
                        new_products = []
                        for _, row in df.iterrows():
                            product = {
                                'id': str(row.get('id', len(st.session_state.products) + len(new_products) + 1)),
                                'name': row.get('name', 'Unknown Product'),
                                'price': float(row.get('price', 0)),
                                'category': row.get('category', 'General'),
                                'description': row.get('description', 'No description'),
                                'image': row.get('image', 'https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?auto=compress&cs=tinysrgb&w=400'),
                                'rating': float(row.get('rating', 4.0)),
                                'reviews': int(row.get('reviews', 100))
                            }
                            new_products.append(product)
                        
                        st.session_state.products.extend(new_products)
                        st.success(f"Successfully imported {len(new_products)} products!")
                
                except Exception as e:
                    st.error(f"Error importing data: {str(e)}")
        
        elif data_type == "Users":
            st.write("**Sample User Data Format:**")
            sample_users = pd.DataFrame([
                {'id': 'user1', 'name': 'Alice Johnson', 'email': 'alice@example.com', 'behavior_score': 0.85},
                {'id': 'user2', 'name': 'Bob Smith', 'email': 'bob@example.com', 'behavior_score': 0.62}
            ])
            st.dataframe(sample_users)
        
        elif data_type == "Orders":
            st.write("**Sample Order Data Format:**")
            sample_orders = pd.DataFrame([
                {'order_id': 'ORD001', 'total': 25000, 'status': 'completed', 'payment_method': 'card'},
                {'order_id': 'ORD002', 'total': 15000, 'status': 'processing', 'payment_method': 'upi'}
            ])
            st.dataframe(sample_orders)
    
    with tab2:
        st.subheader("Current Data Overview")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Products", len(st.session_state.products))
        with col2:
            st.metric("Orders", len(st.session_state.orders))
        with col3:
            st.metric("Interventions", len(st.session_state.interventions))
        
        # Products table
        if st.session_state.products:
            st.write("**Products:**")
            products_df = pd.DataFrame(st.session_state.products)
            st.dataframe(products_df[['name', 'price', 'category', 'rating']], use_container_width=True)
    
    with tab3:
        st.subheader("System Settings")
        
        st.write("**Prediction Settings:**")
        abandonment_threshold = st.slider("Abandonment Risk Threshold (%)", 0, 100, 60)
        intervention_delay = st.slider("Intervention Delay (minutes)", 1, 10, 1)
        
        st.write("**E-commerce Settings:**")
        free_shipping_threshold = st.number_input("Free Shipping Threshold (₹)", value=20000)
        tax_rate = st.slider("Tax Rate (%)", 0.0, 30.0, 18.0)
        
        if st.button("Save Settings"):
            st.success("Settings saved successfully!")

def chatbot_interface():
    """AI Chatbot for customer support"""
    st.subheader("🤖 SmartMart Assistant")
    
    # Chat messages
    if not st.session_state.chat_messages:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Hi! I'm your SmartMart assistant. How can I help you today?"}
        ]
    
    # Display chat messages
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message..."):
        # Add user message
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        
        # Generate bot response
        if "discount" in prompt.lower() or "offer" in prompt.lower():
            response = "Great! I can offer you a 15% discount on your current cart. Would you like me to apply it?"
        elif "shipping" in prompt.lower():
            response = "We offer FREE shipping on orders over ₹20,000. Your current cart qualifies for free shipping!"
        elif "return" in prompt.lower():
            response = "We have a hassle-free 30-day return policy. All items can be returned in original condition."
        elif "help" in prompt.lower():
            response = "I can help you with discounts, shipping, returns, product information, and more. What would you like to know?"
        else:
            response = "I understand! Let me help you with that. Would you like me to apply a special discount to complete your purchase?"
        
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        st.rerun()

def main():
    """Main application"""
    initialize_session_state()
    
    # Sidebar navigation
    with st.sidebar:
        st.title("🛒 SmartMart")
        
        # Navigation
        if 'page' not in st.session_state:
            st.session_state.page = "home"
        
        page = st.radio("Navigation", 
                       ["🏠 Home", "🛍️ Shop", "📊 Dashboard", "💰 Checkout Analytics", 
                        "💳 Checkout", "📁 Data Import", "🤖 Chat Support"],
                       key="nav_radio")
        
        # Update page based on selection
        page_mapping = {
            "🏠 Home": "home",
            "🛍️ Shop": "shop", 
            "📊 Dashboard": "dashboard",
            "💰 Checkout Analytics": "checkout_analytics",
            "💳 Checkout": "checkout",
            "📁 Data Import": "import",
            "🤖 Chat Support": "chat"
        }
        st.session_state.page = page_mapping[page]
        
        st.markdown("---")
        
        # User info
        st.write(f"**User:** {st.session_state.user_data['name']}")
        st.write(f"**Email:** {st.session_state.user_data['email']}")
        
        # Cart summary (only show if not on checkout page)
        if st.session_state.page != "checkout":
            cart_sidebar()
    
    # Main content
    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "shop":
        shopping_page()
    elif st.session_state.page == "dashboard":
        analytics_dashboard()
    elif st.session_state.page == "checkout_analytics":
        checkout_analytics()
    elif st.session_state.page == "checkout":
        checkout_page()
    elif st.session_state.page == "import":
        data_import_page()
    elif st.session_state.page == "chat":
        chatbot_interface()

if __name__ == "__main__":
    main()