import streamlit as st
import PyPDF2
import requests

# --------------------- Streamlit Theme Setup ---------------------
st.set_page_config(page_title="🤖PDF Summarizer Chatbot")

ms = st.session_state
if "themes" not in ms:
    ms.themes = {"current_theme": "light",
                 "refreshed": True,

                 "light": {"theme.base": "dark",
                           "theme.backgroundColor": "#FFFFFF",
                           "theme.primaryColor": "#6200EE",
                           "theme.secondaryBackgroundColor": "#F5F5F5",
                           "theme.textColor": "000000",
                           "button_face": "🌜"},

                 "dark": {"theme.base": "light",
                          "theme.backgroundColor": "#121212",
                          "theme.primaryColor": "#BB86FC",
                          "theme.secondaryBackgroundColor": "#1F1B24",
                          "theme.textColor": "#E0E0E0",
                          "button_face": "🌞"},
                 }

def ChangeTheme():
    previous_theme = ms.themes["current_theme"]
    tdict = ms.themes["light"] if previous_theme == "light" else ms.themes["dark"]
    for k, v in tdict.items():
        if k.startswith("theme"):
            st._config.set_option(k, v)
    ms.themes["refreshed"] = False
    ms.themes["current_theme"] = "dark" if previous_theme == "light" else "light"

btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
st.button(btn_face, on_click=ChangeTheme)

if ms.themes["refreshed"] == False:
    ms.themes["refreshed"] = True
    st.rerun()


# --------------------- Sidebar ---------------------
with st.sidebar:
    st.title('🤖PDF Summarizer Chatbot')

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    pdf_text = ""

    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            reader = PyPDF2.PdfReader(uploaded_file)
            for page in reader.pages:
                pdf_text += page.extract_text() or ""
        st.success("PDF uploaded and text extracted!")

    st.markdown('''
        Developed by ANUSHMITA DUBEY - 2025  
        Visit my GitHub profile <a href="https://github.com/Anushmita-Dubey" style="color:white; background-color:#3187A2; padding:3px 5px; text-decoration:none; border-radius:5px;">here</a>
        ''', unsafe_allow_html=True)

# --------------------- Mistral Chat via Ollama ---------------------
def generate_mistral_response(text, question):
    system_prompt = "You are a helpful assistant. You answer based only on the PDF content given."
    prompt = f"{system_prompt}\n\nContext:\n{text[:5000]}\n\nQuestion: {question}\nAnswer:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    result = response.json()
    return result.get("response", "No response received from Mistral.")

# --------------------- Chat Memory & Display ---------------------
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Upload a PDF file from the sidebar to get started."}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Upload a PDF file from the sidebar to get started."}]
st.sidebar.button('🗑️ Clear Chat History', on_click=clear_chat_history)

# --------------------- User Input & Answer ---------------------
if pdf_text:
    question = st.chat_input("Ask a question about the PDF:")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_mistral_response(pdf_text, question)
                st.write(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

