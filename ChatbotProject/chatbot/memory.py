from typing import List, Dict


class MemoryManager:
    def __init__(self) -> None:
        self._history: List[Dict[str, str]] = []

    def add_user_message(self, content: str) -> None:
        self._history.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str) -> None:
        self._history.append({"role": "assistant", "content": content})

    def get_history(self) -> List[Dict[str, str]]:
        return self._history.copy()

    def reset(self) -> None:
        self._history.clear()
