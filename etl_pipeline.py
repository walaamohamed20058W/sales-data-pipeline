import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# ------------------------
# 1. Extract: قراءة البيانات من CSV
# ------------------------
df = pd.read_csv("sales.csv")

# حساب العمود Total = Quantity * Price
df["Total"] = df["Quantity"] * df["Price"]

print("✅ Data Loaded:")
print(df.head())

# ------------------------
# 2. Transform: تنظيف البيانات (لو في Missing أو Errors)
# ------------------------
df["Date"] = pd.to_datetime(df["Date"])  # تحويل التاريخ
df.dropna(inplace=True)  # حذف أي بيانات ناقصة

# ------------------------
# 3. Load: تخزين البيانات في SQLite
# ------------------------
conn = sqlite3.connect("sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Data saved into sales.db")

# ------------------------
# 4. SQL Queries: تحليل المبيعات شهريًا
# ------------------------
query = """
SELECT strftime('%Y-%m', Date) AS YearMonth,
       SUM(Total) AS TotalSales
FROM sales
GROUP BY YearMonth
ORDER BY YearMonth;
"""

monthly_sales = pd.read_sql(query, conn)
print("✅ Monthly Sales:")
print(monthly_sales)

# ------------------------
# 5. Visualization: رسم النتائج
# ------------------------
plt.figure(figsize=(6,4))
plt.plot(monthly_sales["YearMonth"], monthly_sales["TotalSales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.show()

conn.close()
