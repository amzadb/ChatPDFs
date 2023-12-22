import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import pdf_util as PdfUtil

from htmlTemplates import css, bot_template, user_template

def handle_userinput(user_question):
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Chat with PDFs",
        page_icon=":books:"
    )
    st.write(css, unsafe_allow_html=True)

    st.header("Chat with PDFs 💬")

    user_question = st.text_input("Ask a question about your PDFs:")
    if user_question:
        handle_userinput(user_question)
   
    #Sidebar content
    with st.sidebar:    
        st.header("Documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs and click on 'Process'", 
            type="pdf",
            accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = PdfUtil.get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = PdfUtil.get_text_chunks(raw_text)

                # create vector store
                vectorstore = PdfUtil.get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = PdfUtil.get_conversation_chain(vectorstore)
                
                # process completed
                st.write("**:green[The PDF(s) processed successfully!]**")

        st.markdown('''
            ## About
            This app is an LLM-powered chatbot built using:
            - [Streamlit](https://streamlit.io/)
            - [LangChain](https://python.langchain.com/)
            - [OpenAI](https://platform.openai.com/docs/models/) LLM Model
            ''')
        st.write("Made with ❤️ by Amzad Basha.")
            
if __name__ == '__main__':
    main()
