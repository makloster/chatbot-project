# 🔐 FastAPI Challenge – API de Algoritmos Protegida con JWT

Este proyecto fue desarrollado como parte del **CAP01_CHALLENGE** de Henry, con el objetivo de demostrar cómo un copiloto de código asistido por IA puede ayudar a construir una API funcional y segura desde cero, utilizando herramientas modernas del ecosistema Python. Las consignas para el Challenge se encuentran en el documento `README_consignas.md`.

El enfoque principal fue implementar una API que:

- Expone algoritmos clásicos como Bubble Sort o Búsqueda Binaria
- Protege los endpoints mediante autenticación con tokens JWT
- Almacena contraseñas de forma segura con hash
- Es fácilmente testeable y extensible

---

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) – Framework web moderno y de alto rendimiento
- [Pydantic](https://docs.pydantic.dev/) – Validación de datos
- [Passlib](https://passlib.readthedocs.io/) – Cifrado de contraseñas
- [PyJWT](https://pyjwt.readthedocs.io/) – Autenticación con tokens JWT
- [pytest](https://docs.pytest.org/) – Testing automatizado
- [Ruff](https://docs.astral.sh/ruff/) – Linter y formateador todo-en-uno

---

## 🧠 Objetivos del challenge

El desafío consistía en implementar:

### 1. Endpoints de algoritmos

- `/bubble-sort`: Ordena una lista usando Bubble Sort
- `/filter-even`: Filtra números pares
- `/sum-elements`: Calcula la suma total
- `/max-value`: Devuelve el máximo valor
- `/binary-search`: Busca un número en una lista ordenada
- `/merge-sort`: Nuevo – ordena usando Merge Sort
- `/min-value`: Nuevo – devuelve el número mínimo
- `/mean-median`: Nuevo – calcula media y mediana

### 2. Autenticación con JWT

- Registro e inicio de sesión de usuarios
- Protección de endpoints mediante `?token=...`

### 3. Cifrado seguro de contraseñas

- Contraseñas almacenadas con `passlib` y `bcrypt`

---

## ⚙️ Instalación y ejecución

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
uvicorn main:app --reload
```

---

## 🔐 Autenticación

### Registro de usuario

```http
POST /register
{
  "username": "user1",
  "password": "pass1"
}
```

### Inicio de sesión

```http
POST /login
{
  "username": "user1",
  "password": "pass1"
}
```

➡️ Devuelve un `access_token` JWT.

---

## 📌 Uso de los endpoints protegidos

Todos los endpoints requieren un `token` como parámetro de consulta:

```http
POST /<endpoint>?token=<access_token>
```

### Ejemplo:

```http
POST /sum-elements?token=eyJhbGciOiJIUzI1NiIsInR5cCI6...
{
  "numbers": [1, 2, 3]
}
```

---

## 🧪 Testing

Los tests automatizados predeterminados por el equipo de Henry están definidos en `tests.py`.

Para ejecutarlos:

```bash
pytest tests.py
```

Se testean:

- Registro y login
- Acceso válido e inválido a endpoints
- Funcionalidad de todos los algoritmos

---

## 🧼 Formato del código

El código está validado y formateado con [**Ruff**](https://docs.astral.sh/ruff/), una herramienta moderna y veloz para estilo de código, linting y ordenamiento de imports.

Como Ruff no se integra como formateador en VS Code aún, el formato se aplica desde la terminal:

```bash
ruff format .
```

---

## 🧑‍💻 Autor

Desarrollado por _makloster_, como parte del proceso de aprendizaje en Henry, con el soporte de varias herramientas de IA. 🚀

---

## 📄 Licencia

Este proyecto se entrega como parte de un ejercicio educativo. Libre para su uso y adaptación con fines no comerciales.
