##📊 Superstore Sales Data Analysis Project
This project is a complete end-to-end data analysis pipeline on the Superstore dataset using Python and Power BI. It involves data cleaning, exploratory data analysis (EDA), and interactive dashboarding to derive meaningful business insights.

##🗂️ Project Structure

sales/
│
├── analysis/
│   ├── analysis.py        # Data cleaning and preprocessing script
│   └── eda.py             # Script for generating EDA visualizations (PNG)
│
├── Output/
│   ├── sample.csv         # Cleaned dataset for Power BI
│   ├── *.png              # Charts created by EDA script
│   └── superstore.pbix    # Power BI dashboard file
│
└── data/
    └── superstore.csv     # Raw dataset


## 🔧 Technologies Used

- **Python** (Pandas, Matplotlib, Seaborn)
- **Power BI** (Dashboard, KPI cards, Line, Pie)
- **VS Code** for development

---

## 🧹 Data Preprocessing Highlights (`analysis.py`)

- Renamed columns for consistency.
- Converted date columns to datetime.
- Removed duplicates.
- Added calculated fields:
  - `order_month`: Monthly period grouping
  - `profit_margin`: Profit to Sales ratio
- Exported cleaned data as `sample.csv` for use in Power BI.


## 📈 Exploratory Data Analysis (`eda.py`)

The EDA script produced insights through visualizations such as:

- **Sales vs. Profit by Category/Sub-Category**
- **Region-wise Performance**
- **Monthly Sales Trend**
- **Top 10 Customers by Revenue**
- **State-wise Sales Heatmap**

All charts are saved as PNGs in the `Output/` directory.


## 📊 Power BI Dashboard Highlights

The interactive Power BI dashboard includes:

| Visual Type               | Description                                                              |
|---------------------------|--------------------------------------------------------------------------|
| Dropdown Slicer           | Filter data by city, country, and region                                 |
| Pie Chart                 | Displays the sum of sales and profit by region                           |
| Clustered Column Chart    | Compares total sales and profit across different regions                 |
| Line and Clustered Column | Shows yearly trend of sales and profit                                   |
| Bar Chart                 | Visualizes total yearly sales                                            |
| KPI Card with Area Chart  | Shows monthly sales, profit, and profit margin with KPI target indicator |

✅ **All visuals are interactive and filterable** by region, time period, and location dimensions.

## 📌 Key Business Insights

- 📉 Some states have high sales but low profit margins.
- 📈 Technology is the highest grossing category.
- ⏳ December and November see sales peaks every year.
- 💡 West region contributes the highest revenue consistently.

---

## 📦 Dataset

- **Source**: [Superstore dataset](https://www.kaggle.com/datasets/henrysue/superstore)
- Contains ~10,000 orders with attributes like:
  - Order ID, Order Date, Ship Date
  - Customer & Segment
  - Product, Category, Sub-Category
  - Sales, Profit, Quantity, Discount

---

## 🙌 Final Notes

This project demonstrates practical **data analysis skills**, **Python scripting**, and **BI reporting**. It's a strong portfolio piece for roles in Data Science or Business Intelligence.

> 💬 Feel free to connect if you’d like to extend this into a forecasting model or integrate SQL insights.
