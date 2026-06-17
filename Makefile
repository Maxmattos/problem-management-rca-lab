.PHONY: data notebooks test lint format verify clean help

help:                 ## lista os alvos
	@grep -E '^[a-z]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  %-12s %s\n", $$1, $$2}'

data:                 ## gera o CSV determinístico
	python data/gerar_ocorrencias.py

notebooks:            ## reexecuta e atualiza os PNGs comitados (uso local)
	jupyter nbconvert --to notebook --execute --inplace notebooks/*.ipynb

lint:                 ## ruff lint + checagem de formatação
	ruff check .
	ruff format --check .

format:               ## aplica formatação
	ruff format .

test:                 ## invariantes + execução de notebooks + anonimato + sem-gabarito
	pytest

verify: data lint test ## pipeline completo (espelha o CI)
	@echo "verify OK"

clean:
	rm -rf .pytest_cache **/__pycache__ **/.ipynb_checkpoints
