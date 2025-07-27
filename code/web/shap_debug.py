import joblib
import pandas as pd
import numpy as np
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

# 使用和test_model.py相同的输入
user_input = {
    'YearsCodePro': 5,
    'Age': 30,
    'WorkExp': 7,
    'GDP_per_capita': 50000,
    'Cost_Index': 100
}

selections = {
    'EdLevel': 'Bachelor\'s degree (B.A., B.S., B.Eng., etc.)',
    'RemoteWork': 'Remote',
    'OrgSize': '100 to 499 employees',
    'Country': 'United States',
    'DevType': 'Developer, back-end',
    'Employment': 'Employed, full-time',
    'Languages': ['Python', 'JavaScript']
}

# 创建DataFrame
df = pd.DataFrame(0, index=[0], columns=model.feature_names_in_)

# 填充数值特征
for key, value in user_input.items():
    if key in df.columns:
        df[key] = value

# 计算ExperienceLevel
experience_level = map_experience_level(user_input['YearsCodePro'])

# 填充one-hot编码特征
for feature, selection in selections.items():
    if feature == 'Languages':
        for lang in selection:
            lang_col = f'Lang_{lang}'
            if lang_col in df.columns:
                df[lang_col] = 1
    else:
        col_name = f'{feature}_{selection}'
        if col_name in df.columns:
            df[col_name] = 1

# 处理ExperienceLevel
if experience_level is not None:
    exp_col = f'ExperienceLevel_{experience_level}'
    if exp_col in df.columns:
        df[exp_col] = 1

# 获取模型系数
if hasattr(model, 'named_steps'):
    final_model = model.named_steps[list(model.named_steps.keys())[-1]]
    coefficients = final_model.coef_
    intercept = final_model.intercept_
else:
    coefficients = model.coef_
    intercept = model.intercept_

print("🔍 SHAP值计算详解")
print("="*60)

# 显示模型基本信息
print(f"模型类型: {type(model).__name__}")
if hasattr(model, 'named_steps'):
    print(f"Pipeline中的最终模型: {type(final_model).__name__}")
print(f"模型截距 (intercept): {intercept:.4f}")
print(f"特征数量: {len(coefficients)}")
print()

# 验证SHAP公式: SHAP值 = 特征值 × 模型系数
print("📊 SHAP值计算公式验证:")
print("SHAP值 = 特征值 × 模型系数")
print("-" * 60)

# 获取特征值
feature_values = df.iloc[0].values
feature_names = df.columns.tolist()

# 计算SHAP值
shap_values = feature_values * coefficients

# 显示前10个最重要的特征
print(f"{'排名':<4} {'特征名':<40} {'特征值':<10} {'模型系数':<12} {'SHAP值':<12} {'验证':<8}")
print("-" * 90)

# 创建(特征名, SHAP值)的列表并排序
feature_importance = list(zip(feature_names, shap_values))
feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)

for i, (feature_name, shap_val) in enumerate(feature_importance[:10]):
    feature_val = feature_values[feature_names.index(feature_name)]
    coef = coefficients[feature_names.index(feature_name)]
    
    # 验证计算是否正确
    calculated_shap = feature_val * coef
    is_correct = abs(calculated_shap - shap_val) < 1e-10
    
    print(f"{i+1:<4} {feature_name:<40} {feature_val:<10.2f} {coef:<12.6f} {shap_val:<12.4f} {'✅' if is_correct else '❌'}")

print()
print("💡 解读说明:")
print("="*60)

# 解释为什么GDP_per_capita影响这么大
gdp_index = feature_names.index('GDP_per_capita')
gdp_value = feature_values[gdp_index]
gdp_coef = coefficients[gdp_index]
gdp_shap = shap_values[gdp_index]

print(f"1. GDP_per_capita 为什么影响大:")
print(f"   - 特征值: {gdp_value:,.0f} (美元)")
print(f"   - 模型系数: {gdp_coef:.6f}")
print(f"   - SHAP值: {gdp_value:,.0f} × {gdp_coef:.6f} = {gdp_shap:.4f}")
print(f"   - 解释: GDP越高，工资预测越高，系数表示每增加1美元GDP对工资的影响")

print(f"\n2. Cost_Index 的影响:")
cost_index = feature_names.index('Cost_Index')
cost_value = feature_values[cost_index]
cost_coef = coefficients[cost_index]
cost_shap = shap_values[cost_index]

print(f"   - 特征值: {cost_value}")
print(f"   - 模型系数: {cost_coef:.6f}")
print(f"   - SHAP值: {cost_value} × {cost_coef:.6f} = {cost_shap:.4f}")
print(f"   - 解释: 生活成本指数越高，工资预测越高")

print(f"\n3. 预测结果验证:")
prediction = model.predict(df)[0]
calculated_prediction = intercept + sum(shap_values)
print(f"   - 模型预测: {prediction:.4f}")
print(f"   - 手动计算: {intercept:.4f} + {sum(shap_values):.4f} = {calculated_prediction:.4f}")
print(f"   - 验证: {'✅ 一致' if abs(prediction - calculated_prediction) < 1e-10 else '❌ 不一致'}")

print(f"\n4. 为什么这些值不是1或百分比:")
print(f"   - SHAP值是绝对贡献，不是相对贡献")
print(f"   - 所有SHAP值之和 + 截距 = 最终预测值")
print(f"   - 正值表示增加预测值，负值表示减少预测值")
print(f"   - 数值大小表示影响程度，不是百分比")

print(f"\n5. 实际工资计算:")
actual_salary = np.power(10, prediction)
print(f"   - 对数工资预测: {prediction:.4f}")
print(f"   - 实际工资: ${actual_salary:,.2f}")
print(f"   - 公式: 实际工资 = 10^(对数工资预测)") 