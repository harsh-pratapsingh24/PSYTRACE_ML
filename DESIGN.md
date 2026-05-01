# Design Document: Modular AI Therapist Chatbot

## 1. Project Overview
A modular AI therapist chatbot designed to be educational and beginner-friendly. The system is split across several Jupyter notebooks to demonstrate clear separation of concerns. The AI logic is powered by the **Groq API** for high-speed, empathetic dialogue.

## 2. Architecture
The application is divided into five core modules:

### 2.1 Memory Module (`01_Memory_Module.ipynb`)
- **Role**: State management for the conversation.
- **Key Data Structures**: 
  - `history`: List of dictionaries containing `role` and `content`.
  - `user_profile`: Dictionary containing persistent facts about the user.
- **Functions**:
  - `save_interaction(role, text)`
  - `get_recent_history(n)`
  - `update_profile(insights)`

### 2.2 Analysis Module (`02_Analysis_Module.ipynb`)
- **Role**: NLP processing of user input.
- **Functions**:
  - `analyze_sentiment(text)`: Sentiment analysis using TextBlob.
  - `detect_emotional_tone(text)`: Rule-based emotion detection.
  - `detect_risk(text)`: Basic keyword-based safety check.

### 2.3 Prompt Builder (`03_Prompt_Builder.ipynb`)
- **Role**: Constructing the LLM context.
- **Functions**:
  - `get_therapist_persona()`: Defines the empathetic persona guidelines.
  - `build_final_prompt(user_text, history, memory, analysis)`: Merges all context into a structured prompt.

### 2.4 LLM Interaction Module (`04_LLM_Interaction.ipynb`)
- **Role**: API communication with **Groq**.
- **Functions**:
  - `initialize_api()`: Configures the Groq client.
  - `get_ai_response(prompt)`: Sends the prompt to Groq (Llama-3) and returns the text.

### 2.5 Main Chatbot Loop (`05_Main_Chatbot_Loop.ipynb`)
- **Role**: User Interface and Orchestration.

## 3. Technology Stack
- **Language**: Python 3.x
- **Environment**: Jupyter Notebooks
- **Libraries**:
  - `groq` (for AI generation)
  - `python-dotenv` (for API key management)
  - `textblob` (for sentiment analysis)

## 4. Data Flow
`User Input` -> `Analysis` -> `Memory (Short + Long)` -> `Prompt Builder` -> `Groq API` -> `User Display`

## 5. Example Conversation Flow
- **User**: "I'm feeling really anxious about my boss today."
- **Analysis**: Sentiment: `negative`, Tone: `anxious`, Concern: `work`.
- **Memory**: Stores "Anxiety about work" in `memory.json`.
- **AI Response**: "It sounds like there's a lot of pressure coming from your workplace right now. I'm here to listen—what specifically about your boss is making you feel this way?"

## 6. Future Improvements
- **Crisis Detection 2.0**: Integrate a specialized NLP model for distress detection.
- **Vector Memory (RAG)**: Replace JSON with a Vector Database (like ChromaDB).
- **Voice Interface**: Integrate STT/TTS for hands-free sessions.
