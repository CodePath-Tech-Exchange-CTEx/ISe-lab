import streamlit as st
from utils import setup_page, footer

setup_page("About")

st.write("""
Fake Company LLC Inc. is a fake company created in 2024.
It produces nothing and earns $0 revenue.
""")

st.image("./assets/fake_company.png")

footer()