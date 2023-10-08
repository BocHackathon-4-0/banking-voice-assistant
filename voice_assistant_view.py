import streamlit as st
import recognize_speech
import time
import bank_api_requests
import boc_ads

def start():

        welcome_message = "Hello! How can I help you?"
        recognize_speech.read_text(welcome_message)
        while True: 
            initial_command = recognize_speech.get_voice()
            time.sleep(5)
            new_voice_recorded = recognize_speech.replace_my_with_your(initial_command)  
            voice_recorded = "You told me to " + new_voice_recorded + ". Is everything correct? Shall I proceed with that request?"        
            recognize_speech.read_text(voice_recorded)

            next_step = recognize_speech.get_voice()
            if ("yes" in next_step): 
                if ("balance" in initial_command):       
                    balance = bank_api_requests.get_accounts_available_balance("351092345676")
                    ad_to_read = boc_ads.get_random_ad()
                    text_to_read_final = "Your account balance is " + balance + ". " + ad_to_read
                    recognize_speech.read_text(text_to_read_final)
                    break
                if ("details" in initial_command):
                    details = bank_api_requests.get_filtered_details("351092345676")
                    ad_to_read = boc_ads.get_random_ad()
                    text_to_read_final = "Your account type is " + details[0] + ", your account currency is " + details[1] + " and your account balance is " + details[2] + ". " + ad_to_read
                    recognize_speech.read_text(text_to_read_final)
                    break
                # utility payment
                if ("bill" in initial_command):
                    amount_message = "Please specify the amount."
                    recognize_speech.read_text(amount_message)
                    amount_mentioned = recognize_speech.get_voice()
                    print(amount_mentioned)                    
                    payment_id = bank_api_requests.create_payment(bank_api_requests.sign_utility_payment(amount_mentioned))
                    payment_status = bank_api_requests.get_payment_details(payment_id)
                    ad_to_read = boc_ads.get_random_ad()                    
                    payment_final_message = "You payment was completed successfully. The current status is " + payment_status + " by the organization" + ad_to_read
                    recognize_speech.read_text(payment_final_message)
                    print(payment_id)
                    break
                else:
                    try_again_message = "I did not find what you are looking for. Let's try again!"
                    recognize_speech.read_text(try_again_message)
                    continue
            elif ("stop" in next_step):
                ad_to_read = boc_ads.get_random_ad()
                text_to_read_final = "I hope I have been helpful. " + ad_to_read
                recognize_speech.read_text(text_to_read_final)
                break
            elif ("no" in next_step):
                no_message = "OK then. Let's try again!"
                recognize_speech.read_text(no_message)
                continue
            else:
                continue
 
# Web user interface
style_title = "color: #FF00FF;"
st.markdown(f"<h1 style='text-align: center; color: white;'></i>Hi! I am <span style='{style_title}'>PayVia</span>!</h1>", unsafe_allow_html=True)
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


