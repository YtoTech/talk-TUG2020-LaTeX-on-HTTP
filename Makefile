install:
	pipenv install --dev

run-demo:
	pipenv run python demo.py

format-code:
	pipenv run black .