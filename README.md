This project aims to create a financial forecasting model using three powerful tools: Excel, Python, and R. Each tool has a specific purpose to streamline the process of forecasting revenue, expenses, and profit margins over a three-year period. Here’s how it works:

1. Excel: Initial Setup
The project starts with Excel to set up the core financial calculations. Excel's ease of use makes it the perfect tool for inputting data such as initial revenue, expenses, and the growth rate. It also serves as a good foundation for anyone wanting to interact with the data manually before automating the process further.

2. Python: Automating Calculations
Once the initial data is set, Python steps in to automate the forecasting process. Using libraries like pandas and numpy, a script reads financial assumptions (e.g., revenue growth rate, profit margins) and then calculates forecasts for future years. The results, including revenue, expenses, and profit margins, are exported into an Excel file, making it easy to review and refine.

Python Code Breakdown:
Assumptions: Annual growth rate, initial revenue, and expenses are defined.
Calculations: Forecasts are computed for each year, with key metrics like revenue, expenses, profit, and profit margin.
Output: The results are saved in a new Excel file (financial_model.xlsx) for easy access and further analysis.
3. R: Data Visualization and Analysis
Finally, R is used for analyzing and visualizing the financial data. The ggplot2 library is employed to create a plot that compares revenue and expenses over the three-year forecast period. The graphical output provides clear insights into the financial health of the model, helping stakeholders visualize trends at a glance.

R Code Breakdown:
Assumptions and Data Generation: Similar to Python, R generates forecast data based on the assumptions.
Visualization: A plot is generated to display the growth of revenue and expenses over time.
Output: The forecast data is also saved into an Excel file (financial_model.xlsx), and the plot is displayed as a visual summary of the forecast.
Key Features:
Ease of Setup: Use Excel to manually input and modify assumptions.
Automation: Python automates the forecast calculations, making the process faster and reducing manual errors.
Visualization: R adds a layer of data analysis by visualizing revenue and expenses over time.
How to Run the Project:
Excel Setup: Start by entering your assumptions (growth rates, initial figures) into Excel, or use the Python script to automate this part.
Python Script: Run financial_model.py to automate the calculation of the forecast, and it will output an Excel file with the forecast data.
R Script: Run financial_model.R to visualize the forecast trends using graphs.
Libraries Used:
Python: pandas, numpy, openpyxl
R: readxl, writexl, ggplot2
Output:
Excel File: financial_model.xlsx
Plot: Visualization of financial trends over time.



![sales_over_time](https://github.com/user-attachments/assets/9d37aaca-96d8-4f7e-b82b-a853fc4446ec)
[sales_data.xlsx](https://github.com/user-attachments/files/17028623/sales_data.xlsx)
![sales_by_region](https://github.com/user-attachments/assets/9b74289e-3403-4dbb-81ce-8914dc52a7f9)
![sales_by_product](https://github.com/user-attachments/assets/44e20f04-cd79-4b20-b867-e0d0621541ef)
