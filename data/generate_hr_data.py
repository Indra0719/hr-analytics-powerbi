import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

n = 1000
departments = ['Engineering', 'Sales', 'HR', 'Finance', 'Marketing', 'Operations']
job_levels = ['Junior', 'Mid', 'Senior', 'Manager', 'Director']
education = ['High School', 'Bachelor', 'Master', 'PhD']
gender = ['Male', 'Female']

dept = np.random.choice(departments, n, p=[0.3, 0.2, 0.1, 0.15, 0.15, 0.1])
level = np.random.choice(job_levels, n, p=[0.3, 0.3, 0.2, 0.15, 0.05])
age = np.random.randint(22, 60, n)
tenure = np.random.randint(1, 20, n)
salary_base = {
    'Junior': (40000, 65000),
    'Mid': (60000, 90000),
    'Senior': (85000, 130000),
    'Manager': (110000, 160000),
    'Director': (150000, 220000)
}
salary = [round(random.uniform(*salary_base[l]), -2) for l in level]
satisfaction = np.random.randint(1, 6, n)
performance = np.random.randint(1, 6, n)
work_life = np.random.randint(1, 6, n)

# Attrition logic
attrition_prob = (
    0.15
    + (satisfaction < 3) * 0.2
    + (tenure < 3) * 0.15
    + (work_life < 3) * 0.1
    - (level == 'Director') * 0.1
    - (tenure > 10) * 0.1
)
attrition_prob = np.clip(attrition_prob, 0.05, 0.95)
attrition = np.random.binomial(1, attrition_prob, n)

df = pd.DataFrame({
    'employee_id': [f'EMP-{i:04d}' for i in range(1, n+1)],
    'age': age,
    'gender': np.random.choice(gender, n),
    'department': dept,
    'job_level': level,
    'education': np.random.choice(education, n, p=[0.1, 0.5, 0.3, 0.1]),
    'tenure_years': tenure,
    'salary': salary,
    'satisfaction_score': satisfaction,
    'performance_score': performance,
    'work_life_balance': work_life,
    'attrition': attrition
})

df['attrition_label'] = df['attrition'].map({1: 'Yes', 0: 'No'})
df.to_csv('data/hr_data.csv', index=False)
print(f'Dataset created: {len(df)} rows')
print(f'Attrition rate: {df["attrition"].mean():.1%}')
print(df.head())
