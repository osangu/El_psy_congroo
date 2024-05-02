FROM python:3.9

WORKDIR hello-world-server

COPY ./app ./app
COPY ./run.py ./run.py
COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD ["uvicorn", "run:app", "--host", "0.0.0.0"]
