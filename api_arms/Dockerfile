FROM python:3.12.2-bullseye
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
RUN python manage.py migrate
RUN python manage.py test
CMD python manage.py runserver
