import streamlit as st
import pandas as pd

# Sets the layout on the streamlit app to wide
st.set_page_config(layout="wide")

# Creates 2 column objects
col1, col2 = st.columns(2)

# Uses context manager to add an image to column 1
with col1:
    st.image("./images/photo.jpg")

# Uses context manager to add information to column 2
with col2:
    st.title("Niall Mc Hugh")
    content = """
    Enjoy working as a team member as well as independently and possess a strong commitment to team environment
    dynamics. Self-motivated and hard working with strong interpersonal skills and positive work ethic. Able to deal
    courteously and professionally with the public. Results-oriented problem solver who works well in high-stress and
    deadline-oriented environments.
    """
    st.info(content)

# Adds more information outside the columns
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

# Creates 3 more column objects with different widths
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Use pandas do import csv file data into a dataframe
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        if not pd.isnull(row['url']):
            st.header(row["title"])
            st.write(row["description"])
            st.image("./images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")
            if not pd.isnull(row['optionalurl']):
                st.write(f"[Web App Link]({row['optionalurl']})")
with col4:
    for index, row in df[10:].iterrows():
        if not pd.isnull(row['url']):
            st.header(row["title"])
            st.write(row["description"])
            st.image("./images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")
            if not pd.isnull(row['optionalurl']):
                st.write(f"[Web App Link]({row['optionalurl']})")
