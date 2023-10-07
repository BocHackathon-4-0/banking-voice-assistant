import streamlit as st

# Web user interface
style_title = "color: #FF00FF;"
st.markdown(f"<h1 style='text-align: center; color: white;'></i>Hi! I am <span style='{style_title}'>Payvia</span>!</h1>", unsafe_allow_html=True)
style_subtitle = "color: cyan;"
st.markdown(f"<h2 style='text-align: center; color: white;'>Your <span style='{style_subtitle}'>Favourite</span> Personal Banking Assistant</h2>", unsafe_allow_html=True)

# CSS styling for button
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #34c9eb;
    margin-Left: 35%;
    margin-top: 35%;
    height: 20%;
    width: 30%;
}
</style>""", unsafe_allow_html=True)

# Button to start the assistant
btn = st.button("Let's Start!")