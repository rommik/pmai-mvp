install:upgrade
	pip install -r requirements.txt
upgrade:
	pip install --upgrade pip
run: install
	python app.py