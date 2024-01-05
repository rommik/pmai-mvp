install:
	poetry install --no-root

run: install
	poetry run python app.py
prod:
	poetry run python app.py
dev: install
	poetry run gradio cc dev app.py