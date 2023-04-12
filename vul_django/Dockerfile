FROM python:3.8-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
ENV DockerHOME=/home/vul_django
RUN mkdir $DockerHOME
WORKDIR $DockerHOME

COPY . $DockerHOME
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver
RUN echo "[+] Now visit http://localhost to start learning. "
RUN echo "Happy Hacking. "