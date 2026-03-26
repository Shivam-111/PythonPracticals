import matplotlib.pyplot as plt
import pandas as pd

# Example: reading from CSV
data = pd.read_csv("company_sales_data.csv")

months = data['month_number']
profit = data['total_profit']

plt.plot(months, profit, marker='o', color='blue')
plt.title("Company Profit per Month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()