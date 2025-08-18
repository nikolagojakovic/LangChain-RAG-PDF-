
**This project implements a Retrieval-Augmented Generation (RAG) pipeline for querying information from PDF documents using LangChain, ChromaDB, and Streamlit. It enables users to upload and index PDF files, generate vector embeddings (locally with Ollama or via AWS Bedrock), and interactively query the indexed content through a simple web UI.**

Key Components
PDF Ingestion:
**PDF files placed in the data directory are loaded and split into text chunks using LangChain’s text splitters**

Embeddings:
Each text chunk is converted into a vector embedding using either:

Ollama (local, free, CPU-based, using the nomic-embed-text model), or
AWS Bedrock (cloud-based, requires AWS credentials and incurs cost).
Vector Store:
Embeddings and metadata are stored in a local ChromaDB instance for efficient similarity search.

**Database Population:
The populate_db.py script processes PDFs, generates embeddings, and populates the Chroma database. Use --reset to clear and rebuild the database.**

Interactive UI:
The ui.py Streamlit app provides a web interface for querying the database. It displays the most relevant answer and allows users to view additional relevant results.

Docker Support:
The project includes a Dockerfile for easy containerization and deployment. (soon)

Typical Workflow
Start Ollama (if using local embeddings) and pull the required model.
Add PDFs to the data directory.
Run python [populate_db.py](http://_vscodecontentref_/4) --reset to index documents.
Launch the UI with streamlit run ui.py (or via Docker).
Ask questions in the web interface and view relevant answers from your PDF collection.
Requirements
Python 3.10+
Ollama (for local embeddings) or AWS credentials (for Bedrock)
Docker (optional, for containerized deployment)
