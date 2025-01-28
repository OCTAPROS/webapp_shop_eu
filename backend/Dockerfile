FROM python:3.12


WORKDIR /src
COPY ./src /src

COPY ./requirements.txt /src_pre/requirements.txt

RUN pip install --no-cache-dir -r /src_pre/requirements.txt



CMD ["fastapi", "run", "/src/main.py", "--proxy-headers", "--port", "8001", "--reload"]