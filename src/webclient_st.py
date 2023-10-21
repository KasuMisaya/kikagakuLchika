import streamlit as st
import requests

st.title('Raspberry Pi Controller')

if st.button('Run Command'):
    response = requests.post('http://everyone-l-chika.onrender.com:10000/run-command')
    if response.ok:
        st.success("Command was run successfully.")
    else:
        st.error("Failed to run the command.")