import streamlit as st
import pandas as pd

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df = pd.read_csv(url)

st.title("Company Sales")

chart_type = st.selectbox("Select chart type:", ["Line", "Bar"])

column = st.selectbox("Select column:", df.columns[1:])

st.write("### Chart:")
if chart_type == "Line":
    st.line_chart(df[column])
else:
    st.bar_chart(df[column])