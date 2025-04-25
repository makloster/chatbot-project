# Diagrama de Componentes del Sistema de Reservación

```mermaid
graph TD
    UI["Frontend (Next.js)"]
    API["API Gateway / Next.js API Routes"]
    Auth["Servicio de Autenticación"]
    Search["Motor de Búsqueda de Disponibilidad"]
    Booking["Gestión de Reservas"]
    Availability["Administración de Disponibilidad en Tiempo Real"]
    Payment["Procesamiento de Pagos"]
    Notification["Sistema de Notificaciones"]
    DB["Base de Datos"]
    Cache["Cache en Memoria - Redis"]

    UI --> API

    API --> Auth
    API --> Search
    API --> Booking
    API --> Payment
    API --> Notification

    Search --> Availability
    Search --> Cache

    Booking --> Availability
    Booking --> DB
    Booking --> Cache

    Availability --> DB
    Payment --> DB
    Auth --> DB
    Notification --> DB
```

# Diagrama UML de Componentes del Sistema de Reservación

```mermaid
classDiagram
    direction TB

    class Frontend {
        +Next.js
        +Interfaz de usuario
    }

    class API_Gateway {
        +Rutas de API
        +Orquestación
    }

    class AuthService {
        +Login/Registro
        +Gestión de sesión
    }

    class InventoryService {
        +Consultar disponibilidad
        +Bloquear habitaciones
        +Actualizar ocupación
    }

    class BookingService {
        +Crear/modificar/cancelar reservas
        +Asociar habitaciones y usuarios
    }

    class PaymentProcessor {
        <<External System>>
        +Stripe / MercadoPago
        +Validación y cobros
    }

    class NotificationService {
        <<External System>>
        +Email / SMS
        +Confirmación y alertas
    }

    class Database {
        <<Storage>>
        +Usuarios
        +Reservas
        +Habitaciones
    }

    Frontend --> API_Gateway : Solicita acciones
    API_Gateway --> AuthService : Validación de usuario
    API_Gateway --> InventoryService : Consultar y bloquear disponibilidad
    API_Gateway --> BookingService : Crear o modificar reservas
    API_Gateway --> PaymentProcessor : Redirige para pagos
    API_Gateway --> NotificationService : Envía confirmaciones
    AuthService --> Database : Leer/Escribir usuarios
    InventoryService --> Database : Leer/Escribir habitaciones
    BookingService --> Database : Leer/Escribir reservas
```

# Diagrama de Secuencia UML

```mermaid
sequenceDiagram
    autonumber
    participant Usuario
    participant Frontend
    participant API
    participant AuthService
    participant InventoryService
    participant BookingService
    participant PaymentGateway
    participant DB

    Usuario->>Frontend: Ingresar fechas y criterios
    Frontend->>API: Solicitar disponibilidad
    API->>InventoryService: Buscar habitaciones disponibles
    InventoryService->>DB: Consultar disponibilidad
    DB-->>InventoryService: Lista de habitaciones libres
    InventoryService-->>API: Habitaciones disponibles
    API-->>Frontend: Mostrar resultados

    Usuario->>Frontend: Seleccionar habitación
    Frontend->>API: Iniciar reserva
    API->>AuthService: Validar autenticación
    AuthService-->>API: Usuario autenticado

    API->>BookingService: Crear reserva preliminar
    BookingService->>InventoryService: Bloquear habitación temporal
    InventoryService->>DB: Actualizar estado
    BookingService->>DB: Registrar reserva temporal
    BookingService-->>API: Reserva preliminar creada

    API-->>Frontend: Solicitar confirmación de pago
    Usuario->>Frontend: Confirmar y pagar
    Frontend->>API: Enviar detalles de pago
    API->>PaymentGateway: Procesar transacción
    PaymentGateway-->>API: Transacción exitosa

    API->>BookingService: Confirmar reserva
    BookingService->>DB: Actualizar estado a confirmado
    BookingService-->>API: Reserva confirmada
    API-->>Frontend: Mostrar confirmación final
    Frontend-->>Usuario: Reserva completada con éxito
```

# Diagrama de Transición de Estados

```mermaid
stateDiagram-v2
    [*] --> Pendiente : Usuario inicia reserva

    Pendiente --> Confirmada : Se validan datos y disponibilidad
    Confirmada --> Pagada : Pago exitoso
    Confirmada --> Cancelada : Usuario o sistema cancela
    Confirmada --> Modificada : Usuario solicita cambios

    Modificada --> Confirmada : Se actualizan detalles
    Modificada --> Cancelada : Se cancela tras cambios

    Pagada --> CheckIn : Fecha de entrada alcanzada
    CheckIn --> CheckOut : Usuario realiza salida

    Pagada --> Cancelada : Cancelación antes del check-in (según política)

    Cancelada --> [*]
    CheckOut --> [*]
```

# Estructura del Proyecto (monorepo estilo fullstack con Next.js + backend modular)

```text
/hotel-booking-system/
│
├── /apps/
│   ├── /web/                   # Frontend (Next.js app)
│   │   ├── /components/        # Componentes UI reutilizables
│   │   ├── /pages/             # Rutas y vistas
│   │   ├── /styles/            # Archivos CSS/Tailwind/config de estilo
│   │   ├── /utils/             # Helpers o funciones comunes
│   │   └── /public/            # Assets públicos
│   │
│   └── /admin/                 # (opcional) App de administración interna
│
├── /packages/
│   ├── /api/                   # Lógica del backend (API Routes o serverless)
│   │   ├── /auth/              # Servicios de autenticación
│   │   ├── /booking/           # Creación y gestión de reservas
│   │   ├── /inventory/         # Control de disponibilidad de habitaciones
│   │   ├── /payments/          # Integración con Stripe / MercadoPago
│   │   ├── /notifications/     # Emails, SMS, etc.
│   │   └── /users/             # Gestión de perfiles y roles
│   │
│   ├── /db/                    # Prisma ORM, migraciones, seeders
│   │   └── schema.prisma
│   │
│   ├── /lib/                   # Código compartido (validador, logger, helpers)
│   └── /types/                 # Tipos TypeScript globales
│
├── /infra/                     # IaC: Terraform, Docker, etc.
│   └── /nginx/                 # Configuración de reverse proxy
│
├── .env                        # Variables de entorno (dev)
├── docker-compose.yml          # Servicios locales
├── package.json
├── tsconfig.json
└── README.md
```

# Diagrama Entidad-Relación

```mermaid
erDiagram

    USERS ||--o{ BOOKINGS : hace
    ROOMS ||--o{ BOOKINGS : es_reservada_en
    BOOKINGS ||--o{ PAYMENTS : genera
    BOOKINGS ||--o{ NOTIFICATIONS : dispara

    USERS {
        string id PK
        string name
        string email
        string phone
        string role
        datetime created_at
    }

    ROOMS {
        string id PK
        string hotel_id
        string type
        int capacity
        float price_per_night
        boolean is_available
    }

    BOOKINGS {
        string id PK
        string user_id FK
        string room_id FK
        datetime check_in
        datetime check_out
        string status
        float total_amount
        datetime created_at
    }

    PAYMENTS {
        string id PK
        string booking_id FK
        string method
        float amount
        string status
        datetime paid_at
    }

    NOTIFICATIONS {
        string id PK
        string booking_id FK
        string type
        string recipient
        string message
        datetime sent_at
    }
```
