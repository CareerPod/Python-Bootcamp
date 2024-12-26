import requests
import streamlit as st

# App title
st.title("Random Joke Generator")

# Display instructions
st.write("Click the button below to get a random joke!")

# Button to fetch a joke
if st.button("Get a Joke"):
    # Fetching joke from the API
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        print(response)
        joke = response.json()
        print(joke)
        
        # Displaying the joke
        st.write(f"### {joke['setup']}")
        st.write(f"**{joke['punchline']}**")
    except:
        st.write("Oops! Something went wrong. Please try again.")
