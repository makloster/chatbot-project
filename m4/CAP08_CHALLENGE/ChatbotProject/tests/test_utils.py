from chatbot.utils import build_messages
from typing import List, Dict

def test_build_messages_basic():
    history: List[Dict[str, str]] = [
        {"role": "user", "content": "Hola"},
        {"role": "assistant", "content": "¡Hola! ¿En qué puedo ayudarte?"},
    ]
    context = "Esto es contexto externo"

    result = build_messages(history, context)

    assert isinstance(result, list)
    assert len(result) >= 3  # incluye system + 2 turnos + contexto
    assert result[0]["role"] == "system"
    assert result[-1]["content"].startswith("Contexto")
