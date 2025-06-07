# Pdf---Q-A
🧠 PDF Q&amp;A Chatbot using Groq’s LLaMA 3 This interactive Streamlit app allows users to:  📄 Upload any PDF document ❓ Ask natural language questions based on the content 🤖 Get intelligent, context-aware answers powered by Groq’s LLaMA 3 model  

📄 Upload any PDF document
❓ Ask natural language questions based on the content
🤖 Get intelligent, context-aware answers powered by Groq’s LLaMA 3 model

🔧 How It Works:
PDF Parsing:
Uses PyMuPDF (fitz) to extract full text from uploaded PDFs

Chunking:
Breaks the text into manageable pieces (max 4000 characters per chunk)

AI-Powered Q&A:
Sends context + question to Groq's hosted LLaMA 3 model (llama3-8b-8192) for a smart response

Real-Time Chat Interface:
Built with Streamlit for an intuitive and responsive experience
