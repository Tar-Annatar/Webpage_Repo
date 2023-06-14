import requests
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
st.set_page_config(page_title="Vignesh", page_icon=":wave:", layout="wide")

lottie_url = "https://assets4.lottiefiles.com/packages/lf20_au98facn.json"
    
st.sidebar.image("https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/The Dark King.png", use_column_width=True)
st.sidebar.title("Vignesh_Webpage")

tabs1 = st.sidebar.button("About Me")
tabs2 = st.sidebar.button("Resume")
tabs3 = st.sidebar.button("Contact Me")

with st.container():
    if tabs1:
        st.empty().title("About Me")
        st.empty().subheader("Vision")
        st.empty().write("Man with a plan")
        about_me_button = st.empty().button("Back to Main Page")
        if about_me_button:
            st.experimental_set_query_params()
    else:
        st.empty().empty()
with st.container():
    if tabs2:
        st.empty().title("Resume")
        st.empty().subheader("Education")
        st.empty().write("Educational details go here.")
        resume_button = st.empty().button("Back to Main Page")
        if resume_button:
            st.experimental_set_query_params()
    else:
        st.empty().empty()
with st.container():
    if tabs3:
        st.empty().title("Contact Me")
        contact_button = st.empty().button("Back to Main Page")
        if contact_button:
            st.experimental_set_query_params()
    else:
        st.empty().empty()


with st.container():
    if not any([tabs1, tabs2, tabs3]):
        st.title(":grinning: Vignesh")
        st.subheader("A student in Singapore")
        st.write("[Find out more about me 👈](https://tarannator.blogspot.com/)")
        
    with st.container():
            st.write("""
                    On my YouTube channel I am creating tutorials for people who:
                    - are looking for a way to leverage the power of Python in their day-to-day work.
                    - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
                    - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
                    - are working with Excel and found themselves thinking - "there has to be a better way."

                    If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.

                    """)

            left_column, right_column = st.columns(2)
            with left_column:
                st.header("Latest Updates")
                st.write("""
                IN THE OVEN
                """)
            with right_column:
                components.html('<lottie-player src="{}" background="transparent" speed="1" style="width: 300px; height: 300px;"></lottie-player>'.format(lottie_url), height=300)          
            st.write("[My YouTube Channel 👈](https://youtube.com)")
