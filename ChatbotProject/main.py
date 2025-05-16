from typing import List
import time
from dotenv import load_dotenv
from chatbot.memory import MemoryManager
from chatbot.search import search_query
from chatbot.extractor import extract_text_from_urls
from chatbot.llm import stream_chat_response
from chatbot import MessageType
from chatbot.utils import build_messages


load_dotenv()


def run_chatbot() -> None:
    memory = MemoryManager()
    print("\n🤖 ¡ForceBot listo! Dime tu inquietud, amigo, o 'salir' para terminar.\n")

    while True:
        user_input = input("\n> USUARIO: ").strip()
        if user_input.lower() in ("salir", "exit", "quit"):
            print("\n🖐🏼 ¡Que la Fuerza esté contigo!")
            break

        memory.add_user_message(user_input)

        print("\n🔍 Consultando al Cosmos...")
        urls: List[str] = search_query(user_input)
        web_context: str = extract_text_from_urls(urls)

        print("\n🤖 Trayendo La Respuesta...\n")
        messages: List[MessageType] = build_messages(memory.get_history(), web_context)

        response_text: str = ""
        for chunk in stream_chat_response(messages):
            print(chunk, end="", flush=True)
            response_text += chunk
            time.sleep(0.01)

        print("\n\n🔗 Fuentes:")
        for url in urls:
            print(f"- {url}")

        memory.add_assistant_message(response_text)


if __name__ == "__main__":
    run_chatbot()
