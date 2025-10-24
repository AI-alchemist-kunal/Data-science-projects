import pandas as pd
import numpy as np

def generate_ab_data(n_users=10000, control_cr=0.10, treatment_cr=0.105):
    """Generates synthetic A/B test data."""
    print(f"Generating data for {n_users} users...")
    groups = np.random.choice(['control', 'treatment'], n_users)
    data = []
    for group in groups:
        if group == 'control':
            converted = np.random.binomial(1, control_cr)
        else:
            converted = np.random.binomial(1, treatment_cr)
        data.append({'group': group, 'converted': converted})

    df = pd.DataFrame(data)
    df['user_id'] = range(1, n_users + 1)
    df = df[['user_id', 'group', 'converted']]
    print("Data generation complete.")
    return df

if __name__ == "__main__":
    # This block runs only if the script is executed directly
    df_data = generate_ab_data()
    # Save the data to a CSV for the analysis script to use
    output_path = "ab_test_data.csv"
    df_data.to_csv(output_path, index=False)
    print(f"Synthetic A/B test data saved to {output_path}")
    print(df_data.head())