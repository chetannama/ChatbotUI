from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def build_vector_db():
    documents = []

#1. loader.load()
#Reads the file
#Converts the content into LangChain Document objects
#2. documents.extend()
#Adds those document objects to the documents list
#Important difference:
# Method	Behavior
# append()	Adds one item
# extend()	Adds multiple items
# Since loader.load() returns a list of documents, we use extend().

    for file in os.listdir("knowledge"):
        loader = TextLoader(f"knowledge/{file}")
        documents.extend(loader.load())


#1 RecursiveCharacterTextSplitter
# This class from LangChain is used to split large documents into smaller chunks.
# Why?
# LLMs have context window limits, so sending large documents directly is inefficient.

#2 chunk_size = 500
# This defines the maximum number of characters per chunk.
#3 chunk_overlap = 50
# This means 50 characters from the previous chunk are repeated in the next chunk.
#4 Why overlap?
# To preserve context between chunks.
#5 Why "Recursive" Splitter?
# This splitter tries to break text intelligently using separators.

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )


# splitter
# This is the object we created earlier using RecursiveCharacterTextSplitter.
# It already contains the configuration:
# chunk_size = 500
# chunk_overlap = 50
# 2. split_documents(documents)
# This method:
# Takes the list of documents
# Reads the text inside each document
# Splits the content into smaller chunks based on the config

    chunks = splitter.split_documents(documents)

# creates an instance of the embeddings model from OpenAI that will be used to convert text into vector embeddings.
# These embeddings represent the semantic meaning of the text.
    embeddings = OpenAIEmbeddings()

#This line uses the from_documents() method of FAISS through the LangChain integration to create a vector database from the document chunks.
    vector_db = FAISS.from_documents(chunks,embeddings)

    return vector_db