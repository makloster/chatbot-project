from chatbot.llm import stream_chat_response
from typing import List, Dict
import os
import pytest

@pytest.mark.skipif(
    not os.getenv("OPENROUTER_API_KEY"),
    reason="OPENROUTER_API_KEY no definida en .env"
)
def test_stream_chat_response_openrouter():
    messages: List[Dict[str, str]] = [
        {"role": "user", "content": "¿Cuál es la capital de Francia?"}
    ]

    chunks = list(stream_chat_response(messages))
    combined = "".join(chunks)

    assert isinstance(combined, str)
    assert len(combined) > 10
