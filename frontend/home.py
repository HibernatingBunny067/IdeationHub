import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="IdeationHub",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 IdeationHub")

st.markdown("""
Welcome to **IdeationHub**.

This tool helps you:

- Generate structured project ideas
- Refine ideas through guided AI discussion
- Align projects with your career goals

Use the sidebar to get started.
""")

st.divider()

st.subheader("How It Works")

st.markdown("""
1. Go to **Generate Ideas** in the sidebar  
2. Enter your skill level, domain, and career goal  
3. Select an idea  
4. Refine it in conversation mode  
""")

st.sidebar.success('Select a page above.')