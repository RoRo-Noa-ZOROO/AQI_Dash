import streamlit as st

st.title("Power BI Embedded Report")
st.markdown(
    """
    <iframe title="first try" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiZGJkYTk1NGQtNWUzMi00MmJhLThmZDMtNTAzOTNjMmRmZWM4IiwidCI6IjkzZTljMTgyLTdhOWMtNGI4YS04YzY1LTM3OTMyNDZlYzgzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True,
)