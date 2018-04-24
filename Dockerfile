FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "./src/manage.py", "runserver", "0.0.0.0:8001"]
