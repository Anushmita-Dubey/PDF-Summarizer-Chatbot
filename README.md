<img width="1915" height="861" alt="image" src="https://github.com/user-attachments/assets/9a7e4538-a4c4-4756-8f22-db5887702e20" />

# 🤖 PDF Summarizer Chatbot

## 1) Project Overview  
This is a Streamlit-based web application that allows users to upload a PDF file, extract its text, and interact with the document through a chatbot interface. The chatbot uses the **Mistral** language model served locally via **Ollama** to answer user queries based on the uploaded document.

## 2) Project Purpose  
The purpose of this project is to create a simple and efficient tool for summarizing and interacting with PDF documents. It allows users to ask questions about a document’s content without having to read the entire file, making document analysis faster and easier.

## 3) Features  
- 📄 Upload and extract text from PDF files  
- 🤖 Question-answering using Mistral via Ollama  
- 💬 Chat interface with memory  
- 🎨 Light/Dark theme toggle  
- 🗑️ Option to clear chat history  
- ⚙️ Fully local setup with no external API calls

## 4) Getting Started  

### i) Clone the Repository
```bash
git clone https://github.com/Anushmita-Dubey/pdf-summarizer-chatbot.git
cd pdf-summarizer-chatbot
```
### ii) Install Dependencies
```bash
pip install -r requirements.txt
```

### iii) Run the Application
```bash
ollama run mistral
```

Then start the Streamlit app:

```bash
streamlit run app.py
```

## 5) Future Enhancements
-🔍 OCR support for scanned PDFs
-📊 Multi-page summarization and keyword extraction
-🌐 Deployable version for cloud use
-💡 Support for other local models (LLaMA 2, Gemma, etc.)
-📝 Option to export chat and summary

## 6) Acknowledgments
-Thanks to Streamlit for the intuitive UI framework
-Gratitude to Ollama for enabling easy local LLM usage
-Mistral model credits to the open-source ML community
-Created by Anushmita Dubey, 2025
