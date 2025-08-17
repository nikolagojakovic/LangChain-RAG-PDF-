import streamlit as st
from langchain.vectorstores.chroma import Chroma
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

st.title("LangChain RAG Demo")

query = st.text_input("Enter your question:")

if query:
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function()
    )
    results = db.similarity_search(query, k=5)
    if results:
        # Show only the top result as the main response
        st.subheader("Response")
        st.write(results[0].page_content)

        # Show other results in an expandable section
        if len(results) > 1:
            with st.expander("Other relevant results"):
                for i, doc in enumerate(results[1:], 2):
                    st.markdown(f"**Result {i}:**")
                    st.write(doc.page_content)
                    st.write(doc.metadata)
    else:
        st.write("No relevant results found in the database.")