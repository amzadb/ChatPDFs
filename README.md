# ChatPDFs

## Introduction
----------------
The ChatPDFs App is a Python application that allows you to chat with PDF document(s). You can ask questions about the PDF(s) using natural language, and the application will provide the responses based on the content of the documents. This app utilizing a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the uploaded PDF(s).

## How It Works
----------------

Following are the steps involeved in ChatPDFs application, to provide responses to your questions:

1. PDF Loading: The app reads the uploaded PDF document(s) and extracts their text content.

2. Text Chunking: The extracted text is divided into chunks that can be processed effectively.

3. Language Model: The application using a language model to generate vector representations (embeddings) of the text chunks.

4. Semantic Search: When you ask a question, the app compares it with the text chunks and identifies the most similar matching ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDF(s).

## Dependencies and Installation
------------------------------------
To setup the ChatPDFs App, follow the steps given below:

1. Clone the repository to your local machine.

2. Install the required dependencies:
   ```
   pip install openai
   pip install langchain
   pip install streamlit
   pip install pypdf2
   pip install tiktoken
   pip install dot-env
   pip install faiss-cpu
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_openai_api_key
```

## Usage
-----------
To use the ChatPDFs App, follow the steps given below:

1. After installing the required dependencies and added the OpenAI API key to the `.env` file, run the `app.py` file as follows:
   ```
   streamlit run app.py
   ```

2. The application will launch in your default web browser, displaying the user interface.

3. Upload the PDF document(s) into the application.

4. Ask questions in natural language about the uploaded PDF(s) using the chat interface.
