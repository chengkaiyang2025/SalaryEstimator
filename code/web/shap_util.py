import shap
import pandas as pd
import numpy as np

def analyze_model_with_shap(model, df, show_top_n=15):
    """
    Analyze model predictions using SHAP values.
    
    Args:
        model: The trained model (can be Pipeline or direct model)
        df: DataFrame with features for prediction
        show_top_n: Number of top features to display
    
    Returns:
        dict: Dictionary containing analysis results
    """
    results = {
        'feature_importance': [],
        'summary': {},
        'category_breakdown': {},
        'success': False,
        'error': None
    }
    
    try:
        # Handle Pipeline model
        if hasattr(model, 'named_steps'):
            # If it's a Pipeline, get the final estimator
            final_model = model.named_steps[list(model.named_steps.keys())[-1]]
            
            # Extract coefficients from the linear model
            if hasattr(final_model, 'coef_') and hasattr(final_model, 'intercept_'):
                coefficients = final_model.coef_
                intercept = final_model.intercept_
                
                # Calculate SHAP values manually for linear model
                feature_values = df.iloc[0].values
                shap_values = feature_values * coefficients
                
                # Get feature names
                feature_names = df.columns.tolist()
                
                # Create feature importance list
                feature_importance = list(zip(feature_names, shap_values))
                feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)
                
                # Store results
                results['feature_importance'] = feature_importance
                results['summary'] = {
                    'positive_contributions': sum([val for _, val in feature_importance if val > 0]),
                    'negative_contributions': sum([val for _, val in feature_importance if val < 0]),
                    'intercept': intercept
                }
                
                # Calculate category breakdown
                results['category_breakdown'] = calculate_category_breakdown(feature_names, feature_importance)
                results['success'] = True
                
            else:
                results['error'] = "Could not extract coefficients from the model"
                
        else:
            # If it's not a Pipeline, use SHAP explainer
            explainer = shap.LinearExplainer(model, df)
            shap_values = explainer.shap_values(df)
            
            # Get feature names and their SHAP values
            feature_names = df.columns.tolist()
            shap_values_list = shap_values[0].tolist()
            
            # Create feature importance list
            feature_importance = list(zip(feature_names, shap_values_list))
            feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)
            
            # Store results
            results['feature_importance'] = feature_importance
            results['summary'] = {
                'positive_contributions': sum([val for _, val in feature_importance if val > 0]),
                'negative_contributions': sum([val for _, val in feature_importance if val < 0]),
                'intercept': explainer.expected_value
            }
            
            # Calculate category breakdown
            results['category_breakdown'] = calculate_category_breakdown(feature_names, feature_importance)
            results['success'] = True
            
    except Exception as e:
        results['error'] = f"SHAP analysis failed: {str(e)}"
    
    return results

def calculate_category_breakdown(feature_names, feature_importance):
    """Calculate contribution breakdown by feature categories."""
    categories = {
        'Numerical': ['YearsCodePro', 'Age', 'WorkExp', 'GDP_per_capita', 'Cost_Index'],
        'Education': [f for f in feature_names if f.startswith('EdLevel_')],
        'Work': [f for f in feature_names if f.startswith('RemoteWork_') or f.startswith('OrgSize_') or f.startswith('Employment_')],
        'Experience': [f for f in feature_names if f.startswith('ExperienceLevel_')],
        'Location': [f for f in feature_names if f.startswith('Country_')],
        'Role': [f for f in feature_names if f.startswith('DevType_')],
        'Languages': [f for f in feature_names if f.startswith('Lang_')]
    }
    
    breakdown = {}
    for category, features in categories.items():
        category_contrib = sum([val for feature, val in feature_importance if feature in features])
        if abs(category_contrib) > 0.001:  # Only include significant categories
            breakdown[category] = category_contrib
    
    return breakdown

def print_shap_analysis(results, show_top_n=15):
    """Print SHAP analysis results in a formatted way."""
    if not results['success']:
        print(f"❌ {results['error']}")
        return
    
    print("\n" + "="*50)
    print("SHAP ANALYSIS - Feature Importance")
    print("="*50)
    
    # Display top features
    print(f"\nTop {show_top_n} Most Important Features:")
    print("-" * 40)
    for i, (feature, shap_val) in enumerate(results['feature_importance'][:show_top_n]):
        impact = "📈" if shap_val > 0 else "📉"
        print(f"{i+1:2d}. {impact} {feature:<40} {shap_val:>8.4f}")
    
    # Display summary
    summary = results['summary']
    print(f"\n📊 Summary:")
    print(f"   Total positive contributions: {summary['positive_contributions']:.4f}")
    print(f"   Total negative contributions: {summary['negative_contributions']:.4f}")
    print(f"   Net contribution: {summary['positive_contributions'] + summary['negative_contributions']:.4f}")
    print(f"   Base value (model intercept): {summary['intercept']:.4f}")
    
    # Display category breakdown
    print(f"\n📋 Feature Category Breakdown:")
    print("-" * 30)
    for category, contrib in results['category_breakdown'].items():
        print(f"   {category:<12}: {contrib:>8.4f}")

def get_shap_insights(results, top_n=5):
    """Get key insights from SHAP analysis for display in UI."""
    if not results['success']:
        return []
    
    insights = []
    
    # Top positive contributors
    positive_features = [(f, v) for f, v in results['feature_importance'] if v > 0][:top_n]
    if positive_features:
        insights.append({
            'type': 'positive',
            'title': 'Top Salary Boosters',
            'features': [{'name': f, 'value': v} for f, v in positive_features]
        })
    
    # Top negative contributors
    negative_features = [(f, v) for f, v in results['feature_importance'] if v < 0][:top_n]
    if negative_features:
        insights.append({
            'type': 'negative',
            'title': 'Top Salary Reducers',
            'features': [{'name': f, 'value': v} for f, v in negative_features]
        })
    
    # Category insights
    category_insights = []
    for category, contrib in results['category_breakdown'].items():
        if abs(contrib) > 0.01:  # Only significant categories
            category_insights.append({
                'category': category,
                'contribution': contrib,
                'impact': 'positive' if contrib > 0 else 'negative'
            })
    
    if category_insights:
        insights.append({
            'type': 'category',
            'title': 'Category Impact',
            'categories': category_insights
        })
    
    return insights
