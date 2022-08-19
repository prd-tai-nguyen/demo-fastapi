FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY /src /app

EXPOSE 8000
CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]