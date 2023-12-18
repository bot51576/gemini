import google.generativeai as genai
import streamlit as st 


genai.configure(api_key=f'{st.secrets["api_key"]}')

def gemini_vision_pro(prompt, image):
    # Set up the model
    generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    }
    ]

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    image_parts = [
    {
        "mime_type": "image/jpeg",
        "data": image
    },
    ]

    prompt_parts = [
    prompt,
    image_parts[0],
    ]

    response = model.generate_content(prompt_parts)
    return response.text    