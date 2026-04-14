from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


def main():
    # Initialize LLM
    llm = OpenAI(temperature=0.7)

    # Create prompt template
    # prompt = PromptTemplate(
    #     input_variables=["question"],
    #     template="What year did the {question} happen?",
    # )

    # Input
    question = "Apollo 11 moon landing"

    # Format prompt
    # formatted_prompt = prompt.format(question=question)

    # Call LLM (correct way)
    response = llm.invoke("give be best 5 name on li for a girl child")

    print(response)


if __name__ == "__main__":
    main()