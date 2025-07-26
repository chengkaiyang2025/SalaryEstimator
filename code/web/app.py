import streamlit as st
import pandas as pd
import numpy as np
import joblib
from feature_options import all_options
from shap_util import analyze_model_with_shap, get_shap_insights

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
def map_experience_level(years):
    if pd.isna(years):
        return np.nan
    elif years < 2:
        return 'Beginner'
    elif years < 5:
        return 'Intermediate'
    elif years < 10:
        return 'Advanced'
    else:
        return 'Expert'
# Basic Information Panel
with st.expander("📊 Basic Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        user_input['EdLevel'] = st.selectbox(
            "Education Level",
            all_options['EdLevel'],
            index=0
        )
        user_input['YearsCodePro'] = st.number_input(
            "Years of Coding", 
            min_value=0, max_value=50, value=4, step=1
        )
        user_input['Age'] = st.number_input(
            "Age", 
            min_value=16, max_value=80, value=23, step=1
        )
    
    with col2:
        user_input['WorkExp'] = st.number_input(
            "Total Work Experience (Years)", 
            min_value=0, max_value=50, value=2, step=1
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
st.subheader("📝 The place you want to work")

# Work Details Panel
with st.expander("💼 Work Details", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:

        # ExperienceLevel will be calculated automatically based on YearsCodePro
        # No need to show this in the UI
        selections['Employment'] = st.selectbox(
            "Employment Type",
            all_options['Employment'],
            index=0
        )
        selections['RemoteWork'] = st.selectbox(
            "Work Location",
            all_options['RemoteWork'],
            index=0
        )
    
    with col2:
        selections['OrgSize'] = st.selectbox(
            "Company Size",
            all_options['OrgSize'],
            index=2
        )
        
        # Find default indices safely
        try:
            us_index = all_options['Country'].index('Canada')
        except ValueError:
            us_index = 0
        
        try:
            dev_index = all_options['DevType'].index('Developer, full-stack')
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
st.subheader("📝 Your tech stack")

# Programming Languages Panel
with st.expander("💻 Programming Languages", expanded=True):
    selections['Languages'] = st.multiselect(
        "Programming Languages You Work With",
        all_options['Languages'],
        default=['Python','JavaScript','Java','C#','SQL']
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
            
            # Calculate ExperienceLevel based on YearsCodePro
            experience_level = map_experience_level(user_input['YearsCodePro'])
            
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
            
            # Handle ExperienceLevel separately since it's calculated automatically
            if experience_level is not None:
                exp_col = f'ExperienceLevel_{experience_level}'
                if exp_col in df.columns:
                    df[exp_col] = 1
            
            # Make prediction
            prediction = model.predict(df)[0]
            actual_salary = np.power(10, prediction)
            
            # Display results
            st.success("## 💰 Prediction Results")
            
            result_col1, result_col2 = st.columns(2)
            
            with result_col1:
                st.metric("Predicted Annual Salary", f"${actual_salary:,.0f}")
            
            with result_col2:
                st.metric("Experience Level", experience_level)
            
            # SHAP Analysis
            st.markdown("---")
            st.subheader("🔍 Feature Importance Analysis")
            
            # Get SHAP analysis
            shap_results = analyze_model_with_shap(model, df)
            
            if shap_results['success']:
                # Display insights in a user-friendly way
                insights = get_shap_insights(shap_results, top_n=5)
                
                # Create columns for insights
                if insights:
                    insight_cols = st.columns(len(insights))
                    
                    for i, insight in enumerate(insights):
                        with insight_cols[i]:
                            if insight['type'] == 'positive':
                                st.markdown("### 📈 Top Salary Boosters")
                                for feature in insight['features']:
                                    st.markdown(f"• **{feature['name']}**: +{feature['value']:.3f}")
                            
                            elif insight['type'] == 'negative':
                                st.markdown("### 📉 Top Salary Reducers")
                                for feature in insight['features']:
                                    st.markdown(f"• **{feature['name']}**: {feature['value']:.3f}")
                            
                            elif insight['type'] == 'category':
                                st.markdown("### 📊 Category Impact")
                                for category in insight['categories']:
                                    icon = "📈" if category['impact'] == 'positive' else "📉"
                                    st.markdown(f"• **{category['category']}**: {icon} {category['contribution']:.3f}")
                
                # Show detailed breakdown in expander
                with st.expander("📋 Detailed Feature Analysis"):
                    # Top features table
                    if shap_results['feature_importance']:
                        top_features = shap_results['feature_importance'][:10]
                        feature_data = {
                            'Feature': [f[0] for f in top_features],
                            'Impact': [f[1] for f in top_features],
                            'Direction': ['📈' if f[1] > 0 else '📉' for f in top_features]
                        }
                        feature_df = pd.DataFrame(feature_data)
                        st.dataframe(feature_df, use_container_width=True)
                    
                    # Summary metrics
                    summary = shap_results['summary']
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Positive Contributions", f"{summary['positive_contributions']:.3f}")
                    with col2:
                        st.metric("Negative Contributions", f"{summary['negative_contributions']:.3f}")
                    with col3:
                        st.metric("Net Impact", f"{summary['positive_contributions'] + summary['negative_contributions']:.3f}")
            else:
                st.warning("Could not generate feature importance analysis.")
            
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.error("Please check if the model file exists and all features are properly configured.")

# Footer
st.markdown("---")
st.markdown("*This application uses machine learning to predict tech salaries based on your profile.*")
