import os
from typing import Dict

import streamlit as st

from constants.file import TMP_DIR, TMP_TEST_JSON
from functions.gui import show_st_h1, show_st_h2
from functions.io import load_json
from pipelines.prep_data_comps_map import prep_data


def st_page_comps_map():

    show_st_h1("Sales Comparables")
    show_st_h2("Nearby Flipped Properties", w_divider=True)

    st.markdown(
        f"""
        The following map shows flipped properties from the same ZIP
        code as the subject property located at:

        *{st.session_state.subj_prop_address}*

        Use the map settings below to select nearby comps.
        """
    )

    st.markdown("#### Distance")
    distance_in_mi = st.slider("**Miles From Subject Property**", 0.0, 2.0, 0.5)

    prep_data()
    prepped_data: Dict = load_json(os.path.join(TMP_DIR, TMP_TEST_JSON))
    st.write(prepped_data)


st_page_comps_map()
