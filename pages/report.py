import streamlit as st
from utils import setup_page, footer

setup_page("Report")

st.write("Here is a report.")

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

footer()