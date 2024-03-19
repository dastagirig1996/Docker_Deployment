FROM python:3.12.2-bullseye
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py test
CMD python3 manage.py runserver
