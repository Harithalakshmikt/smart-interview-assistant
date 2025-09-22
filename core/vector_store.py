from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

def build_faiss_index(text, embedding_model):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    return FAISS.from_documents(docs, embedding_model)

def retrieve_context(db, query, k=3):
    results = db.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in results])
