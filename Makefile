.DEFAULT_GOAL := help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run: ## Run the Flask app in local (debug) mode
	flask --app app --debug run --host=0.0.0.0

dev-setup: ## Create a virtual environment for development
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

freeze: ## Freeze the dependencies
	pip freeze > requirements.txt
