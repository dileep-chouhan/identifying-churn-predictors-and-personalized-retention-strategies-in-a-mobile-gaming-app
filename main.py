import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Number of users
num_users = 1000
# Generate synthetic user data
data = {
    'user_id': range(1, num_users + 1),
    'days_active': np.random.randint(1, 365, num_users),  # Days active in the last year
    'sessions_per_day': np.random.poisson(2, num_users), # Average sessions per day
    'in_app_purchases': np.random.poisson(1, num_users), # Number of in-app purchases
    'average_session_duration': np.random.normal(15, 5, num_users), # Average session duration in minutes
    'churned': np.random.binomial(1, 0.2, num_users) # Churned (1) or not (0)
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Feature Engineering ---
# No significant cleaning needed for this synthetic data
# --- 3. Exploratory Data Analysis and Visualization ---
# Churn Rate
churn_rate = df['churned'].mean()
print(f"Overall Churn Rate: {churn_rate:.2%}")
# Visualize churn rate
plt.figure(figsize=(6, 4))
sns.countplot(x='churned', data=df)
plt.title('Churn Distribution')
plt.xlabel('Churned (1=Yes, 0=No)')
plt.ylabel('Number of Users')
plt.savefig('churn_distribution.png')
print("Plot saved to churn_distribution.png")
# Relationship between days active and churn
plt.figure(figsize=(8, 6))
sns.boxplot(x='churned', y='days_active', data=df)
plt.title('Days Active vs. Churn')
plt.xlabel('Churned (1=Yes, 0=No)')
plt.ylabel('Days Active')
plt.savefig('days_active_vs_churn.png')
print("Plot saved to days_active_vs_churn.png")
#Correlation Analysis
correlation_matrix = df[['days_active', 'sessions_per_day', 'in_app_purchases', 'average_session_duration', 'churned']].corr()
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
print("Plot saved to correlation_matrix.png")
#Statistical Tests (example using t-test)
#Test if average session duration differs significantly between churned and non-churned users.
churned_users = df[df['churned'] == 1]['average_session_duration']
non_churned_users = df[df['churned'] == 0]['average_session_duration']
t_statistic, p_value = stats.ttest_ind(churned_users, non_churned_users)
print(f"T-test results (Average Session Duration): t-statistic = {t_statistic:.2f}, p-value = {p_value:.3f}")
# --- 4.  Retention Strategy Recommendations (based on analysis)---
#  (This section would typically involve more sophisticated modeling and prediction, 
#   but for this example, we'll provide high-level recommendations based on the EDA)
print("\nRetention Strategy Recommendations:")
if churn_rate > 0.15: #Example threshold
    print("- Focus on increasing user engagement: Implement features to encourage more frequent and longer sessions.")
    print("- Reward loyal users: Offer in-game rewards or discounts to incentivize continued play.")
    print("- Personalize the experience: Tailor game content and offers based on user preferences and behavior.")
else:
    print("- Maintain current strategies. Monitor key engagement metrics closely.")
print("- Conduct further analysis using more advanced techniques (e.g., survival analysis, machine learning models) to identify more precise predictors of churn and develop more targeted retention strategies.")