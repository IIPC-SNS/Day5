import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
import os

# --- Set your API key directly (⚠️ not secure for production) ---
os.environ["GOOGLE_API_KEY"] = "AIzaSyBwZzZ3ADbW9M-_HzuZubtA65m1Fr4zbIA"

# --- Set page config ---
st.set_page_config(page_title="English to French Translator", page_icon="🌍")

# --- Title ---
st.title("🌍 English to French Translator")
st.markdown("Translate English sentences to French using Google Gemini + LangChain.")

# --- Input: English sentence ---
english_input = st.text_input("✍️ Enter a sentence in English:")

# --- Translate Button ---
if st.button("🌐 Translate"):
    if not english_input.strip():
        st.warning("Please enter a sentence to translate.")
    else:
        try:
            # Step 1: Set up the LLM
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

            # Step 2: Create a prompt template
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant that translates English to French."),
                ("user", "Translate the following sentence into French: {sentence}")
            ])

            # Step 3: Create the chain using `|` operator
            chain: Runnable = prompt | llm

            # Step 4: Run the chain
            response = chain.invoke({"sentence": english_input})

            # Step 5: Display the translation
            translated_text = response.content
            st.success("✅ Translation successful!")
            st.markdown(f"**French Translation:**\n\n{translated_text}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
