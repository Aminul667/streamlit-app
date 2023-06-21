import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def bar_plot():
    fig = plt.figure(figsize=(12, 5))
    plt.xticks(rotation=80)
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    xaxis = "event"
    yaxis = "views"
    plt.ticklabel_format(style="plain")
    plt.bar(bar_data[xaxis], bar_data[yaxis])
    plt.xlabel("Event")
    plt.ylabel("Views")
    plt.title("Event and View plot")
    st.pyplot(fig)


@st.cache_data
def load_data():
    df = pd.read_csv("./data/ted.csv")
    return df


df = load_data()


def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage",
            "Bar Plot"
        ]
    )

    if page == "Homepage":
        # st.header("Data Application")
        """
        # Data Application
        Dataset has been loaded
        """
        st.balloons()
        st.write(df)
    elif page == "Bar Plot":
        bar_plot()


if __name__ == "__main__":
    main()
