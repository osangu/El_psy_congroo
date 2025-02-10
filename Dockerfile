FROM python:3.11-slim AS builder

ENV PREFIX="/usr/local"

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt --prefix $PREFIX

FROM python:3.11-slim

ENV PREFIX="/usr/local"

WORKDIR /satchat-be

COPY --from=builder $PREFIX $PREFIX

COPY ./app ./app
COPY ./main.py ./main.py

# CMD ["python3", "main.py"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
