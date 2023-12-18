import streamlit as st
from gemini import gemini_vision_pro


st.markdown("# Ayu's App with Gemini")
st.markdown("## カロリー推定アプリ(Calorie estimation app)")

uploaded_file = st.file_uploader("食べ物写真をアップロードしてください。(Please upload image of food.)")

if uploaded_file is not None:
    with st.spinner('Wait for it...'):
        age = gemini_vision_pro(
        """
        The calorie content must be predicted from the input photograph.
        Only numbers must always be output, even if they are difficult to predict.
        Outputs such as difficult to predict are not acceptable.
        """, uploaded_file.read())
        st.markdown(f'# {age}カロリー/Calorie')