FROM python:3.8.0-buster

# Make a directory for our application
WORKDIR /application


COPY project.py .
RUN pip install -r project.py


COPY /app .

CMD ["python", "project.py"]
