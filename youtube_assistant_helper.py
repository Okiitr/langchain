from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# This file contains helper functions for the YouTube assistant app. It includes functions to create a vector database from a YouTube video transcript and to get a response from a query using the vector database and an LLM.
def create_db_from_youtube_video_url(video_url: str, openai_api_key: str):
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(transcript)

    embeddings = OpenAIEmbeddings(api_key=openai_api_key)

    db = FAISS.from_documents(docs, embeddings)
    return db

# This function takes a vector database, a query, and an OpenAI API key, and returns a response from the LLM based on the query and the documents in the vector database. It uses a prompt template to guide the LLM's response.
def get_response_from_query(db, query, openai_api_key, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(
        temperature=0.3,
        api_key=openai_api_key
    )

    prompt = PromptTemplate.from_template("""
    You are a helpful assistant that can answer questions about a YouTube video 
    based only on its transcript.

    Answer the following question:
    {question}

    Using this transcript:
    {docs}

    Rules:
    - Only use transcript data
    - If answer is not found, say "I don't know"
    - Give detailed answer
    """)

    chain = prompt | llm

    response = chain.invoke({
        "question": query,
        "docs": docs_page_content
    })

    return response.strip(), docs