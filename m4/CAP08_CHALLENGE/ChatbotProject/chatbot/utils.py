from typing import List, Dict

MessageType = Dict[str, str]


def build_messages(
    history: List[Dict[str, str]],
    web_context: str,
) -> List[MessageType]:
    messages: List[MessageType] = []

    messages.append(
        {
            "role": "system",
            "content": (
                "Sos un chatbot que ayuda al usuario respondiendo con datos actualizados "
                "extraídos desde internet. Citá siempre tus fuentes al final."
            ),
        }
    )

    for turn in history:
        if turn["role"] == "user":
            messages.append({"role": "user", "content": turn["content"]})
        elif turn["role"] == "assistant":
            messages.append({"role": "assistant", "content": turn["content"]})

    if web_context:
        messages.append(
            {
                "role": "user",
                "content": f"Contexto de búsqueda:\n{web_context}",
            }
        )

    return messages
