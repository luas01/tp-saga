# TP-SAGA — Implementación del Patrón Saga con Microservicios
Este proyecto implementa el patrón **Saga** utilizando una arquitectura basada en microservicios. El objetivo es coordinar una serie de operaciones distribuidas (catálogo, pagos, compras, inventario) de forma confiable, aplicando compensaciones en caso de fallos.

# Estructura del Proyecto
TP-SAGA/
│
├── api-gateway/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── ms-catalogo/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── ms-compras/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── ms-inventario/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── ms-pagos/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── orquestador/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
├── README.md
└── .gitignore

# Cómo levantar el proyecto
Opción 1: Manualmente (modo desarrollo)
1. Crear entorno virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate    # Windows

2. Instalar dependencias por carpeta:
pip install -r ms-catalogo/requirements.txt
pip install -r ms-pagos/requirements.txt
pip install -r ms-compras/requirements.txt
pip install -r ms-inventario/requirements.txt
pip install -r orquestador/requirements.txt
pip install -r api-gateway/requirements.txt

3. Ejecutar cada microservicio en su propia terminal:
python ms-catalogo/app.py
python ms-pagos/app.py
python ms-compras/app.py
python ms-inventario/app.py
python orquestador/app.py
python api-gateway/app.py

Opción 2: Con Docker Compose

Construir y levantar todos los servicios:

docker-compose up --build


Acceder al único endpoint expuesto:

POST http://localhost:8000/saga

# Cómo probar el flujo Saga

Desde PowerShell o terminal:

(Invoke-WebRequest -Uri "http://localhost:8000/saga" -Method POST).Content


La respuesta puede ser:

Éxito: {"mensaje":"Saga completada con éxito"}

Falla: {"error":"Fallo en la compra, pago compensado"}

# Flujo de la Saga (Diagrama ASCII)
          +-----------+
          |   Cliente |
          +-----------+
                |
                v
        +----------------+
        |  API Gateway   |
        +----------------+
                |
                v
        +----------------+
        |  Orquestador   |
        +----------------+
         /       |       \
        v        v        v
+---------------+ +---------------+ +---------------+
|  ms-catalogo  | |   ms-pagos    | |  ms-compras   |
+---------------+ +---------------+ +---------------+
                          |
                          v
                  +---------------+
                  | ms-inventario |
                  +---------------+


El flujo es:

Cliente → Gateway → Orquestador

El orquestador coordina los microservicios en orden

Si falla algún paso, se ejecutan compensaciones (ej: cancelar pago, cancelar compra)

# Endpoints por microservicio
Servicio	Endpoint	Método
ms-catalogo	/obtener_producto	GET
ms-pagos	/procesar_pago	POST
ms-pagos	/cancelar_pago	POST
ms-compras	/procesar_compra	POST
ms-compras	/cancelar_compra	POST
ms-inventario	/actualizar_inventario	POST
orquestador	/saga	POST
api-gateway	/saga	POST
 
# Tecnologías utilizadas

Python 3.11

Flask

Docker

Docker Compose

PowerShell / Bash