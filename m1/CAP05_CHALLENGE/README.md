## 🧠 InternetWhisper — Descripción General

**InternetWhisper** es un chatbot de IA que combina modelos de lenguaje avanzados (LLMs) con búsqueda web en tiempo real, ofreciendo respuestas actualizadas y contextualizadas.

### 🔍 Características Clave

- **Búsqueda Web**: Responde con información reciente.
- **Contexto Conversacional**: Mantiene el hilo de la charla.
- **Interfaz Intuitiva**: Interacción sencilla vía navegador.
- **Personalización**: Adaptable a distintos usos.

### ⚙️ Requisitos

- Python 3.8+
- API de un LLM (OpenAI, Anthropic, etc.)
- Conexión a Internet

### 🎯 Valor Agregado

Ideal para **investigadores**, **profesionales** y **usuarios** que necesitan información actualizada y razonamiento contextual.
Su arquitectura modular permite múltiples aplicaciones, desde **uso personal** hasta **soluciones empresariales**.

## 🛠️ Arquitectura Técnica de InternetWhisper

InternetWhisper está diseñado con una arquitectura modular que separa responsabilidades para mayor escalabilidad y mantenibilidad.

### 🧩 Componentes Principales

- **Frontend (UI)**: React + API REST (Flask)
- **Procesamiento**: Gestor de conversaciones y analizador de consultas
- **Motor de Búsqueda**: Conexión con SerpAPI, Google CSE o Bing + caché
- **Motor de IA**: Integración con LLMs (GPT-4, Claude, LLaMA) + prompt engineering + retroalimentación
- **Infraestructura**: Logging, autenticación, monitoreo

### 🔁 Flujo de Datos

1. El usuario envía una consulta.
2. Se analiza si requiere búsqueda externa.
3. Se enruta al LLM o al motor de búsqueda.
4. Se genera una respuesta combinada y se entrega al usuario.

### ⚙️ Tecnologías Clave

**Backend**: Python, Flask, SQLAlchemy, Redis, Celery
**Frontend**: React, Redux, Socket.IO
**IA**: OpenAI/Anthropic APIs, LangChain, embeddings
**Búsqueda**: SerpAPI, Google CSE, BeautifulSoup, Scrapy
**Almacenamiento**: PostgreSQL, MongoDB

### 🚀 Rendimiento y Escalabilidad

- Paralelización de búsquedas
- Caché inteligente
- Compresión de contexto
- Procesamiento asíncrono
- Arquitectura basada en microservicios (Docker + Kubernetes)

### 🔐 Seguridad y Privacidad

- Cifrado de datos sensibles
- Sanitización de entradas
- Retención controlada de datos
- Anonimización opcional

> Esta arquitectura permite respuestas precisas y actuales, combinando lo mejor del razonamiento LLM con acceso web en tiempo real.

## 🔧 Configuración de Variables de Entorno

La configuración de variables de entorno permite personalizar InternetWhisper y proteger credenciales sensibles.

### 🛡️ Variables Requeridas

#### 🔑 LLM (Modelo de Lenguaje)

```env
LLM_PROVIDER=openai         # o anthropic
OPENAI_API_KEY=sk-xxx       # o ANTHROPIC_API_KEY=xxx
LLM_MODEL=gpt-4             # o claude-2, etc.
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2000
```

#### 🌐 Búsqueda Web

```env
SEARCH_PROVIDER=serpapi
SERPAPI_API_KEY=serpapi_xxx
# Google CSE (opcional):
GOOGLE_CSE_ID=xxx
GOOGLE_API_KEY=xxx
```

#### 🗃️ Base de Datos

```env
DB_TYPE=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_NAME=internetwhisper
DB_USER=dbuser
DB_PASSWORD=dbpassword
```

#### ⚙️ Redis (opcional)

```env
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=redispassword
REDIS_DB=0
```

#### ⚙️ Configuración General y Rendimiento

```env
APP_SECRET_KEY=una_clave_segura
APP_DEBUG=false
APP_HOST=0.0.0.0
APP_PORT=5000
LOG_LEVEL=info

MAX_CONCURRENT_SEARCHES=3
CACHE_EXPIRATION=3600
REQUEST_TIMEOUT=30
MAX_HISTORY_LENGTH=10
```

---

### 🧩 Métodos de Configuración

- **.env (Recomendado en desarrollo)**
  Crear `.env` con los valores anteriores.

- **Variables del sistema**
  En Linux/macOS:

  ```bash
  export OPENAI_API_KEY=sk-xxx
  export LLM_MODEL=gpt-4
  ```

  En PowerShell (Windows):

  ```powershell
  $env:OPENAI_API_KEY = "sk-xxx"
  ```

- **Docker**

  ```bash
  docker run -e OPENAI_API_KEY=sk-xxx -e LLM_MODEL=gpt-4 internetwhisper
  ```

- **docker-compose.yml**

  ```yaml
  services:
    app:
      image: internetwhisper
      environment:
        - OPENAI_API_KEY=sk-xxx
        - LLM_MODEL=gpt-4
  ```

