import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st

#从文件夹里直接导入py file的function
from util.pages2.home import home_page
from util.pages2.experience import experience_page
from util.pages2.education import education_page
from util.pages2.resume import resume_page
from util.pages2.contact import contact_page

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.set_page_config(page_title="personalsite", layout="wide")

        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.radio(
            "Navigation", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()

app = MultiApp()

app.add_app("Home Page", home_page)
app.add_app("Education Page", education_page)
app.add_app("Experience Page", experience_page)
app.add_app("Resume Page", resume_page)
app.add_app("Contact Page", contact_page)

app.run()

