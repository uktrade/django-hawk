SHELL := /bin/bash

# Colour coding for output
COLOUR_NONE=\033[0m
COLOUR_GREEN=\033[32;01m
COLOUR_YELLOW=\033[33;01m
COLOUR_RED='\033[0;31m'

# Help output
.PHONY: help test
help:
	@echo -e "$(COLOUR_YELLOW)make cleanup-code$(COLOUR_NONE) : Run flake8, black, isort, mypy"

cleanup-code:
	flake8 .
	black .
	isort .
	mypy .

tests:
	tox

build-test:
	pip install --upgrade build twine
	python -m build
	twine upload --repository testpypi dist/*

build:
	pip install --upgrade build twine
	python -m build
	twine upload dist/*
