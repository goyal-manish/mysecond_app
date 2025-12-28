import streamlit as st
import random

st.set_page_config(page_title="Kids Fun App", page_icon="🎈")

st.title("🎈 Welcome to Kids Fun App 🎈")
st.subheader("Learn • Play • Enjoy 😄")

menu = st.sidebar.selectbox(
    "Choose a Fun Activity 🎯",
    ["🏠 Home", "🐶 Animal Sounds", "🎲 Guess the Number", "🎨 Color Fun"]
)

# ---------------- HOME ----------------
if menu == "🏠 Home":
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3468/3468377.png",
        width=200
    )
    st.markdown("### 🌟 Hello Kids!")
    st.write("Press the buttons and have fun 🎉")
    st.balloons()

# ---------------- ANIMAL SOUNDS ----------------
elif menu == "🐶 Animal Sounds":
    st.header("🐶 Animal Sounds")

    animal = st.radio(
        "Choose an Animal 🐾",
        ["Dog 🐶", "Cat 🐱", "Cow 🐮", "Lion 🦁"]
    )

    if st.button("🔊 Play Sound"):
        if "Dog" in animal:
            st.success("🐶 Dog says: Woof Woof!")
        elif "Cat" in animal:
            st.success("🐱 Cat says: Meow Meow!")
        elif "Cow" in animal:
            st.success("🐮 Cow says: Moo Moo!")
        elif "Lion" in animal:
            st.success("🦁 Lion says: Roarrr!")

# ---------------- GUESS THE NUMBER ----------------
elif menu == "🎲 Guess the Number":
    st.header("🎲 Guess the Number Game")

    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 5)

    guess = st.number_input(
        "Guess a number between 1 and 5 🔢",
        min_value=1,
        max_value=5
    )

    if st.button("✅ Check"):
        if guess == st.session_state.number:
            st.success("🎉 Correct! You are awesome!")
            st.balloons()
            st.session_state.number = random.randint(1, 5)
        else:
            st.error("❌ Try again!")

# ---------------- COLOR FUN ----------------
elif menu == "🎨 Color Fun":
    st.header("🎨 Choose Your Favorite Color")

    color = st.color_picker("Pick a Color 🌈")

    st.markdown(
        f"""
        <div style='background-color:{color};
        padding:50px;
        border-radius:20px;
        text-align:center;
        font-size:30px;'>
        😍 Beautiful Color 😍
        </div>
        """,
        unsafe_allow_html=True
    )

    st.snow()

st.markdown("---")
st.markdown("### 💖 Made with Love for Kids")
