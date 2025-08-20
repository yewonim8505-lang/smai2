import streamlit as st

page_main=st.Page("main.py",title="Main Page")
page_1=st.Page("p1.py",title="Main Page1")
page_2=st.Page("p2.py",title="Main Page2")
page_3=st.Page("p3.py",title="Main Page3")

page=st.navigation([page_main,page_1,page_2,page_3])

page