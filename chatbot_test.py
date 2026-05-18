from chatbot.gemini_chatbot import (
    medical_chatbot
)

response = medical_chatbot(
    "What foods should diabetic patients avoid?"
)

print(response)