install:
	poetry install 

run: install
	poetry run python app.py

dev: install
	poetry run gradio cc dev app.py