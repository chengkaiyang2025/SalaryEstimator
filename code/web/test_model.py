import joblib
import os
import pandas as pd
import numpy as np
from feature_options import all_options
from shap_util import analyze_model_with_shap, print_shap_analysis

# Load model
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lr_model.pkl')
model = joblib.load(model_path)

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

# SHAP Analysis using the utility module
shap_results = analyze_model_with_shap(model, df)
print_shap_analysis(shap_results)
