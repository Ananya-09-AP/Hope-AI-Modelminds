# SmartMart - AI-Powered E-Commerce Platform

A comprehensive Streamlit application that demonstrates intelligent cart abandonment prevention, real-time analytics, and AI-powered customer interventions.

## Features

### 🏠 Home Page
- Beautiful landing page with feature overview
- Navigation to all application sections
- Key statistics and metrics display

### 🛍️ Smart Shopping Experience
- Product catalog with search and filtering
- Real-time cart management
- AI-powered abandonment prediction
- Automatic intervention triggers

### 📊 Analytics Dashboard
- Real-time cart abandonment predictions
- ML-based risk assessment
- User behavior tracking
- Intervention success monitoring

### 💰 Checkout Analytics
- Revenue and conversion tracking
- Payment method analysis
- Order status monitoring
- Time-based analytics

### 💳 Secure Checkout Process
- Multi-step checkout flow
- Multiple payment options (Card/UPI/COD)
- Order confirmation and tracking
- Real-time price calculations

### 📁 Data Management
- CSV/JSON data import
- Product and user management
- System configuration
- Data visualization

### 🤖 AI Assistant
- Interactive chatbot support
- Personalized recommendations
- Discount applications
- Customer service automation

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd smartmart-streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. **Home Page**: Start here to explore all features
2. **Shopping**: Browse products, add to cart, experience AI interventions
3. **Analytics**: Monitor real-time predictions and user behavior
4. **Checkout**: Complete purchases with secure payment processing
5. **Data Import**: Upload your own product/user data
6. **Chat Support**: Get AI-powered customer assistance

## Key Technologies

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical computations
- **Python**: Core programming language

## AI Features

- **Cart Abandonment Prediction**: ML algorithms predict when users might abandon their cart
- **Risk Assessment**: Real-time scoring based on user behavior
- **Smart Interventions**: Automated discounts and offers
- **Behavioral Analytics**: Track user engagement patterns

## Configuration

The application includes configurable settings for:
- Abandonment risk thresholds
- Intervention timing
- Shipping and tax calculations
- Discount percentages

## Data Import

Supports importing:
- **Products**: CSV/JSON with name, price, category, description
- **Users**: Customer data with behavior scores
- **Orders**: Historical transaction data

## Sample Data Format

### Products CSV:
```csv
id,name,price,category,description,image,rating,reviews
1,"Product Name",999,"Electronics","Description","image_url",4.5,100
```

### Users CSV:
```csv
id,name,email,behavior_score,previous_purchases
user1,"John Doe","john@example.com",0.75,5
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.