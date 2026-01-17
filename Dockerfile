FROM python:3.13.7

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "project_for_test/manage.py", "runserver", "0.0.0.0:8000"]
