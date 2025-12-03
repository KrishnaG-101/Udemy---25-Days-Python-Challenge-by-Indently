import csv
import matplotlib.pyplot as plt

# DATA
# Monthly
# monthly_income : float = 24_000
# monthly_rent : float = 4500
# food_expenses : float = 3400
# other_expenses : float = 3200
# tax_rate : float = 0.10
# tax_amount : float = monthly_income * tax_rate

with open("data.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        monthly_income : float = float(row["income"])
        monthly_rent : float = float(row["rent"])
        food_expenses : float = float(row["food"])
        other_expenses : float = float(row["other"])
        tax_rate : float = float(row["tax_rate"])
        tax_amount : float = monthly_income * tax_rate

# Yearly
yearly_income : float = monthly_income * 12
yearly_expenses : float = sum([monthly_rent, food_expenses, other_expenses, tax_amount]) * 12
yearly_savings : float = yearly_income - yearly_expenses 

# TICKERS
monthly_tickers : list[str] = ["Income", "Rent", "Food", "Taxes", "Other"]
monthly_amounts : list[float] = [monthly_income, monthly_rent, food_expenses, tax_amount, other_expenses]
monthly_colors : list[str] = ["green", "red", "red", "red", "red"]
yearly_tickers : list[str] = ["Income", "Expenses", "Savings"]
yearly_amounts : list[float] = [yearly_income, yearly_expenses, yearly_savings]
yearly_colors : list[str] = ["green", "red", "green"]

# PRESENTATION
fig, axes = plt.subplots(1, 2, figsize=(10, 6))

# Monthly Bar Chart
axes[0].bar(monthly_tickers, monthly_amounts, color=monthly_colors)
axes[0].set_title("Monthly Financial Overview")
axes[0].set_ylabel("Amount ($)")
axes[0].tick_params(axis="x", rotation=30)

# Yearly Bar Chart
axes[1].bar(yearly_tickers, yearly_amounts, color=yearly_colors)
axes[1].set_title("Monthly Financial Overview")
axes[1].set_ylabel("Amount ($)")
axes[1].tick_params(axis="x", rotation=30)

# Display
plt.tight_layout()
plt.show()