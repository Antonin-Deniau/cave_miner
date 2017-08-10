PIP=pip2.7
PYTHON=python
TWINE=twine

.PHONY: install publish

install:
	$(PIP) install -e .
publish:
	$(PIP) install twine wheel
	$(PYTHON) setup.py sdist bdist_wheel
	$(TWINE) upload dist/*
	rm -fr build dist .egg requests.egg-info