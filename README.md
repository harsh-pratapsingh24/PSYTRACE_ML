# Modular AI Therapist Chatbot (Groq Powered)

A clean, beginner-friendly AI therapist chatbot split across 5 Jupyter Notebooks to demonstrate modular programming and separation of concerns. Optimized with the **Groq API** for lightning-fast, empathetic responses.

## 🚀 Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install groq python-dotenv textblob
   ```

2. **Configure API Key**:
   - Rename `.env.example` to `.env`.
   - Open `.env` and paste your Groq API Key:
     ```
     GROQ_API_KEY=gsk_your_actual_key_here
     ```

3. **Run the Chatbot**:
   - Open **`05_Main_Chatbot_Loop.ipynb`**.
   - Run all cells.
   - The chatbot will automatically detect your Groq API key and start the session.

## 📂 Project Structure
- **`01_Memory_Module_v2.ipynb`**: Handles conversation history and persistent JSON profiles.
- **`02_Analysis_Module.ipynb`**: Performs sentiment (TextBlob) and psychological insight extraction.
- **`03_Prompt_Builder.ipynb`**: Synthesizes data into a professional, empathetic therapist prompt.
- **`04_LLM_Interaction.ipynb`**: Manages the live connection to **Groq (Llama-3)**.
- **`05_Main_Chatbot_Loop.ipynb`**: The central orchestrator.

## 🛠️ Features
- **Lightning Fast**: Powered by Groq's LPUs for near-instant responses.
- **Empathetic Persona**: Designed for active listening and reflective therapy.
- **Persistent Memory**: Remembers user details across sessions via JSON.
- **Context-Aware**: Adjusts its tone based on real-time emotional analysis.

## 📝 Prerequisites
- Python 3.x
- Jupyter Notebook
- A Groq API Key (get one at [console.groq.com](https://console.groq.com/))
