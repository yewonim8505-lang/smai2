import streamlit as st



#Page
st.title("Page4")
image = Image.open("dog.png")
st.image(image, caption="예제 이미지",  use_container_width=True)