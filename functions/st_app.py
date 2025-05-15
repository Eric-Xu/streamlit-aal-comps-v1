import os
from pathlib import Path

import streamlit as st
from streamlit.navigation.page import StreamlitPage

from constants.file import (
    COMPS_MAP_PAGE_FILE,
    CSS_DIR,
    CSS_FILE,
    MARKET_DOM_PAGE_FILE,
    MARKET_PRICES_PAGE_FILE,
    PAGE_DIR,
)


def initialize_session_state() -> None:
    st.session_state["subj_prop_address"] = "123 Main St"


def load_css() -> None:
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file_path = os.path.join(current_dir, CSS_DIR, CSS_FILE)

    with open(css_file_path) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


def setup_page_navigation() -> StreamlitPage:
    comps_map_page = st.Page(
        os.path.join(PAGE_DIR, COMPS_MAP_PAGE_FILE),
        title="Comps Map",
        icon=":material/map:",
        default=True,
    )
    page2 = st.Page(
        os.path.join(PAGE_DIR, MARKET_PRICES_PAGE_FILE),
        title="Listed Vs Sold Price",
        icon=":material/stacked_line_chart:",
    )
    page3 = st.Page(
        os.path.join(PAGE_DIR, MARKET_DOM_PAGE_FILE),
        title="Days On Market",
        icon=":material/scatter_plot:",
    )

    pages = {
        "Sales Comparables": [comps_map_page],
        "Market Analysis": [page2, page3],
    }
    pg: StreamlitPage = st.navigation(pages)

    return pg
