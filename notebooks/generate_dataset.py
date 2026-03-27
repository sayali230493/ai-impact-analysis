import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# random reproducibility
np.random.seed(42)

roles = ['Analyst', 'Data Scientist', 'Engineer']
task_types = ['Reporting', 'Data Cleaning', 'Debugging', 'Modeling', 'Documentation']
ai_tools = ['ChatGPT', 'Claude', 'Copilot', 'Gemini', 'Automation Script', 'None']

rows = 200
data = []

for i in range(1, rows+1):
    role = random.choice(roles)
    task_type = random.choice(task_types)
    
    # Base time by role
    if role == 'Analyst':
        time_before = np.random.normal(4, 0.8)  # hours
    elif role == 'Data Scientist':
        time_before = np.random.normal(5, 1)
    else:
        time_before = np.random.normal(3, 0.7)
    
    # Time after AI
    ai_tool_used = random.choice(ai_tools)
    if ai_tool_used != 'None':
        time_after = max(time_before - np.random.uniform(0.5, 2.0), 0.5)
        quality_before = random.randint(6, 9)
        quality_after = min(quality_before + random.randint(0,2), 10)
    else:
        time_after = time_before
        quality_before = random.randint(6, 9)
        quality_after = quality_before
    
    # Random date in last 60 days
    date = datetime.today() - timedelta(days=random.randint(0,60))
    
    data.append([
        i, role, task_type, round(time_before,2), round(time_after,2),
        quality_before, quality_after, ai_tool_used, date.date()
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'employee_id','role','task_type','time_before_ai','time_after_ai',
    'output_quality_before','output_quality_after','ai_tool_used','date'
])

# Save to CSV
df.to_csv('../data_productivity.csv', index=False)
print("Dataset created with 200 rows at data_productivity.csv")
