import streamlit as st

from functions.gui import show_st_h1, show_st_h2


def st_page_compare_prices():

    show_st_h1("Market Analysis")
    show_st_h2("Listed Vs Sold Price", w_divider=True)

    st.markdown(
        """
        ### Hello

        To the left, is a dropdown main menu for navigating to 
        each page in the *AAL* database:

        - **Home Page:** We are here!
        """
    )


st_page_compare_prices()
