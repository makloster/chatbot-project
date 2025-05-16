# chatbot.py

import os
import time
from typing import List, Tuple

# Cargar claves desde .env
from dotenv import load_dotenv
load_dotenv()

# Historial de la conversación
Conversation = List[Tuple[str, str]]
history: Conversation = []

def print_streaming_response(response: str):
    for char in response:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()  # salto de línea final

def mock_llm_response(prompt: str, context: str) -> str:
    """Simula una respuesta del LLM."""
    return f"Respuesta generada en base a tu pregunta y contexto web simulado.\n\n(Pregunta: {prompt})"

def run_chatbot():
    print("\n🤖 Chatbot listo. Escribe tu pregunta o 'salir' para terminar.\n")
    while True:
        user_input = input("> Tú: ").strip()
        if user_input.lower() in ("salir", "exit", "quit"):
            print("\n👋 ¡Hasta luego!")
            break

        # Agregar al historial
        history.append(("user", user_input))

        # TODO: integración con Serper y extracción de contexto web
        web_context = "[Contexto web simulado de Serper.dev]"

        # Preparar entrada para LLM
        prompt = user_input
        context = "\n".join([f"Usuario: {u}\nBot: {b}" for u, b in history[:-1]])

        # Obtener respuesta
        print("\n🤖 Pensando...")
        response = mock_llm_response(prompt, context + "\n" + web_context)

        print_streaming_response(response)

        # Agregar respuesta al historial
        history.append(("bot", response))

if __name__ == "__main__":
    run_chatbot()
