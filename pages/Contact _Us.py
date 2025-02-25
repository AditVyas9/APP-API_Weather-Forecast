import streamlit as st
from send_email import send_email

st.header("Contact Me!")

with st.form(key="email_form"):
    user_email = st.text_input("Your E-mail address:")
    raw_message = st.text_area("Your Message:")
    message = f"""\
Subject: New E-mail from {user_email}  

From: {user_email}
{raw_message}
"""
    submit = st.form_submit_button("Submit")
    # checking if the value of button is True or False
    if submit:
        send_email(message)
        st.info("Your E-mail was sent successfully!")
