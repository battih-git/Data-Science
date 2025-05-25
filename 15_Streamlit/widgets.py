import streamlit as st

st.title("Streamlit Text Input")
name = st.text_input('Enter your name: ')

age = st.slider('Select your age: ', 0,100,25)

st.write(f"Your age is {age}")

options = ['Python', 'Java', 'C++']
st.selectbox('Choose your preferred language', options)

uploaded_file = st.file_uploader('Choose a CSV file: ', type='csv')


if name:
    st.write(f"Hello {name}")

