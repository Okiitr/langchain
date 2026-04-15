import streamlit as st
import youtube_assistant_helper as lch
import textwrap

st.set_page_config(page_title="YouTube Assistant", page_icon="🎥")

st.title("🎥 YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.text_area(
            label="YouTube Video URL",
            max_chars=200
        )

        query = st.text_area(
            label="Ask a question about the video",
            max_chars=200
        )

        openai_api_key = st.text_input(
            label="OpenAI API Key",
            type="password"
        )

        submit_button = st.form_submit_button(label='Submit')

# -------- MAIN --------
if submit_button:
    if not youtube_url or not query:
        st.warning("⚠️ Please enter both URL and question")
        st.stop()

    if not openai_api_key:
        st.warning("⚠️ Please enter OpenAI API key")
        st.stop()

    with st.spinner("Processing video... ⏳"):
        db = lch.create_db_from_youtube_video_url(
            youtube_url,
            openai_api_key
        )

        response, docs = lch.get_response_from_query(
            db,
            query,
            openai_api_key
        )

    st.subheader("📌 Answer:")
    st.write(textwrap.fill(response, width=85))