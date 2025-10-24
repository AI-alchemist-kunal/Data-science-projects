import pandas as pd
from scipy.stats import chi2_contingency

def analyze_ab_test(data_path="ab_test_data.csv", alpha=0.05):
    """Loads A/B test data, performs Chi-Squared test, and prints results."""
    print(f"Analyzing data from {data_path}...")
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print(f"Error: {data_path} not found. Run generate_data.py first.")
        return

    # Create contingency table
    contingency_table = pd.crosstab(df['group'], df['converted'])
    print("\n--- Contingency Table ---")
    print(contingency_table)

    # Calculate observed conversion rates
    control_total = contingency_table.loc['control'].sum()
    treatment_total = contingency_table.loc['treatment'].sum()
    control_converted = contingency_table.loc['control', 1]
    treatment_converted = contingency_table.loc['treatment', 1]

    control_cr = control_converted / control_total
    treatment_cr = treatment_converted / treatment_total

    print(f"\nControl Conversion Rate: {control_cr:.4f} ({control_cr * 100:.2f}%)")
    print(f"Treatment Conversion Rate: {treatment_cr:.4f} ({treatment_cr * 100:.2f}%)")
    print(f"Observed Difference: {treatment_cr - control_cr:.4f} ({ (treatment_cr - control_cr) * 100:.2f}%)")

    # Run Chi-Squared test
    chi2_stat, p_value, dof, expected_values = chi2_contingency(contingency_table)

    print(f"\n--- Chi-Squared Test Results ---")
    print(f"Chi-Squared Statistic: {chi2_stat:.4f}")
    print(f"P-Value: {p_value:.4f}")

    if p_value < alpha:
        print(f"Conclusion: The result IS statistically significant (p < {alpha}).")
        recommendation = "SHIP the change."
    else:
        print(f"Conclusion: The result is NOT statistically significant (p >= {alpha}).")
        recommendation = "DO NOT SHIP the change."

    print(f"\nRecommendation: {recommendation}")
    return p_value # Return p-value for potential further use

if __name__ == "__main__":
    # Generate data first (if needed)
    try:
        pd.read_csv("ab_test_data.csv")
    except FileNotFoundError:
        print("Data file not found, generating...")
        import generate_data # Import and run the other script
        df_generated = generate_data.generate_ab_data()
        df_generated.to_csv("ab_test_data.csv", index=False)
        print("Data generated and saved.")

    # Run the analysis
    analyze_ab_test()