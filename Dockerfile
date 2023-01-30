# Usar la imagen base de Python 3.9
FROM python:3.9-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los requisitos y actualizar y instalar paquetes necesarios
COPY requirements.txt .
RUN apk update && \
    apk add build-base && \
    pip install -r requirements.txt

RUN apk update && apk add nginx
# Copiar todos los archivos y carpetas del proyecto
COPY . .
COPY nginx.conf /etc/nginx/nginx.conf

# Establecer la puerta de escucha en el contenedor
EXPOSE 5000

# Ejecutar comandos
CMD ["sh", "-c", "pip install -r requirements.txt && python app.py & nginx -g 'daemon off;'"]


