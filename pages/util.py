import streamlit as st

COMPANY_NAME = "Fake Company LLC Inc."
YEAR = 2024
ADDRESS = "1600 Amphitheatre Parkway Mountain View, CA 94043"


def init_session():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False


def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False


def setup_page(title):
    init_session()
    st.set_page_config(page_title=title)
    st.title(title)
    sidebar(title)


def sidebar(title):
    st.sidebar.header(title)

    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", on_click=login)

    st.sidebar.write(
        f"This site is copyright {COMPANY_NAME}, {YEAR}"
    )


def footer():
    with st.expander("Company Info"):
        st.write(f"{COMPANY_NAME} is located at {ADDRESS}")

    with st.expander("Links"):
        st.markdown("""
        [Google](https://google.com)

        [Gemini](https://gemini.google.com)

        [Streamlit Docs](https://docs.streamlit.io/)
        """)