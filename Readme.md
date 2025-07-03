# 🧱 Cement Bag Loading Forecasting using Prophet

This is my  project where I used **Meta's Prophet** model to forecast the number of cement bags loaded per day.

---

## 📌 What It Does

- Reads synthetic daily cement loading data  
- Forecasts next 7 days of cement loading  
- Plots past (blue) and future (green) values using Plotly  
- Prints future predicted values in the terminal  

---

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

2. Run the forecast script:
python forecast.py

yaml
Copy
Edit

3. Output:
- Forecast graph saved as `forecast_plot.png`
- Predicted values printed in the terminal

---

## 📁 Files in the Project

- `cement_data.csv` – the input data  
- `forecast.py` – main code to forecast  
- `forecast_plot.png` – the output graph  
- `requirements.txt` – required libraries  
- `README.md` – this file  

---

## 🛠 Libraries Used

- prophet  
- pandas  
- plotly  
- matplotlib  

---

## 📈 Example Output (Terminal)
Date Predicted Lower Bound Upper Bound
2025-07-01 2038.72 1799.62 2282.79
2025-07-02 2285.97 2030.78 2543.71
...

yaml
Copy
Edit

---

## 🙋‍♂️ Author

**Shenbaga ganeshan S**, Final Year AI & Data Science Student  
> “Using AI to solve real-world problems” 