import streamlit as st
import pandas as pd

@st.cache
def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

# Example: Loading a CSV file into a DataFrame
# df = load_data('your_csv_file.csv')



# Title of your app
st.title('Murder Mystery Game')

# Creating tabs for Schema and Data Exploration
tab1, tab2 = st.tabs(["Schema", "Data Exploration"])

with tab1:
    st.header("Database Schema")
    st.write("Your database schema goes here. You can use Markdown or diagrams.")

with tab2:
    st.header("Explore the Data")
    user_code = st.text_area("Write your Pandas code here to explore the data", height=300)
    
    # Execute button
    if st.button('Execute'):
        # Safe execution logic here
        pass
