from google import genai

import os

from dotenv import load_dotenv

# LOAD ENV VARIABLES
load_dotenv()

# GET API KEY
api_key = os.getenv(
    "GEMINI_API_KEY"
)

# INITIALIZE GEMINI CLIENT
client = genai.Client(
    api_key=api_key
)

# =====================================================
# NORMAL CHATBOT
# =====================================================

def medical_chatbot(user_message):

    prompt = f"""
    You are an advanced AI healthcare assistant.

    Answer professionally in:
    - point-wise format
    - readable structure
    - concise explanations

    Use:
    - bullet points
    - headings
    - clean formatting

    User Question:
    {user_message}

    Add disclaimer:
    Consult a healthcare professional.
    """

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt
    )

    return response.text

# =====================================================
# VOICE AI ASSISTANT
# =====================================================

def voice_medical_chatbot(user_message):

    prompt = f"""
    You are a voice healthcare AI assistant.

    Reply VERY SHORT.

    Rules:
    - Maximum 3-4 sentences
    - No markdown
    - No headings
    - No bullet points
    - No stars
    - No hashtags
    - Sound natural and conversational
    - Keep response easy to speak aloud

    User Question:
    {user_message}
    """

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt
    )

    clean_response = response.text

    # REMOVE MARKDOWN SYMBOLS
    clean_response = clean_response.replace(
        "*",
        ""
    )

    clean_response = clean_response.replace(
        "#",
        ""
    )

    return clean_response