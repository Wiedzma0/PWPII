import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Połączenie z bazą
conn = sqlite3.connect(r'C:\Users\aleks\Desktop\Studia\JWPII\lab8\sales.db')
c = conn.cursor()

# Funkcja do dodawania danych
def add_sale(product, quantity, price, date, lat, lon):
    c.execute("INSERT INTO sales (product, quantity, price, date, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)",
              (product, quantity, price, date, lat, lon))
    conn.commit()

# Pobierz wszystkie dane
def get_data():
    return pd.read_sql_query("SELECT * FROM sales", conn)

# Tytuł
st.title("Aplikacja sprzedaży")

# Formularz dodawania
st.subheader("Dodaj nową sprzedaż")
with st.form("add_form"):
    product = st.text_input("Produkt")
    quantity = st.number_input("Ilość", min_value=1, step=1)
    price = st.number_input("Cena", min_value=0.0, step=0.01)
    date = st.date_input("Data")
    lat = st.number_input("Szerokość (latitude)")
    lon = st.number_input("Długość (longitude)")
    submitted = st.form_submit_button("Dodaj")

    if submitted:
        add_sale(product, quantity, price, date.strftime("%Y-%m-%d"), lat, lon)
        st.success("Sprzedaż dodana!")
        st.balloons()

# Pobierz dane
df = get_data()

# Filtrowanie
st.subheader("Filtrowanie danych")
products = df['product'].unique().tolist()
selected_product = st.selectbox("Wybierz produkt", ["Wszystkie"] + products)

if selected_product != "Wszystkie":
    df = df[df['product'] == selected_product]

# Tabela
st.subheader("Tabela danych")
st.dataframe(df)

# Wykres 1: Sprzedaż dzienna
df['total_value'] = df['quantity'] * df['price']
daily_sales = df.groupby('date')['total_value'].sum()

st.subheader("Wartość sprzedaży dziennie")
fig1, ax1 = plt.subplots()
daily_sales.plot(kind='bar', ax=ax1)
st.pyplot(fig1)

# Wykres 2: Ilość wg produktu
by_product = df.groupby('product')['quantity'].sum()
st.subheader("Liczba sprzedanych produktów")
fig2, ax2 = plt.subplots()
by_product.plot(kind='bar', color='green', ax=ax2)
st.pyplot(fig2)

# Mapa
st.subheader("Mapa sprzedaży")
if 'latitude' in df.columns and 'longitude' in df.columns:
    map_data = df[['latitude', 'longitude']].dropna()
    st.map(map_data)
