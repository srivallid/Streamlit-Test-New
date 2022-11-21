import streamlit as st
from password_check import check_password

if check_password():
    def run():
        st.set_page_config(
            page_title="Home",
            page_icon="🏠",
        )

        st.write("# Welcome Home! 👋")
        st.write("Please click on the page you see on the side bar")

    run()
