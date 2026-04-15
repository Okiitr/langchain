from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate


def generate_baby_name(zodiac_sign, gender, starting_letter, openai_api_key):
    
    # Temperature is set to 0.8 to encourage more creative name suggestions
    llm = OpenAI(
        temperature=0.8,
        api_key=openai_api_key
    )

    if starting_letter:
        template = """
        Suggest 5 unique and meaningful {gender} baby names based on the zodiac sign "{zodiac_sign}".
        Names must start with the letter "{starting_letter}".

        For each name, also provide a short meaning.
        Format:
        1. Name - Meaning
        """
    else:
        template = """
        Suggest 5 unique and meaningful {gender} baby names based on the zodiac sign "{zodiac_sign}".

        For each name, also provide a short meaning.
        Format:
        1. Name - Meaning
        """
    # Create a prompt template with the defined structure
    prompt = PromptTemplate.from_template(template)

    chain = prompt | llm

    # Invoke the chain with the provided inputs
    response = chain.invoke({
        "zodiac_sign": zodiac_sign,
        "gender": gender,
        "starting_letter": starting_letter if starting_letter else ""
    })

    return response