FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:./impl

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "./impl", "main:app", "--reload"]