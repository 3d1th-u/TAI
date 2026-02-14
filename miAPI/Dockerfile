FROM python:3.12-slim

#crear carpeta de trabajo
WORKDIR /app

#copia de requeriminetos 
COPY requirements.txt .

#intalalos
RUN pip install --no-cache-dir -r requirements.txt

#copiar el codigo del proyecto
COPY ./app ./app

#exponer el puerto 
EXPOSE 5000

#comandos para ejecutar FASTAPI
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","5000","--reload"]