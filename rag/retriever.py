from rag.embedder import build_vector_db

vector_db = build_vector_db()

retriever = vector_db.as_retriever()

def retriever_doc(query):
    #docs = retriever.get_relevant_documents(query) ---- Depricated
    docs = retriever.invoke(query)

    context = "\n".join([f"{doc.metadata['source']} : {doc.page_content}" for doc in docs])

    return context