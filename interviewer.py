import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a professional AI interviewer.

Rules:
- Ask ONE interview question at a time.
- Wait for candidate answer.
- Evaluate the answer briefly.
- Give score out of 10.
- Ask next relevant question.
- Keep responses concise and professional.
"""

def ask_interview(field, history):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Conduct an interview for {field} role."}
    ]

    messages.extend(history)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content