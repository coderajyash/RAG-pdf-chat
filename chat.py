from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# Embedding model (free, local)
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

# Connect to existing Qdrant collection
vectordb = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="pdforacle",
    url="http://localhost:6333"
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# Free local LLM via Ollama
llm = ChatOllama(model="llama3.2", temperature=0.2)

# System prompt
SYSTEM_PROMPT = """You are PDFOracle, an expert assistant that answers questions 
based strictly on the provided PDF context. 

Rules:
- Only use information from the context below to answer.
- If the answer is not in the context, say "I couldn't find that in the document."
- Be concise and cite relevant parts of the context.

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{question}")
])

def format_docs(docs):
    return "\n\n---\n\n".join(
        f"[Page {doc.metadata.get('page', '?')}]: {doc.page_content}"
        for doc in docs
    )

# RAG chain
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

# Chat loop
print("PDFOracle ready! Type 'exit' to quit.\n")
while True:
    user_query = input("You: ").strip()
    if user_query.lower() in ("exit", "quit"):
        break
    if not user_query:
        continue

    response = rag_chain.invoke(user_query)
    print(f"\nPDFOracle: {response}\n")