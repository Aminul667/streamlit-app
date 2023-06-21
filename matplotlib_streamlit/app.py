import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


@st.cache_data
def load_data():
    df = pd.read_csv("./data/ted.csv")
    return df


df = load_data()


def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage"
        ]
    )

    if page == "Homepage":
        st.header("Data Application")
        st.balloons()
        st.write(df)


if __name__ == "__main__":
    main()
