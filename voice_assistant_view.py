import streamlit as st
import recognize_speech
import time
import bank_api_requests
import boc_ads

def start():
    initial_command = recognize_speech.get_voice()
    time.sleep(5)
    new_voice_recorded = recognize_speech.replace_my_with_your(initial_command)  
    voice_recorded = "You told me to " + new_voice_recorded + ". Is everything correct? Shall I proceed with that request?"        
    recognize_speech.read_text(voice_recorded)

    next = recognize_speech.get_voice()
    if ("yes" in next):        
        balance = bank_api_requests.get_accounts_available_balance("351092345676")
        ad_to_read = boc_ads.get_random_ad()
        text_to_read_final = "Your account balance is " + str(balance) + ". " + ad_to_read
        recognize_speech.read_text(text_to_read_final)
 
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
btn = st.button("Let's Start! 	:studio_microphone:", on_click=start)


