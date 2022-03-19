from numpy import isin
import pandas as pd
import streamlit as st

# Data import & columns
df = pd.read_csv(r"C:\Users\mmadh\Documents\Python\New_Proj\Assignment-Business-Quant.csv")

df.Sales.shift(1)
df['Sales Last Year'] = df.Sales.shift(1)

df['Sales Growth %'] = ((((df['Sales']/df['Sales Last Year']) -1)*100).round(decimals=1)).astype(str) + '%'

Item = list(df['Item'].drop_duplicates())
Year = list(df['Year'].drop_duplicates())

#App
# Title & Filters

st.sidebar.markdown('### Data Filters')
Item_choice = st.sidebar.multiselect(
    'Choose Item:', Item, default=Item)

df = df[df['Item'].isin(Item_choice)]

#Main
st.title(f"Items and Sales Last Year")
st.dataframe(df.sort_values('Year',
            ascending=True).reset_index(drop=True))

# To run on Streamlit ----used below code
#  streamlit run c:/Users/mmadh/Documents/Python/New_Proj/BuisnessQuant_task.py [ARGUMENTS]