- **Archivo config.json**
  Alternativa para producción:

  ```json
  {
    "llm": { "provider": "openai", "api_key": "sk-xxx", "model": "gpt-4" },
    "search": { "provider": "serpapi", "api_key": "serpapi_123456" },
    "database": {
      "type": "postgresql",
      "host": "localhost",
      "port": 5432,
      "name": "internetwhisper",
      "user": "dbuser",
      "password": "dbpassword"
    }
  }
  ```

  Ejecutar con:

  ```bash
  export CONFIG_FILE_PATH=/path/to/config.json
  ```

---

### ✅ Verificación

```bash
python -m internetwhisper.utils.config_check
```

---

## 🚀 Correr InternetWhisper Localmente

Pasos esenciales para levantar InternetWhisper en tu entorno local.

### 🧰 Requisitos Previos

- Python 3.8+
- pip
- Git
- Node.js 14+
- (Opcional) PostgreSQL y Redis para producción

---

### 🔧 Setup Inicial

```bash
git clone https://github.com/tu-usuario/InternetWhisper.git
cd InternetWhisper
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

Crear y configurar `.env` con tus claves:

```env
OPENAI_API_KEY=sk-xxx
LLM_MODEL=gpt-4
SERPAPI_API_KEY=serpapi-xxx
DB_TYPE=sqlite
APP_SECRET_KEY=clave123
```

Inicializar base de datos:

```bash
python -m internetwhisper.db.init_db
```

---

### 🌐 Configurar el Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
```

Editar `.env.local` según la URL del backend.

---

### ▶️ Ejecutar en Modo Desarrollo

**Backend:**

```bash
python -m internetwhisper.app
# o flask run --debug
```

**Frontend:**

```bash
npm run dev
```

- Backend: [http://localhost:5000](http://localhost:5000)
- Frontend: [http://localhost:3000](http://localhost:3000)

---

### 🧪 Verificar la Instalación

Abrí el navegador y probá la app en `localhost:3000`.

---

### ⚙️ Redis y Celery (Opcional)

Instalar Redis y ejecutar:

```bash
redis-server
celery -A internetwhisper.tasks worker --loglevel=info
```

---

### 🧪 Ejecutar Pruebas

```bash
pytest
# o pruebas específicas:
pytest tests/test_llm_integration.py
```

---

### 🛠️ Producción

```bash
cd frontend
npm run build

gunicorn -w 4 -b 0.0.0.0:5000 "internetwhisper.app:create_app()"
```

Se recomienda usar Nginx como proxy inverso.

---

### 🔁 Desarrollo Continuo

- `flask run --debug` recarga cambios del backend.
- `npm run dev` recarga el frontend automáticamente.
- Activar hooks de calidad:

```bash
pre-commit install
```

## 📘 Documentación OpenAPI de la API

InternetWhisper ofrece documentación detallada de su API mediante la especificación OpenAPI, ideal para integradores y desarrolladores.

### 🧭 Acceso a la Documentación

- **Swagger UI (interactivo)**
  [http://localhost:5000/api/docs](http://localhost:5000/api/docs)

- **Especificación JSON/YAML**
  - [openapi.json](http://localhost:5000/api/openapi.json)
  - [openapi.yaml](http://localhost:5000/api/openapi.yaml)

Importable en herramientas como **Postman**, **Insomnia**, o **VSCode** (Thunder Client).

---

### 🧪 Generar Clientes API

**OpenAPI Generator:**

```bash
npm install @openapitools/openapi-generator-cli -g
openapi-generator-cli generate -i http://localhost:5000/api/openapi.json -g python -o ./client-python
```

**Swagger Codegen:**

```bash
java -jar swagger-codegen-cli.jar generate -i http://localhost:5000/api/openapi.json -l python -o ./client-python
```

---

### 🧱 Estructura de la API

- `/api/conversations` → Gestión de conversaciones
- `/api/chat` → Interacción con el chatbot
- `/api/search` → Búsqueda en Internet
- `/api/admin/*` → Administración
- `/api/auth/*` → Autenticación y manejo de tokens

---

### 🔐 Autenticación

Usa JWT:

```http
Authorization: Bearer {tu_token}
```

Obtené el token con `POST /api/auth/login`.

---

### 💬 Ejemplos

**Crear conversación**

```http
POST /api/conversations
Content-Type: application/json
Authorization: Bearer {token}
{
  "title": "Mi nueva conversación"
}
```

**Enviar mensaje**

```http
POST /api/conversations/{id}/messages
{
  "content": "¿Últimas noticias sobre IA?",
  "enable_web_search": true
}
```

---

### 🔢 Códigos de Estado HTTP

- `200 OK` – Éxito
- `201 Created` – Recurso creado
- `400 Bad Request` – Error de cliente
- `401 Unauthorized`, `403 Forbidden`, `404 Not Found`
- `500 Internal Server Error`

---

### 📌 Versionado y Rate Limiting

- Versión actual: `/api/v1/...`
- Límite: `60 req/min` (autenticado), `10 req/min` (no autenticado)

Headers:

```
X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset
```

---
