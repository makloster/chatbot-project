import sys
import os
import importlib.util

REQUIRED = [
    "openai",
    "dotenv",
    "requests",
    "tqdm",
    "beautifulsoup4",
    "lxml",
    "httpx",
    "newspaper",
    "pytest",
]

def check_module(module: str) -> bool:
    return importlib.util.find_spec(module) is not None

def main():
    print("🔍 Verificando entorno de Python...\n")

    print(f"🧠 Python: {sys.version}")
    print(f"📁 Entorno: {sys.prefix}")
    print(f"📦 requirements.txt: {'requirements.txt' in os.listdir()}\n")

    errors = 0
    for module in REQUIRED:
        found = check_module(module)
        status = "✅" if found else "❌"
        print(f"{status} {module}")
        if not found:
            errors += 1

    print("\n✔️ Listo!" if errors == 0 else f"\n❗Faltan {errors} módulo(s). Instalá con:\n  pip install -r requirements.txt")

if __name__ == "__main__":
    main()
