"""
Regulatory Testing Framework - Beginner Project
-----------------------------------------------
Simulates a simple regulatory test check for model outputs.

Author: Nithya Gaddam
"""

import pandas as pd

# ✅ Step 1: Sample model output
def load_model_output():
    data = {
        "CustomerID": [1, 2, 3, 4],
        "RiskScore": [0.2, 0.8, 0.5, 0.9]
    }
    df = pd.DataFrame(data)
    print("✅ Model output loaded:")
    print(df)
    return df

# ✅ Step 2: Apply rule-based validation
def run_regulatory_test(df):
    # Example: flagging high-risk customers for review
    df["Flagged"] = df["RiskScore"].apply(lambda x: "Yes" if x >= 0.7 else "No")
    print("\n✅ Regulatory test completed:")
    print(df)
    return df

# ✅ Step 3: Save report
def save_report(df):
    df.to_csv("regulatory_test_report.csv", index=False)
    print("\n✅ Report saved to 'regulatory_test_report.csv'")

if __name__ == "__main__":
    model_output = load_model_output()
    tested_output = run_regulatory_test(model_output)
    save_report(tested_output)
    print("\n🚀 Regulatory Testing Framework completed successfully!")
