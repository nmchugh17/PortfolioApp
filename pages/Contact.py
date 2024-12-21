import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message here")
    captcha = st.checkbox("I am not a robot")
    message = f"""\ 
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        if captcha:
            try:
                send_email(message)
                st.info("Your email was sent successfully.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please confirm that you are not a robot.")
