import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/churn.csv")

# Standardize column names
df.columns = df.columns.str.lower()

# Create visuals folder if it doesn't exist
os.makedirs("visuals", exist_ok=True)

# ---------------------------
# 1. Churn Distribution
# ---------------------------
churn_counts = df['churn'].value_counts()

plt.figure()
plt.bar(churn_counts.index, churn_counts.values)
plt.title("Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.savefig("visuals/churn_distribution.png")
plt.close()

# ---------------------------
# 2. Churn by Contract Type
# ---------------------------
contract_churn = df.groupby('contract_type')['churn'].value_counts().unstack()

contract_churn.plot(kind='bar', stacked=True)
plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.savefig("visuals/churn_by_contract.png")
plt.close()

# ---------------------------
# 3. Tenure vs Churn
# ---------------------------
plt.figure()
plt.hist(df[df['churn'] == 'Yes']['tenure_months'], alpha=0.5, label='Churned')
plt.hist(df[df['churn'] == 'No']['tenure_months'], alpha=0.5, label='Retained')
plt.title("Tenure Distribution by Churn")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")
plt.legend()
plt.savefig("visuals/churn_by_tenure.png")
plt.close()

# ---------------------------
# 4. Monthly Charges Distribution
# ---------------------------
plt.figure()
plt.hist(df['monthly_charges'], bins=20)
plt.title("Monthly Charges Distribution")
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.savefig("visuals/monthly_charges_distribution.png")
plt.close()

# ---------------------------
# Summary Output
# ---------------------------
print("Churn Rate:")
print(df['churn'].value_counts(normalize=True))