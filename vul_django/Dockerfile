FROM python:3.8-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV DockerHOME=/home/vul_django
RUN mkdir $DockerHOME
WORKDIR $DockerHOME

COPY . $DockerHOME
RUN pip install --upgrade pip 
RUN apt-get update && \
    apt-get install -y dnsutils
RUN pip install -r requirements.txt

EXPOSE 8000
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
