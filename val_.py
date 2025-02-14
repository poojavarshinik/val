try:
    import streamlit as st
    import random
except ModuleNotFoundError:
    print("Error: The 'streamlit' module is not installed. Please install it using 'pip install streamlit' and try again.")
    raise SystemExit

# Set the page title and emoji
st.set_page_config(page_title="Be My Valentine? 💘", page_icon="💖")

# Background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFE4E1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='text-align: center; color: #FF1493;'>Will You Be My Valentine? 💕</h1>", unsafe_allow_html=True)

# Fun message options
messages = [
    "Roses are red, violets are blue, my Valentine's wish is to be with you! 🌹",
    "You're the peanut butter to my jelly, the cheese to my pizza! Be mine? 🧡",
    "Life's better with you! Will you be my Valentine? 💖",
    "You light up my life like fireworks in the sky! 🎆 Be my Valentine?",
    "Without you, my world is like a broken pencil… pointless! Be mine? 😉"
]

# Display a random message
st.write(f"### {random.choice(messages)}")

# Buttons for response
col1, col2 = st.columns(2)
with col1:
    if st.button("💘 Yes, of course! 💘"):
        st.balloons()
        st.success("Yay! You just made my day! 💖🥰")

with col2:
    if st.button("💔 yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss! 💔"):
        st.error("Thanks my kabiiiii. 😭🍫")
