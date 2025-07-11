# Project Summary
The Smart Cart Recovery project enhances e-commerce platforms by predicting cart abandonment using machine learning. It offers real-time personalized interventions, such as discounts and chatbot support, to retain customers and improve conversion rates. The application features an interactive dashboard for analyzing abandonment risks and simulating user behavior, making it a valuable tool for optimizing online sales.

# Project Module Description
- **Dashboard**: Displays analytics on cart abandonment rates, device distribution, and high-risk carts needing intervention.
- **User Simulator**: Simulates various user profiles to assess their abandonment risk in real-time.
- **Model Insights**: Provides performance metrics, feature importance, and user segment analysis of the underlying ML model.
- **Rule-based Chatbot**: Engages customers when abandonment risk is high, offering assistance and intervention suggestions.
- **About**: Provides information about the application.

# Directory Tree
```
streamlit_template/
├── app.py               # Main application script containing the logic and UI
├── requirements.txt     # List of Python dependencies required for the application, with minimum version specifications
├── README.md            # Comprehensive guide for installation, deployment, and usage
└── streamlit_app.py     # Entry point for running the Streamlit application
```

# File Description Inventory
- **app.py**: Contains the application logic, including data generation, model training, user interface, and chatbot functionalities.
- **requirements.txt**: Specifies the necessary Python libraries for the application, including minimum version requirements to prevent compatibility issues.
- **README.md**: Provides detailed installation instructions, feature descriptions, and usage guidelines.
- **streamlit_app.py**: Imports all content from `app.py` to serve as the main file for running the Streamlit application.

# Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: scikit-learn, pandas, numpy
- **Data Visualization**: matplotlib, seaborn, plotly

# Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```
