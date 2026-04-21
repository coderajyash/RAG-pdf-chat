# 📄 PDFOracle

PDFOracle is a fully local, free RAG (Retrieval-Augmented Generation) application that lets users chat with PDF documents using natural language. It combines document ingestion, text chunking, semantic embeddings, vector search, and a local language model to generate answers grounded in the content of the uploaded PDF. The entire system runs on the user's machine, making it private, cost-free, and independent of paid external APIs.

---

## 🧩 What PDFOracle Solves

Working with long PDF files can be frustrating when users need specific information quickly. Traditional PDF reading and keyword search are often slow, manual, and limited because they depend on exact word matches rather than meaning.

PDFOracle solves this problem by turning a static PDF into an interactive question-answering system. Instead of scanning pages manually, users can ask questions in plain English and receive relevant answers based on semantically similar content retrieved from the document.

This is especially useful for:

- Technical documentation
- Research papers
- Study material
- Guides and handbooks
- Policy documents
- Product manuals
- Internal company PDFs

In short, PDFOracle transforms a PDF from something you read linearly into something you can query conversationally.

---

## 🚀 Core Features

- Chat with any PDF using natural language
- Fully local and free pipeline
- No OpenAI or paid API required
- Semantic search instead of simple keyword matching
- Persistent vector storage using Qdrant
- Local embeddings using HuggingFace
- Local answer generation using Ollama
- Grounded responses based only on document context
- Reusable indexed collection for repeated querying
- Privacy-first architecture where data never leaves the machine

---

## 🏗️ Project Architecture

PDFOracle follows a Retrieval-Augmented Generation (RAG) architecture.

The project is divided into two main phases:

1. **Document Ingestion Phase**
2. **Question Answering / Chat Phase**

### 1. Document Ingestion Phase

This phase prepares the PDF for semantic search.

Flow:

- Load the PDF file from local storage
- Extract text page by page
- Split the text into smaller overlapping chunks
- Convert each chunk into vector embeddings
- Store those embeddings in Qdrant along with the chunk text and metadata

### 2. Chat Phase

This phase answers user questions.

Flow:

- Take the user's query
- Convert the query into an embedding
- Search the Qdrant collection for the most similar chunks
- Format the retrieved chunks into context
- Send the context and question to a local LLM
- Generate a final answer grounded in the retrieved PDF content

---

## 🔁 End-to-End Flow

### Ingestion Pipeline

```text
PDF File
   ↓
PyPDFLoader
   ↓
RecursiveCharacterTextSplitter
   ↓
HuggingFaceEmbeddings
   ↓
QdrantVectorStore
   ↓
Stored collection: "pdforacle"
```

### Query Pipeline

```text
User Question
   ↓
Embed Question
   ↓
Search Qdrant for similar chunks
   ↓
Retrieve top-k chunks
   ↓
Format chunks into context
   ↓
Inject context into prompt
   ↓
Send to local LLM
   ↓
Generate grounded answer
```


## 📄 License

MIT License — free to use, modify, and distribute.