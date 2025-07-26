import joblib
import pandas as pd
import numpy as np
import shap
from feature_options import all_options

# Load model
model = joblib.load('D:\GITHUB\SalaryEstimator\code\web\lr_model.pkl')

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

# User input for numerical features
user_input = {
    'YearsCodePro': 5,
    'Age': 30,
    'WorkExp': 7,
    'GDP_per_capita': 50000,
    'Cost_Index': 100
}

# Dictionary selections for one-hot encoded features
selections = {
    'EdLevel': 'Bachelor\'s degree (B.A., B.S., B.Eng., etc.)',
    'RemoteWork': 'Remote',
    'OrgSize': '100 to 499 employees',
    'Country': 'United States',
    'DevType': 'Developer, back-end',
    'Employment': 'Employed, full-time',
    'Languages': ['Python', 'JavaScript']
}

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

print(f"Predicted log salary: {prediction:.4f}")
print(f"Predicted annual salary: ${actual_salary:,.2f}")
print(f"Experience Level (calculated): {experience_level}")

# SHAP Analysis
print("\n" + "="*50)
print("SHAP ANALYSIS - Feature Importance")
print("="*50)

# Create SHAP explainer - handle Pipeline model
if hasattr(model, 'named_steps'):
    # If it's a Pipeline, get the final estimator (should be LinearRegression)
    final_model = model.named_steps[list(model.named_steps.keys())[-1]]
    print(f"Model type: Pipeline with {type(final_model).__name__}")
    
    # For Pipeline, we need to use TreeExplainer or create a custom explainer
    # Since it's a linear model, we'll extract coefficients manually
    if hasattr(final_model, 'coef_') and hasattr(final_model, 'intercept_'):
        # Extract coefficients from the linear model
        coefficients = final_model.coef_
        intercept = final_model.intercept_
        
        # Calculate SHAP values manually for linear model
        # SHAP values for linear models are: feature_value * coefficient
        feature_values = df.iloc[0].values
        shap_values = feature_values * coefficients
        
        # Get feature names
        feature_names = df.columns.tolist()
        
        # Create a list of (feature_name, shap_value) tuples and sort by absolute SHAP value
        feature_importance = list(zip(feature_names, shap_values))
        feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)
        
        # Display top 15 most important features
        print("\nTop 15 Most Important Features:")
        print("-" * 40)
        for i, (feature, shap_val) in enumerate(feature_importance[:15]):
            impact = "📈" if shap_val > 0 else "📉"
            print(f"{i+1:2d}. {impact} {feature:<40} {shap_val:>8.4f}")
        
        # Calculate total positive and negative contributions
        positive_contributions = sum([val for _, val in feature_importance if val > 0])
        negative_contributions = sum([val for _, val in feature_importance if val < 0])
        
        print(f"\n📊 Summary:")
        print(f"   Total positive contributions: {positive_contributions:.4f}")
        print(f"   Total negative contributions: {negative_contributions:.4f}")
        print(f"   Net contribution: {positive_contributions + negative_contributions:.4f}")
        print(f"   Base value (model intercept): {intercept:.4f}")
        
        # Show breakdown by feature categories
        print(f"\n📋 Feature Category Breakdown:")
        print("-" * 30)
        
        # Group features by category
        categories = {
            'Numerical': ['YearsCodePro', 'Age', 'WorkExp', 'GDP_per_capita', 'Cost_Index'],
            'Education': [f for f in feature_names if f.startswith('EdLevel_')],
            'Work': [f for f in feature_names if f.startswith('RemoteWork_') or f.startswith('OrgSize_') or f.startswith('Employment_')],
            'Experience': [f for f in feature_names if f.startswith('ExperienceLevel_')],
            'Location': [f for f in feature_names if f.startswith('Country_')],
            'Role': [f for f in feature_names if f.startswith('DevType_')],
            'Languages': [f for f in feature_names if f.startswith('Lang_')]
        }
        
        for category, features in categories.items():
            category_contrib = sum([val for feature, val in feature_importance if feature in features])
            if abs(category_contrib) > 0.001:  # Only show significant categories
                print(f"   {category:<12}: {category_contrib:>8.4f}")
    else:
        print("❌ Could not extract coefficients from the model")
else:
    # If it's not a Pipeline, try the original approach
    try:
        explainer = shap.LinearExplainer(model, df)
        shap_values = explainer.shap_values(df)
        
        # Get feature names and their SHAP values
        feature_names = df.columns.tolist()
        shap_values_list = shap_values[0].tolist()
        
        # Create a list of (feature_name, shap_value) tuples and sort by absolute SHAP value
        feature_importance = list(zip(feature_names, shap_values_list))
        feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)
        
        # Display top 15 most important features
        print("\nTop 15 Most Important Features:")
        print("-" * 40)
        for i, (feature, shap_val) in enumerate(feature_importance[:15]):
            impact = "📈" if shap_val > 0 else "📉"
            print(f"{i+1:2d}. {impact} {feature:<40} {shap_val:>8.4f}")
        
        # Calculate total positive and negative contributions
        positive_contributions = sum([val for _, val in feature_importance if val > 0])
        negative_contributions = sum([val for _, val in feature_importance if val < 0])
        
        print(f"\n📊 Summary:")
        print(f"   Total positive contributions: {positive_contributions:.4f}")
        print(f"   Total negative contributions: {negative_contributions:.4f}")
        print(f"   Net contribution: {positive_contributions + negative_contributions:.4f}")
        print(f"   Base value (model intercept): {explainer.expected_value:.4f}")
        
        # Show breakdown by feature categories
        print(f"\n📋 Feature Category Breakdown:")
        print("-" * 30)
        
        # Group features by category
        categories = {
            'Numerical': ['YearsCodePro', 'Age', 'WorkExp', 'GDP_per_capita', 'Cost_Index'],
            'Education': [f for f in feature_names if f.startswith('EdLevel_')],
            'Work': [f for f in feature_names if f.startswith('RemoteWork_') or f.startswith('OrgSize_') or f.startswith('Employment_')],
            'Experience': [f for f in feature_names if f.startswith('ExperienceLevel_')],
            'Location': [f for f in feature_names if f.startswith('Country_')],
            'Role': [f for f in feature_names if f.startswith('DevType_')],
            'Languages': [f for f in feature_names if f.startswith('Lang_')]
        }
        
        for category, features in categories.items():
            category_contrib = sum([val for feature, val in feature_importance if feature in features])
            if abs(category_contrib) > 0.001:  # Only show significant categories
                print(f"   {category:<12}: {category_contrib:>8.4f}")
    except Exception as e:
        print(f"❌ SHAP analysis failed: {e}")
