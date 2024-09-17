# sales_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# Set your folder path
folder_path = r'C:\Users\Janay\OneDrive\Desktop\sales analysis'

# Step 1: Read data from Excel file
data_file = os.path.join(folder_path, 'sales_data.xlsx')
df = pd.read_excel(data_file)

# Step 2: Data Preprocessing
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Data Analysis
total_sales = df['Sales'].sum()
print(f"Total Sales: ${total_sales:,.2f}")

sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(sales_by_region)

df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

# Step 4: Data Visualization
# Sales by Region Bar Chart
plt.figure(figsize=(8, 6))
sales_by_region.plot(kind='bar', color='skyblue')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig(os.path.join(folder_path, 'sales_by_region.png'))
plt.show()

# Monthly Sales Line Chart
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', linestyle='-')
plt.title('Monthly Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig(os.path.join(folder_path, 'monthly_sales.png'))
plt.show()

# Step 5: Export Results to Excel
output_file = os.path.join(folder_path, 'sales_analysis_results.xlsx')
with pd.ExcelWriter(output_file) as writer:
    sales_by_region.to_frame().to_excel(writer, sheet_name='Sales by Region')
    monthly_sales.to_frame().to_excel(writer, sheet_name='Monthly Sales')

print(f"\nAnalysis results have been saved to '{output_file}'")
