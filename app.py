import streamlit as st
from gemini import gemini_vision_pro


st.markdown("# Ayu's App with Gemini")
st.markdown("## 顔写真年齢推定(Facial photo age estimation)")

uploaded_file = st.file_uploader("顔写真をアップロードしてください。(Please upload image of face.)")

if uploaded_file is not None:
    with st.spinner('Wait for it...'):
        age = gemini_vision_pro(
        """
        入力された写真から年齢を予測しなければならない。
        予測困難な場合でも、必ず数字のみを出力しなければならない。
        予測困難などの出力は受け付けられません。
        プログラムで使用するため、整数と言わなければならない。
        """, uploaded_file.read())
        st.markdown(f'# {age}歳/years old')