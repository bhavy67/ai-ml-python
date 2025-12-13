from ast import literal_eval
import math

# Function to calculate portfolio risk
def analyze_portfolio_risk(data):
    daily_returns, variance_threshold, std_dev_threshold = data
    n = len(daily_returns)

    if n <= 1:
        return 'Low Risk: Within Acceptable Limits'

    mean_return = sum(daily_returns) / n

    variance = sum((r - mean_return) ** 2 for r in daily_returns) / n

    std_dev = math.sqrt(variance)

    variance_exceeds = variance > variance_threshold
    std_exceeds = std_dev > std_dev_threshold

    if variance_exceeds and std_exceeds:
        return 'High Risk: Exceeds Both Thresholds'
    elif variance_exceeds:
        return 'Moderate Risk: High Variance Only'
    elif std_exceeds:
        return 'Moderate Risk: High Standard Deviation Only'
    else:
        return 'Low Risk: Within Acceptable Limits'


# Taking the input as a tuple (do not edit)
data = literal_eval(input())

# Calculate and output the risk status
print(analyze_portfolio_risk(data))