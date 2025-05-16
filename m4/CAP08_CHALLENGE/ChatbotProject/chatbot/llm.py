from typing import Generator, List, Dict
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY no definido en .env")

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def stream_chat_response(messages: List[Dict[str, str]]) -> Generator[str, None, None]:
    try:
        stream = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=messages,
            temperature=0.7,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta
            content = delta.content or ""
            yield content

    except Exception as e:
        yield f"\n[LLM Error]: {str(e)}"
