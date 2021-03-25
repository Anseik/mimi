FROM python:3.8
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
EXPOSE 8000
CMD ["gunicorn", "--bind", "0:8000", "backend.wsgi:application"]