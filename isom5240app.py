

import streamlit as st

# Set the title of the app
st.title('My First Streamlit App')

# Add a header
st.header('User Input Example')

# Add a text input widget
user_input = st.text_input("Enter some text", "Type here...")

# Add a button
if st.button("Display Text"):
    # Display the user input in a success message
    st.success(f'You entered: {user_input}')
    st.balloons() # Add some fun!

# You can also use st.write() to display text and data
st.write("---")
st.write("This section uses `st.write()`")

