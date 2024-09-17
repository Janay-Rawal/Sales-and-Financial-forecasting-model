# sales_analysis.R

# Load required libraries
library(readxl)
library(ggplot2)

# Step 1: Read data from Excel file
data_file <- "sales_data.xlsx"
df <- read_excel(data_file)

# Step 2: Data Preprocessing
# Convert 'Date' column to Date format
df$Date <- as.Date(df$Date)

# Step 3: Data Analysis
# Calculate total sales
total_sales <- sum(df$Sales)
cat(sprintf("Total Sales: $%0.2f\n", total_sales))

# Calculate sales by product
sales_by_product <- aggregate(Sales ~ Product, data = df, sum)
cat("\nSales by Product:\n")
print(sales_by_product)

# Step 4: Data Visualization
# Sales by Product Bar Chart
ggplot(sales_by_product, aes(x = Product, y = Sales, fill = Product)) +
  geom_bar(stat = "identity") +
  ggtitle("Sales by Product") +
  xlab("Product") +
  ylab("Total Sales") +
  theme_minimal()

# Save the plot
ggsave("sales_by_product.png")

# Sales Over Time Line Chart
ggplot(df, aes(x = Date, y = Sales, color = Product)) +
  geom_line() +
  ggtitle("Sales Over Time by Product") +
  xlab("Date") +
  ylab("Sales") +
  theme_minimal()

# Save the plot
ggsave("sales_over_time.png")

# Step 5: Export Results to Excel
# Install the writexl package if not installed
# install.packages("writexl")
library(writexl)

write_xlsx(list("Sales by Product" = sales_by_product), "sales_analysis_results_R.xlsx")

cat("\nAnalysis results have been saved to 'sales_analysis_results_R.xlsx'\n")



