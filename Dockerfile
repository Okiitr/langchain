FROM python:3.9.2
WORKDIR llm-apps
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8501
# CMD ["streamlit", "run", "main-baby-name-generator.py", "--server.port=8501", "--server.address=0.0.0.0"] #for baby name generator app
# CMD ["streamlit", "run", "main-pet-name.py", "--server.port=8501", "--server.address=0.0.0.0"] # for pet name generator app
CMD ["streamlit", "run", "main-youtube-assistant.py", "--server.port=8501", "--server.address=0.0.0.0"] # for youtube assistant app