# Project 1: A/B Test Analysis & Product Recommendation

## 1. Business Problem
The product team is considering changing the color of the main "Checkout" button on our e-commerce site from its current blue to a new green, based on a hypothesis that green implies "go" and will increase conversions.

My task is to run an A/B test, analyze the results, and provide a clear "ship / no-ship" recommendation.

## 2. Hypothesis
* **Null Hypothesis ($H_0$):** There is no statistically significant difference in the conversion rate between the blue button (control) and the green button (treatment).
* **Alternative Hypothesis ($H_A$):** The conversion rate of the green button (treatment) is higher than that of the blue button (control).
* **Significance Level:** $\alpha = 0.05$

## 3. Analysis & Results
I ran a test on 10,000 users, split randomly between the two versions. The analysis was performed using a Chi-Squared test for independence.

*(Note: The data for this analysis was synthetically generated for portfolio purposes. The full analysis notebook can be found at `analysis.ipynb`.)*

### Key Results:
* **Control (Blue Button):** Converted at **10.12%**
* **Treatment (Green Button):** Converted at **10.65%**
* **Observed Lift:** +0.53%
* **P-Value:** **0.3458**

## 4. Recommendation: DO NOT SHIP
My recommendation is to **NOT SHIP** this change.

**Reasoning:**
The p-value of 0.3458 is significantly higher than our 0.05 significance level. This means we **fail to reject the null hypothesis**.

The 0.53% lift we observed is **not statistically significant** and is very likely due to random chance. Shipping this change would consume engineering resources for no provable benefit. We should instead test a new hypothesis, such as changing the *text* on the button (e.g., "Complete Purchase" vs. "Buy Now").