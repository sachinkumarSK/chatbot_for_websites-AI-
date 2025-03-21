import google.generativeai as genai
import os

# Load API key
genai.configure(api_key=os.getenv("apikeyhere(i used gemini ai)"))

# Load text content from the file
def load_text():
    with open("college_info.txt", "r", encoding="utf-8") as file:
        return file.read()

COLLEGE_INFO = load_text()

# Function to get AI response
def get_ai_response(user_message):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use your preferred model

    # Format the prompt to restrict answers
    prompt = f"""You are an AI assistant for a college website. 
    Answer only based on the following information:
    
    {COLLEGE_INFO}

    If the question is unrelated, reply with:
    'I can only answer questions about college facilities like fees, transport, and infrastructure.'
    
    User question: {user_message}
    """

    response = model.generate_content(prompt)

    return response.text.strip() if response and response.text else "I'm unable to answer right now."
