# Tech Salary Predictor - Streamlit App

A simple Streamlit application that collects user information and generates salary predictions for tech professionals.

## Features

- **Simple Form Interface**: Clean, straightforward form layout without sidebar
- **User Input Collection**: Collects key information like age, experience, education, location, etc.
- **Random Salary Prediction**: Generates salary predictions based on user inputs (placeholder for ML model)
- **Quick Insights**: Provides simple career and location-based insights
- **Future ML Integration Ready**: Prepared for integration with trained machine learning models

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

1. Navigate to the web directory:
```bash
cd code/web
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser and go to the URL shown in the terminal (usually http://localhost:8501)

## Usage

1. Fill in your information in the form:
   - **Basic Information**: Age, Years of Professional Coding, Work Experience
   - **Education & Experience**: Education Level, Experience Level
   - **Work Details**: Employment Type, Work Location, Company Size
   - **Role & Location**: Role/Position, Country
   - **Programming Languages**: Select languages you work with

2. Click "🚀 Generate Salary Prediction" to get your predicted salary

3. View the prediction results and quick insights

## App Structure

- **app.py**: Main Streamlit application with simplified form interface
- **model_utils.py**: Utility functions for model integration (simplified)
- **requirements.txt**: Python dependencies

## Data Structure

The app collects user data in a simple format:

```python
user_data = {
    'YearsCodePro': years_code_pro,
    'Age': age,
    'WorkExp': work_exp,
    'EdLevel': ed_level,
    'RemoteWork': remote_work,
    'OrgSize': org_size,
    'ExperienceLevel': experience_level,
    'Country': country,
    'DevType': dev_type,
    'Employment': employment,
    'Languages': selected_languages
}
```

## Future Enhancements

- Integrate with trained machine learning models (XGBoost, Random Forest, etc.)
- Add more sophisticated salary prediction algorithms
- Include data visualization and charts
- Implement user data persistence
- Add model comparison features

## Simplified Design

This version removes:
- Sidebar layout
- Complex one-hot encoding logic
- Extensive feature engineering
- Detailed profile summaries

Focusing on a clean, simple interface that's easy to use and understand. 