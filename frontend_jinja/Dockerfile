FROM python:3.12

WORKDIR /code
COPY ./code /code

COPY ./requirements.txt /code_pre/requirements.txt
RUN pip install --no-cache-dir -r /code_pre/requirements.txt


CMD ["fastapi", "run", "/code/main.py", "--proxy-headers", "--port", "80", "--reload"]