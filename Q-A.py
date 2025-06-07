import streamlit as st
import fitz  # PyMuPDF
from groq import Groq

# Initialize Groq client
groq_client = Groq(api_key="Your Key")  # Replace with your actual key

# Function to extract text
def extract_text_from_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

# Split into chunks
def split_text(text, max_chars=4000):
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

# Ask Groq model
def ask_question_with_context(chunks, question):
    context = "\n\n".join(chunks[:3])  # Use first 3 chunks
    prompt = f"""
You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""
    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",  # or llama3-70b-8192
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# Streamlit App
st.set_page_config(page_title="PDF Q&A with Groq", layout="wide")
st.title("📄 Ask Questions About Your PDF")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
question = st.text_input("Ask a question about the document:")

if uploaded_file and question:
    with st.spinner("Reading PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        chunks = split_text(text)

    with st.spinner("Thinking..."):
        answer = ask_question_with_context(chunks, question)

    st.subheader("Answer:")
    st.markdown(answer)
