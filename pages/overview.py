import streamlit as st
from utils import setup_page, footer

setup_page("Overview")

st.write("""
This site has several pages.

All repeated code has been removed using utils.py
""")

footer()