import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("ERROR: No API key found.")
else:
    genai.configure(api_key=api_key)
    print("Attempting to list models...")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"Available Model: {m.name}")
    except Exception as e:
        print(f"FAILED to list models: {e}")
