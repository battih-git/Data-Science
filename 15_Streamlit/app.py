import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title('Hello Stream')

##Display a simple text
st.write("This is a simple text")

# Create a data frame
df = pd.DataFrame({
    'first_column':[1,2,3,4,5],
    'second_column':[10,20,30,40,50]
})

# Display the data frame
st.write("Here is the data frame")
st.write(df)

# Chart data
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.line_chart(chart_data)