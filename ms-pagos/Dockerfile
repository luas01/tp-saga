# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements.txt y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del microservicio
COPY . .

# Exponer el puerto (cambia según el microservicio)
# Ejemplo: ms-catalogo usa 5001
EXPOSE 5002

# Comando para ejecutar el servicio
CMD ["python", "app.py"]
