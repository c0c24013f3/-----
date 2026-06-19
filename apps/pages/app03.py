import streamlit as st
from PIL import Image

st.title("社会情報プロジェクト実習I")
st.subheader("画面設計")

col1, col2 = st.columns(2)

with col1:
    st.subheader("入力画面")
    studentID = st.text_input("学籍番号")
    years = st.selectbox("学年", ("1年", "2年", "3年", "4年"))

with col2:
    st.subheader("画像表示")
    try:
        image = Image.open("apps/data/画像.png")
        st.image(image)
    except FileNotFoundError:
        st.warning("画像.pngを配置してください")
