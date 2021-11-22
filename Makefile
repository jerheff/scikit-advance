.PHONY: install develop test precommit autoupdate clean black build pypi

env:
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
	poetry install --no-dev

develop: env
	poetry install

test:
	poetry run pytest --disable-warnings --cov=skadvance

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

test-publish: build
	twine upload -r testpypi dist/*

publish: build
	twine upload dist/*
