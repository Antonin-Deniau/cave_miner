PIP=pip2.7
PYTHON=python

.PHONY: install publish

install:
	$(PIP) install -e .
publish:
	$(PYTHON) setup.py sdist upload
	rm -fr build dist .egg requests.egg-info