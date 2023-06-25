import pandas as pd
import streamlit as st
import time
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# upload a file
uploaded_file = st.file_uploader("Choose File", type=["csv"])

if uploaded_file != None:
    dataframe = pd.read_csv(uploaded_file)
    with st.spinner("Writing to DF..."):
        time.sleep(1)
        st.write(dataframe)

# plot functions
def pie_chart():
    st.write("Pie Chart")







def main():
    plot = st.selectbox(
        "Select a Plot",
        [
            "Pie Chart"
        ]
    )

    if plot == "Pie Chart":
        pie_chart()


if __name__ == "__main__":
    main()
