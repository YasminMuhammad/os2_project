FROM python:3.8.0-buster

# Make a directory for our application
WORKDIR D:\OsProject

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .

CMD ["python", "project.py"]