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


def horizontal_bar_plot():
    fig = plt.figure(figsize=(12, 5))
    plt.xticks(rotation=80)
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    xaxis = "event"
    yaxis = "views"
    plt.ticklabel_format(style="plain")
    plt.barh(bar_data[xaxis], bar_data[yaxis])
    plt.xlabel("Event")
    plt.ylabel("Views")
    plt.title("Event and View plot")
    st.pyplot(fig)


def scatter_plot():
    fig = plt.figure(figsize=(10, 8))
    plt.scatter(
        x=df["comments"],
        y=df["views"],
        marker="*",
        s=df["languages"],
        c=df["languages"],
        alpha=0.5
    )
    st.pyplot(fig)


def histogram():
    fig = plt.figure(figsize=(12, 5))
    plt.hist(df["languages"], color="y", bins=50)
    st.pyplot(fig)


def pie_chart():
    days_data = (
        df.groupby("published_day")["views"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig = plt.figure(figsize=(10, 8))
    plt.pie(
        days_data["views"],
        labels=days_data["published_day"],
        autopct="%1.1f%%"
    )
    st.pyplot(fig)


def two_subplots():
    fig = plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    xaxis = "event"
    yaxis = "views"
    plt.ticklabel_format(style="plain")
    plt.barh(bar_data[xaxis], bar_data[yaxis])

    plt.subplot(1, 2, 2)
    plt.scatter(df["views"], df["comments"], c=df["languages"], marker="*")

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
            "Bar Plot",
            "Horizontal Bar Plot",
            "Scatter Plot",
            "Histogram",
            "Pie Chart",
            "Two Subplots"
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
    elif page == "Horizontal Bar Plot":
        horizontal_bar_plot()
    elif page == "Scatter Plot":
        scatter_plot()
    elif page == "Histogram":
        st.header("Language Histogram")
        histogram()
    elif page == "Pie Chart":
        st.header("Views and Days pie chart")
        pie_chart()
    elif page == "Two Subplots":
        st.header("Subplots")
        two_subplots()


if __name__ == "__main__":
    main()
