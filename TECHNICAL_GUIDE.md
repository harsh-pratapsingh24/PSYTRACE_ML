# 🛠️ Deep-Dive Technical Manual: PsyTrace-ML

This manual provides an exhaustive breakdown of every module, function, and library used in the AI Therapist system.

---

## 📚 1. Core Technologies & Libraries

| Library | Purpose | Key Usage in Project |
| :--- | :--- | :--- |
| `groq` | **AI Inference** | Connects to Groq's LPU hardware to run the Llama-3 model at high speed. |
| `textblob` | **NLP Processing** | Calculates the numerical "polarity" (sentiment) of user messages. |
| `python-dotenv` | **Secret Management** | Securely loads API keys from the `.env` file into the system environment. |
| `json` | **Data Persistence** | Serializes Python dictionaries into a permanent file on your disk. |
| `os` | **System Pathing** | Handles file path resolution across different operating systems (Windows/Linux). |

---

## 🧩 2. Module-by-Module Function Directory

### 📝 Module 01: Memory (`01_Memory_Module_v2.ipynb`)
Handles the dual-layer storage system.
- `load_long_term_memory()`: 
    - **Logic**: Checks for `memory.json`. If found, parses the string into a Python `dict`.
- `save_long_term_memory()`: 
    - **Logic**: Converts the `long_term_data` dictionary into a formatted JSON string and writes it to disk.
- `add_to_history(role, content)`: 
    - **Logic**: Appends a message to `short_term_history`. If length > 10, it uses "list slicing" (`[-10:]`) to discard the oldest message.
- `update_note(note_text)`: 
    - **Logic**: Appends filtered insights to the persistent profile and triggers an immediate save.

### 🔍 Module 02: Analysis (`02_Analysis_Module.ipynb`)
The "Perception" engine that interprets human language.
- `analyze_sentiment(text)`: 
    - **Logic**: Passes text to `TextBlob`. It looks at the "adjective weight" to return `positive` (>0.1), `negative` (<-0.1), or `neutral`.
- `detect_emotional_tone(text)`: 
    - **Logic**: **Heuristic Rule-Matching**. It iterates through a dictionary of mapped keywords (e.g., "panic" -> "anxious") and returns the first match.
- `extract_psychological_insights(text)`: 
    - **Logic**: **Information Filtering**. Scans for specific "Therapeutic Triggers" (Work, Family, Sleep). If the input is just "Hello," this returns `None`, preventing memory clutter.
- `run_full_analysis(text)`: 
    - **Logic**: The **Wrapper Function**. Runs all the above functions in parallel and bundles the results into a single dictionary.

### 🎭 Module 03: Prompt Builder (`03_Prompt_Builder.ipynb`)
The architectural heart where "Context Injection" happens.
- `get_therapist_persona()`: 
    - **Logic**: Returns a static string of "System Instructions" that define the AI's constraints (validation, active listening).
- `build_final_prompt(user_text, recent_history, long_term_memory, analysis_data)`: 
    - **Logic**: **String Templating**. It constructs a structured document using Markdown headers (`## ROLE`, `## HISTORY`). It injects your name, your past insights, and your current mood into the prompt.

### 🚀 Module 04: LLM Interaction (`04_LLM_Interaction.ipynb`)
The bridge to the cloud.
- `initialize_api()`: 
    - **Logic**: Performs a "Robust Path Check" for the `.env` file using `os.getcwd()`. Configures the `groq` client with your key.
- `get_ai_response(prompt)`: 
    - **Logic**: **The Gatekeeper**. It attempts to call the Groq API using `llama-3.3-70b-versatile`. If the API fails or the key is missing, it automatically calls `get_mock_response()` as a fallback.

### 🕹️ Module 05: Main Loop (`05_Main_Chatbot_Loop.ipynb`)
The "Executive Function" that runs the show.
- `start_therapy_session()`: 
    - **Logic**: **Infinite Event Loop**. 
    - 1. Await input. 
    - 2. Trigger NLP Analysis. 
    - 3. Store Insights. 
    - 4. Construct Prompt. 
    - 5. Generate AI Response. 
    - 6. Display. 
    - 7. Loop until `quit`.

---

## 🌊 3. The Data Flow (Technical Path)
1. **Raw String** is captured by `input()`.
2. **Analysis Module** converts string into a **Metadata Dictionary**.
3. **Memory Module** updates the **JSON State**.
4. **Prompt Builder** merges **Metadata + JSON State + History** into one large **System Prompt**.
5. **LLM Module** sends this prompt via **HTTPS POST request** to Groq.
6. **JSON Response** from Groq is parsed, and the text is displayed.

---

## 🔒 4. Key Logic Concepts
- **Statelessness**: The AI (Llama-3) has NO memory of you. We create the *effect* of memory by sending your entire history and profile in every single API call.
- **Context Window Management**: Since we only send the last 10 messages, we ensure the prompt doesn't become too large for the AI to handle.
- **API Version Fallbacks**: Module 04 includes `try/except` blocks to handle model decommissioning or network outages without crashing the program.
