#La primera instruccion es definir que imagen queremos usar como base de nuestro contenedor
FROM python:3.10.13-alpine3.18

ENV PYTHONUNBUFFERED=1

#Permite a docker almacenar en cache las dependencias instaladas entre compilaciones
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 

#Monta el codigo de la aplicación en la imagen
COPY . /code
WORKDIR /code

EXPOSE 8000

#Corre el servidor de produccion
CMD ["python","ParticipacionCiudadana/app.py","runserver","0.0.0.0:8000"]
