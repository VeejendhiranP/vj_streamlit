import streamlit as st
import pandas as pd

st.header("HI from VJ")
st.text("Good Morning")


# Create sample data
data = {
    "Investor": ["Alice", "Bob", "Charlie", "David"],
    "Investment_Amount": [10000, 25000, 15000, 50000],
    "Rate_of_Return": [0.08, 0.10, 0.07, 0.12],
    "Years": [5, 3, 4, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

st.dataframe(df)
