import re
import uuid

import streamlit as st


def show_st_h1(text, w_divider=False) -> None:
    h1_str = f"<h1 class='st-key-sans-serif-header'>{text}</h1>"
    hr_str = "<hr class='st-key-header-divider'>"

    if w_divider:
        st.html(h1_str + hr_str)
    else:
        st.html(h1_str)


def show_st_h2(text, w_divider=False) -> None:
    h1_str = f"<h2 class='st-key-serif-header'>{text}</h2>"
    hr_str = "<hr class='st-key-header-divider'>"

    if w_divider:
        st.html(h1_str + hr_str)
    else:
        st.html(h1_str)


def show_st_button(link_text, link_url, hover_color="#e78ac3", st_col=None):

    button_uuid = str(uuid.uuid4()).replace("-", "")
    button_id = re.sub("\d+", "", button_uuid)

    button_css = f"""
        <style>
            #{button_id} {{
                background-color: rgb(255, 255, 255);
                color: rgb(38, 39, 48);
                padding: 0.25em 0.38em;
                position: relative;
                text-decoration: none;
                border-radius: 4px;
                border-width: 1px;
                border-style: solid;
                border-color: rgb(230, 234, 241);
                border-image: initial;

            }}
            #{button_id}:hover {{
                border-color: {hover_color};
                color: {hover_color};
            }}
            #{button_id}:active {{
                box-shadow: none;
                background-color: {hover_color};
                color: white;
                }}
        </style> """

    html_str = f'<a href="{link_url}" target="_blank" id="{button_id}";>{link_text}</a><br></br>'

    if st_col is None:
        st.html(button_css + html_str)
    else:
        st_col.html(button_css + html_str)
