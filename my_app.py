import streamlit as st
st.write("Hello World: Getting Bore, Hello Brother!!")
st.title("Display Tittle use st.title()")
st.write("To write text use st.write()")
st.header("I am header to write header use st.header()")
st.subheader("I am subheader to write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text()")

# To create hyperlink

st.markdown("[Streamlit](https://share.streamlit.io/)")
st.markdown("[Github](https://github.com/dashboard)")
st.success("Succes")
st.info("Information")
st.warning("This is warning")
st.error("This is an Error")

from PIL import Image
img = Image.open("smj.jpg")
st.image(img, width=500, caption="Satyamev jayte")

video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=srNoYnGhXAg")

audio_file = open("song.mp3","rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")


st.header("Button widgets")

if st.button("Play"):
    st.text("Hellow World")

if st.button("Play Video"):
    st.text("Enjoy Video")
    st.video("https://www.youtube.com/watch?v=srNoYnGhXAg")

if st.checkbox("Checkbox"):
    st.text("Checkbox selected")