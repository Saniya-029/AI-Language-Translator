# AI Language Translation & Simplification

## Project overview
A Streamlit application designed to:
- Translate text into a selected language.
- Simplify difficult English into clearer English.
- Use the Google Gemini API to generate results.

## Files
- `app.py` — Streamlit interface and Gemini API request.
- `requirements.txt` — Python dependencies.

## Run locally
1. Install dependencies: `python -m pip install -r requirements.txt`
2. Start the app: `python -m streamlit run app.py`
3. Open the local URL shown in the terminal, usually `http://localhost:8501`.
4. Enter your Gemini API key in the password field. Do not publish the key.

## Important testing note
During testing, the Gemini API returned `403 PERMISSION_DENIED` with the message that the project had been denied access. The interface/source code can be uploaded, but successful AI processing requires valid API access and an available model. Resolve this issue with Google and test again before claiming that the live AI feature works.

## Deployment
On Streamlit Community Cloud, choose this repository, branch `main`, and main file `app.py`. The AI request may fail until the API permission issue is resolved. Never put API keys in GitHub files.
