import streamlit as st

st.set_page_config(page_title="VV", page_icon=":wave:", layout="wide")

st.sidebar.image("https://raw.githubusercontent.com/VV-Apps/Webpage_Repo/main/The Dark King.png", use_column_width=True)
st.sidebar.title("VV_Webpage")

tabs1 = st.sidebar.button("About Me")
tabs2 = st.sidebar.button("Resume")
tabs3 = st.sidebar.button("Contact Me")

with st.container():
    if tabs1:
        st.empty().title("About Me")
        st.empty().subheader("Vision")
        st.empty().write("Founded by a group of zealous youths with a passion for music, Project Gift of Song aims to bridge the gap between music and terminal illnesses. We wish to bring joy and comfort to all stages of life through the spread of music.")
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

        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Latest Updates")
            st.write("""
                On my YouTube channel I am creating tutorials for people who:
                - are looking for a way to leverage the power of Python in their day-to-day work.
                - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
                - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
                - are working with Excel and found themselves thinking - "there has to be a better way."

                If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
                """)
            st.write("")
        with right_column:
            st.write("Yes")

    st.write("[My YouTube Channel 👈](https://youtube.com)")
