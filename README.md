# Sales Data ETL Pipeline
This project demonstrates a simple Data Engineering ETL pipeline built with Python. The pipeline extracts raw sales data, transforms it, loads it into a database, and generates analytics & visualizations.
Project Workflow:
- **Extract**: Read raw sales data from `sales.csv`.
- **Transform**: Clean and preprocess data (handle dates, missing values). Add a `Total` column (`Quantity × Price`).
- **Load**: Store transformed data into an SQLite database `sales.db`.
- **Analytics**: Calculate monthly sales using SQL aggregation.
- **Visualization**: Generate a line chart for sales trends using Matplotlib.
Tech Stack:
- Python 3
- Pandas – Data cleaning & transformation
- SQLite3 – Database storage
- Matplotlib – Visualization
Project Structure:
- `sales.csv` → Raw sales data
- `etl_pipeline.py` → ETL script (main pipeline)
- `sales.db` → SQLite database (generated after running pipeline)
- `README.md` → Project documentation
Example Output (Monthly Sales Table):
YearMonth | TotalSales
2025-01   | 6100
2025-02   | 1900
2025-03   | 1700
2025-04   | 2600
How to Run:
1. Clone this repository:
   git clone https://github.com/USERNAME/sales-data-pipeline.git
   cd sales-data-pipeline
2. Install dependencies:
   pip install pandas matplotlib
3. Run the pipeline:
   python etl_pipeline.py
Future Improvements:
- Automate pipeline scheduling using Airflow or Prefect.
- Add real-time data ingestion via APIs.
- Enhance dashboard using Streamlit or Power BI.
Author: [Your Name](# Sales Data ETL Pipeline
This project demonstrates a simple Data Engineering ETL pipeline built with Python. The pipeline extracts raw sales data, transforms it, loads it into a database, and generates analytics & visualizations.
Project Workflow:
- **Extract**: Read raw sales data from `sales.csv`.
- **Transform**: Clean and preprocess data (handle dates, missing values). Add a `Total` column (`Quantity × Price`).
- **Load**: Store transformed data into an SQLite database `sales.db`.
- **Analytics**: Calculate monthly sales using SQL aggregation.
- **Visualization**: Generate a line chart for sales trends using Matplotlib.
Tech Stack:
- Python 3
- Pandas – Data cleaning & transformation
- SQLite3 – Database storage
- Matplotlib – Visualization
Project Structure:
- `sales.csv` → Raw sales data
- `etl_pipeline.py` → ETL script (main pipeline)
- `sales.db` → SQLite database (generated after running pipeline)
- `README.md` → Project documentation
Example Output (Monthly Sales Table):
YearMonth | TotalSales
2025-01   | 6100
2025-02   | 1900
2025-03   | 1700
2025-04   | 2600
How to Run:
1. Clone this repository:
   git clone https://github.com/USERNAME/sales-data-pipeline.git
   cd sales-data-pipeline
2. Install dependencies:
   pip install pandas matplotlib
3. Run the pipeline:
   python etl_pipeline.py
Future Improvements:
- Automate pipeline scheduling using Airflow or Prefect.
- Add real-time data ingestion via APIs.
- Enhance dashboard using Streamlit or Power BI.
Author: [Your Name](https://www.linkedin.com/in/YOUR-LINKEDIN)
