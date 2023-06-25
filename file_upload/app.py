import pandas as pd
import streamlit as st
import time

uploaded_file = st.file_uploader("Choose File", type=["csv"])

if uploaded_file != None:
    dataframe = pd.read_csv(uploaded_file)
    with st.spinner("Writing to DF..."):
        time.sleep(1)
        st.write(dataframe)
