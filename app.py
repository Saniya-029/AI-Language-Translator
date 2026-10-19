
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Language Assistant",
    page_icon="🌐"
)

st.title("🌐 AI Language Translation & Simplification")
st.write(
    "Translate text into another language or simplify "
    "difficult English using AI."
)

api_key = st.text_input(
    "Enter your Gemini API key",
    type="password"
)

text = st.text_area(
    "Enter your paragraph",
    height=180,
    placeholder="Paste your English paragraph here..."
)

task = st.radio(
    "Choose a task",
    [
        "Translate Text",
        "Simplify English"
    ]
)

language = "Marathi"

if task == "Translate Text":
    language = st.selectbox(
        "Select target language",
        ["Marathi", "Hindi", "Kannada", "Gujarati", "French", "Spanish"]
    )

if st.button("Process Text"):
    if not api_key.strip():
        st.error("Please enter your Gemini API key.")
    elif not text.strip():
        st.warning("Please enter a paragraph first.")
    else:
        try:
            client = genai.Client(api_key=api_key)

            if task == "Translate Text":
                prompt = (
                    f"Translate the following text into {language}. "
                    "Preserve its original meaning and explain nothing extra:\n\n"
                    f"{text}"
                )
            else:
                prompt = (
                    "Rewrite the following text in simple, clear English. "
                    "Keep the original meaning and explain difficult terms "
                    "in easy words where helpful:\n\n"
                    f"{text}"
                )

            with st.spinner("AI is processing your text..."):
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

            if response.text:
                st.subheader("Result")
                st.write(response.text)
            else:
                st.error("No text was returned. Please try again.")

        except Exception as e:
            st.error(
                "Could not process the text. Check your API key, "
                "internet connection, model access, and API quota."
            )
            st.caption(str(e))
