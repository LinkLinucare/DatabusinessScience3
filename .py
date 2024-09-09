import streamlit as st

# Title of the app
st.title('Hello, Streamlit!')

# Adding a header
st.header('Welcome to my first web app')

# Adding a simple text input
name = st.text_input('Enter your name:')

# Display the input when user submits
if name:
    st.write(f'Hello, {name}!')

# Adding a slider widget
age = st.slider('Select your age:', 1, 100, 25)
st.write(f'Your age is: {age}')

# Adding a button to display a message
if st.button('Click me'):
    st.write("You clicked the button!")

# Add a selectbox widget
favorite_language = st.selectbox('What is your favorite programming language?', 
                                 ['Python', 'JavaScript', 'C++', 'Java'])
st.write(f'You selected: {favorite_language}')
