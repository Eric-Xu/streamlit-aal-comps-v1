from streamlit.navigation.page import StreamlitPage

from functions.st_app import initialize_session_state, load_css, setup_page_navigation


class MultiApp:
    def __init__(self):
        load_css()

        initialize_session_state()

    def run(self):
        pg: StreamlitPage = setup_page_navigation()
        pg.run()


app = MultiApp()
app.run()
