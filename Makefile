.PHONY: install develop test precommit autoupdate clean black build pypi

env:
ifeq (, $(shell which pipx))
	python3 -m pip install --user pipx
	python3 -m pipx ensurepath
endif
ifeq (, $(shell which pre-commit))
	pipx install pre-commit
endif
	pre-commit install
ifeq (, $(shell which poetry))
	pipx install poetry
endif
ifeq (, $(shell which black))
	pipx install black
endif

install: env
	PIP_USER=false poetry install --no-dev

develop: env
	PIP_USER=false poetry install

test:
	poetry run pytest --cov=skadvance --cov-report=term-missing:skip-covered --cov-report=xml:coverage.xml

black:
	black .

precommit:
	pre-commit run

autoupdate:
	pre-commit autoupdate --freeze

clean:
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf .coverage*

build: clean
	poetry build
