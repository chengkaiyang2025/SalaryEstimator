import streamlit as st
import pandas as pd
import numpy as np
import joblib
from feature_options import all_options

# Page configuration
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💰",
    layout="wide"
)

# Title and description
st.title("💰 Tech Salary Predictor")
st.markdown("Enter your information below to get a salary prediction for tech professionals.")

# Load model
@st.cache_resource
def load_model():
    try:
        model = joblib.load('D:\GITHUB\SalaryEstimator\code\web\lr_model.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

if model is None:
    st.error("Failed to load model. Please check if lr_model.pkl exists.")
    st.stop()

# Create layout
st.subheader("📝 Your Information")

# Initialize dictionaries
user_input = {}
selections = {}

# Basic Information Panel
with st.expander("📊 Basic Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        user_input['YearsCodePro'] = st.number_input(
            "Years of Professional Coding", 
            min_value=0, max_value=50, value=5, step=1
        )
        user_input['Age'] = st.number_input(
            "Age", 
            min_value=16, max_value=80, value=30, step=1
        )
    
    with col2:
        user_input['WorkExp'] = st.number_input(
            "Total Work Experience (Years)", 
            min_value=0, max_value=50, value=7, step=1
        )
        user_input['GDP_per_capita'] = st.number_input(
            "GDP per capita (USD)", 
            min_value=1000, max_value=200000, value=50000, step=1000
        )
    
    with col3:
        user_input['Cost_Index'] = st.number_input(
            "Cost of Living Index", 
            min_value=20, max_value=200, value=100, step=1
        )

# Work Details Panel
with st.expander("💼 Work Details", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        selections['EdLevel'] = st.selectbox(
            "Education Level",
            all_options['EdLevel'],
            index=0
        )
        selections['ExperienceLevel'] = st.selectbox(
            "Experience Level",
            all_options['ExperienceLevel'],
            index=1
        )
        selections['Employment'] = st.selectbox(
            "Employment Type",
            all_options['Employment'],
            index=0
        )
        selections['RemoteWork'] = st.selectbox(
            "Work Location",
            all_options['RemoteWork'],
            index=1
        )
    
    with col2:
        selections['OrgSize'] = st.selectbox(
            "Company Size",
            all_options['OrgSize'],
            index=2
        )
        
        # Find default indices safely
        try:
            us_index = all_options['Country'].index('United States')
        except ValueError:
            us_index = 0
        
        try:
            dev_index = all_options['DevType'].index('Developer, back-end')
        except ValueError:
            dev_index = 0
        
        selections['Country'] = st.selectbox(
            "Country",
            all_options['Country'],
            index=us_index
        )
        
        selections['DevType'] = st.selectbox(
            "Role/Position",
            all_options['DevType'],
            index=dev_index
        )

# Programming Languages Panel
with st.expander("💻 Programming Languages", expanded=True):
    selections['Languages'] = st.multiselect(
        "Programming Languages You Work With",
        all_options['Languages'],
        default=['Python', 'JavaScript']
    )

# Prediction button
st.markdown("---")
if st.button("🚀 Generate Salary Prediction", type="primary", use_container_width=True):
    with st.spinner("Making prediction..."):
        try:
            # Create DataFrame with all zeros
            df = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)
            
            # Fill numerical features
            for key, value in user_input.items():
                if key in df.columns:
                    df[key] = value
            
            # Fill one-hot encoded features
            for feature, selection in selections.items():
                if feature == 'Languages':
                    # Handle multiple language selection
                    for lang in selection:
                        lang_col = f'Lang_{lang}'
                        if lang_col in df.columns:
                            df[lang_col] = 1
                else:
                    # Handle single selection
                    col_name = f'{feature}_{selection}'
                    if col_name in df.columns:
                        df[col_name] = 1
            
            # Make prediction
            prediction = model.predict(df)[0]
            actual_salary = np.power(10, prediction)
            
            # Display results
            st.success("## 💰 Prediction Results")
            
            result_col1, result_col2 = st.columns(2)
            
            with result_col1:
                st.metric("Predicted Annual Salary", f"${actual_salary:,.0f}")
            
            with result_col2:
                st.metric("Predicted Log Salary", f"{prediction:.4f}")
            
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.error("Please check if the model file exists and all features are properly configured.")

# Footer
st.markdown("---")
st.markdown("*This application uses machine learning to predict tech salaries based on your profile.*")
