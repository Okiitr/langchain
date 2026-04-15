import streamlit as st
import baby_name_generator_helper as helper


#Using Streamlit's set_page_config to set the title and icon of the web app 

st.set_page_config(page_title="👶 Baby Name Generator", page_icon="👶")


st.title("👶 Baby Name Generator (Zodiac Based)")

# Sidebar inputs
with st.sidebar:
    st.header("🔧 Input Details")

    zodiac_sign = st.selectbox(
        "Select Zodiac Sign",
        (
            "Aries", "Taurus", "Gemini", "Cancer",
            "Leo", "Virgo", "Libra", "Scorpio",
            "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        )
    )

    gender = st.selectbox(
        "Select Gender",
        ("Boy", "Girl", "Unisex")
    )

    starting_letter = st.text_input(
        "Optional: Starting Letter",
        max_chars=1
    )

    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password"
    )

    generate_btn = st.button("✨ Generate Names")


# Main logic
if generate_btn:
    if not openai_api_key:
        st.warning("⚠️ Please enter your OpenAI API key")
        st.stop()

    with st.spinner("Generating beautiful names... 👶"):
        result = helper.generate_baby_name(
            zodiac_sign,
            gender,
            starting_letter,
            openai_api_key
        )

    st.success("✅ Here are some lovely names:")
    st.write(result)


# Footer
st.markdown("---")
st.caption("Made with ❤️ using LangChain + OpenAI")