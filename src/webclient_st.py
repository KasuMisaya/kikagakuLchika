import streamlit as st
import requests

st.title('Raspberry Pi Controller')

if st.button('Run Command'):
    response = requests.post('http://192.168.2.151:8002/run-command')
    if response.ok:
        st.success("Command was run successfully.")
    else:
        st.error("Failed to run the command.")