import streamlit as st

#Sidebar
st.sidebar.markdown("Clicked Page5")

#Page
st.title("page5")
with st.container():
    st.write("이것은 컨테이너 내부입니다.")
    with st.expander("더 보기"):
        st.write("이곳에 추가 정보를 입력할 수 있습니다.")
    st.write("이것은 컨테이너 내부입니다.")
    with st.expander("더 보기"):
        st.write("이곳에 추가 정보를 입력할 수 있습니다.")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Please enter your name")
        rating = st.slider("Please rate this app", 0, 10, 5)
    with col2:
        dob = st.date_input("Please enter your date of birth")
        recommend = st.radio("Would you recommend this app to others?", ("Yes", "No"))

with col1:
        name = st.text_input("Please enter your name")
        rating = st.slider("Please rate this app", 0, 10, 5)
with col2:
        dob = st.date_input("Please enter your date of birth")
        recommend = st.radio("Would you recommend this app to others?", ("Yes", "No"))
col1, col2, col3 = st.columns([3, 3, 3])

with col1:
  st.header('Col1')
  st.image('https://static.streamlit.io/examples/cat.jpg',width=200)

with col2:
  st.header('Col2')
  st.image('https://static.streamlit.io/examples/dog.jpg',width=200)

with col3:
  st.header('Col3')
  st.image('https://static.streamlit.io/examples/owl.jpg',width=200)

