import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV data
file_path = "important5years.csv"
df = pd.read_csv(file_path)
df.set_index("Shop Code", inplace=True)

# Streamlit app
st.title("Interactive Plotting with Streamlit")
st.set_option('deprecation.showPyplotGlobalUse', False)
# Dropdown for selecting an index
selected_index = st.selectbox("Select an index:", df.index)

# Submit button
if st.button("Submit"):
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df.columns, df.loc[selected_index], marker='o')
    plt.title(f"Sales Data for {selected_index}")
    plt.xlabel("Months")
    plt.ylabel("Sales Amount")
    plt.xticks(rotation=90, ha="right")

    # Show plot
    st.pyplot()
    
