import streamlit as st

from functions.gui import show_st_h1, show_st_h2


def st_page_dom() -> None:
    show_st_h1("Market Analysis")
    show_st_h2("Days-On-Market", w_divider=True)


st_page_dom()
