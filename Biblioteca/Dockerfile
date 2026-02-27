FROM python:3.12-slim

#crear carpeta de trabajo
WORKDIR /app

#copia de requeriminetos 
COPY requirements.txt .

#intalalos
RUN pip install --no-cache-dir -r requirements.txt

#copiar el codigo del proyecto
COPY ./app_biblioteca ./app_biblioteca

#exponer el puerto 
EXPOSE 5002

#comandos para ejecutar FASTAPI
CMD ["uvicorn","app_biblioteca.main:app","--host","0.0.0.0","--port","5002","--reload"]