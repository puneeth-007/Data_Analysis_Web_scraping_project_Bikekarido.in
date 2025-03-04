import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Bike Karido",
    page_icon=":bike:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('Bike Karido Used bikes data',color='green')

f = pd.read_csv(r'C:\Users\punee\OneDrive\Desktop\python\web scraping\DA_PROJECT\bikekarido_old.csv', sep='|')
fdf = pd.DataFrame(f)
fdf = fdf.drop(columns='Unnamed: 0')

fdf['Price'] = pd.to_numeric(fdf['Price'], errors='coerce')
fdf['Registration_Year'] = pd.to_numeric(fdf['Registration_Year'], errors='coerce')
fdf['KMs_Driven'] = pd.to_numeric(fdf['KMs_Driven'], errors='coerce')

default_price = 10000
default_price1 = 1000000

Price_range_lower = st.number_input("Enter the Lower price:", min_value=500, max_value=10000000, key='price_lower', value=default_price)
Price_range_upper = st.number_input("Enter the Upper price:", min_value=500, max_value=10000000, key='price_upper', value=default_price1)
ownership = st.selectbox("Select Ownership", ['All','First', 'Second', 'Third', 'Above'])
company = st.selectbox("Select Company (leave empty to fetch all):", ["All"] + list(fdf['Make'].unique()), key='company')
registration_year = st.selectbox("Enter Year of Registration:", ["All"] + list(map(str, range(2000, 2025))), key='registration_year')

if st.button("Fetch data"):
    if Price_range_lower:
        if Price_range_upper:
            fdf1 = fdf[(fdf['Price'] >= Price_range_lower) & (fdf['Price'] <= Price_range_upper)]
        else:
            fdf1 = fdf[fdf['Price'] >= Price_range_lower]
    else:
        if Price_range_upper:
            fdf1 = fdf[fdf['Price'] <= Price_range_upper]
        else:
            fdf1 = fdf
    if ownership != 'All':
        if ownership:
            fdf2 = fdf1[fdf1['Ownership'] == ownership]
        else:
            fdf2 = fdf1
    else:
        fdf2 = fdf1

    if registration_year != "All":
        if registration_year:
            fdf3 = fdf2[fdf2['Registration_Year'] == int(registration_year)]
        else:
            fdf3 = fdf2
    else:
        fdf3 = fdf2

    if company != "All":
        fdf4 = fdf3[fdf3['Make'] == company]
    else:
        fdf4 = fdf3
    st.write(fdf4)

    fig = px.scatter(
        fdf4,
        x="Price",
        y="Registration_Year",
        color="Ownership",
        size="Price",
        hover_data=["KMs_Driven", "Model", "Make"],
    )
    st.plotly_chart(fig, key="Price")

    fig1 = px.sunburst(fdf4, path=['Location', 'Make', 'Name'], values='Price', color='Location')
    st.plotly_chart(fig1, key='Make')
