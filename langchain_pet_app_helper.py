from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate


def generate_pet_name(animal_type, pet_color, openai_api_key):
    llm = OpenAI(
        temperature=0.7,
        api_key=openai_api_key
    )

    prompt = PromptTemplate.from_template(
        "I have a {animal_type} pet and it is {pet_color} in color. Suggest me five cool names."
    )

    chain = prompt | llm

    response = chain.invoke({
        "animal_type": animal_type,
        "pet_color": pet_color
    })

    return {"pet_name": response}