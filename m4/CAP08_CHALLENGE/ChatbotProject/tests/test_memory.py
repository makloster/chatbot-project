from chatbot.memory import MemoryManager


def test_dummy():
    assert True


def test_memory_add_and_get():
    memory = MemoryManager()
    memory.add_user_message("Hola")
    memory.add_assistant_message("¡Hola! ¿En qué puedo ayudarte?")
    history = memory.get_history()
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "Hola"
    assert history[1]["role"] == "assistant"


def test_memory_reset():
    memory = MemoryManager()
    memory.add_user_message("Mensaje temporal")
    memory.reset()
    assert memory.get_history() == []
