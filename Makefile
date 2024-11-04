VENV := .venv

clean:
	if exist $(VENV) rd /s /q $(VENV)

build:
	if not exist $(VENV) python -m venv $(VENV)

setup:
	python -m pip install --upgrade pip
	pip install -r ./backend/requirements.txt
	pip install -r ./frontend_jinja/requirements.txt
