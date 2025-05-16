# 🤖 Chatbot con Búsqueda Web y LLM (OpenRouter)

Este proyecto implementa un chatbot en consola que:

- ✅ Mantiene historial de conversación (memoria contextual)
- 🔍 Realiza búsquedas en tiempo real usando [Serper.dev](https://serper.dev/)
- 📄 Extrae texto principal de las páginas encontradas
- 💬 Genera respuestas en streaming usando [OpenRouter.ai](https://openrouter.ai/)
- 🔗 Cita fuentes al final de cada respuesta
- 🧪 Incluye pruebas automatizadas con `pytest`

---

## 🚀 Requisitos

- Python 3.11 o 3.12
- Acceso a:
  - [Serper.dev API Key](https://serper.dev/)
  - [OpenRouter API Key](https://openrouter.ai/keys)

---

## 📦 Instalación

```bash
git clone https://github.com/makloster/chatbot-project
cd ChatbotProject

python -m venv venv
source venv/Scripts/activate  # o ./venv/Scripts/activate.ps1 en PowerShell

pip install -r requirements.txt
```

---

## 🔐 Configuración (.env)

Crear un archivo `.env` en la raíz (ver ejemplo .env-sample) con:

```env
SERPER_API_KEY=tu_clave_de_serper
OPENROUTER_API_KEY=tu_clave_de_openrouter
```

---

## 🧠 Uso

Ejecutá el chatbot desde la raíz:

```bash
python main.py
```

Ejemplo:

```bash
> USUARIO: ¿Qué es la inteligencia artificial?
```

El chatbot buscará contexto online, lo procesará y generará una respuesta en streaming, citando las fuentes.

---

## 🧪 Pruebas

Correr todos los tests:

```bash
pytest -v
```

Test específico (por ejemplo `llm`):

```bash
pytest tests/test_llm.py
```

> 🔁 El test de `llm` se salta automáticamente si no hay API Key válida

---

## 🗂 Estructura del Proyecto

```
chatbot/
├── extractor.py        # extracción web
├── llm.py              # conexión a OpenRouter
├── memory.py           # historial en runtime
├── search.py           # API Serper.dev
├── utils.py            # builder de messages
├── __init__.py
main.py                 # interfaz de consola
tests/                  # pruebas unitarias
requirements.txt
.env                    # (se incluye un ejemplo .env-sample)
```

---

## 📚 Créditos

- LLM vía [OpenRouter.ai](https://openrouter.ai)
- Búsqueda con [Serper.dev](https://serper.dev)
- Extracción con `newspaper3k`
- Consola y streaming con Python estándar

---

## 📝 Licencia

MIT © 2025 — Manuel Kloster / Academia Henry
