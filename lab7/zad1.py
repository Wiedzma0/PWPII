import sqlite3
import pandas as pd

conn = sqlite3.connect(r'C:\Users\aleks\Desktop\Studia\JWPII\lab7\sales.db')  # Ścieżkę dostosuj do lokalizacji pliku

# a) Sprzedaż produktu „Laptop”
laptops = pd.read_sql_query("SELECT * FROM sales WHERE product = 'Laptop';", conn)

# b) Dane tylko z dni 2025-05-07 i 2025-05-08
selected_dates = pd.read_sql_query("""
    SELECT * FROM sales 
    WHERE date IN ('2025-05-07', '2025-05-08');
""", conn)

# c) Transakcje z ceną jednostkową > 200 zł
high_price = pd.read_sql_query("SELECT * FROM sales WHERE price > 200;", conn)

# d) Łączna wartość sprzedaży dla każdego produktu
total_value = pd.read_sql_query("""
    SELECT product, SUM(quantity * price) as total_sales 
    FROM sales 
    GROUP BY product;
""", conn)

# e) Dzień z największą liczbą sprzedanych sztuk
busiest_day = pd.read_sql_query("""
    SELECT date, SUM(quantity) as total_quantity 
    FROM sales 
    GROUP BY date 
    ORDER BY total_quantity DESC 
    LIMIT 1;
""", conn)

conn.close()

# Wyświetl wyniki
print("a) Laptop sales:\n", laptops)
print("\nb) Sales on 2025-05-07 and 2025-05-08:\n", selected_dates)
print("\nc) Transactions with price > 200:\n", high_price)
print("\nd) Total sales per product:\n", total_value)
print("\ne) Day with highest quantity sold:\n", busiest_day)
