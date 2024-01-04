force:
	pip install --force-reinstall -r requirements.txt
install:upgrade
	pip install -r requirements.txt
upgrade:
	pip install --upgrade pip
run: install
	python app.py

dev: install
	gradio cc dev app.py