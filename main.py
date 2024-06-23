import streamlit as st

# Sets the layout on the streamlit app to wide
st.set_page_config(layout="wide")

# Creates 2 columns objects
col1, col2 = st.columns(2)

# Uses context manager to add an image to column 1
with col1:
    st.image("images/photo.jpg")

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

# Adds more information outside of the columns
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)
