from google import genai

# ---------------- API KEY ----------------

API_KEY = "AIzaSyDhaEN7An0alg4KHACRGyEObMHdWb9Ag6c"

# ---------------- CLIENT ----------------

client = genai.Client(api_key=API_KEY)

# ---------------- CHATBOT FUNCTION ----------------

def medical_chatbot(user_query):

    prompt = f"""
    You are an AI healthcare assistant.

    Give short, helpful, and safe medical guidance.

    Do not prescribe dangerous medicines.
    Do not pretend to be a doctor.

    User Question:
    {user_query}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text