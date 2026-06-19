import streamlit as st
from PIL import Image
import datetime

st.title("社会情報プロジェクト実習I")
st.subheader("基本オブジェクト")

st.write("テキストの練習")

# 图片
try:
    image = Image.open("apps/data/画像.png")
    st.image(image, caption="サンプル画像")
except FileNotFoundError:
    st.warning("画像.pngが見つかりません")

# 输入组件
studentID = st.text_input("学籍番号")
years = st.selectbox("学年", ("1年", "2年", "3年", "4年"))
class_choice = st.radio("クラス", ("Aクラス", "Bクラス"))
date = st.date_input("出席日", datetime.date.today())
slider = st.slider("出席回数", 0, 14, 0)
checked = st.checkbox("後期も受講")

btn = st.button("出席")
if btn:
    st.write(f"{date}| {years} |{class_choice}| {studentID}| 出席{slider}回目")
    if checked:
        st.write("後期も受講")
    print(f"出席:{studentID}")
