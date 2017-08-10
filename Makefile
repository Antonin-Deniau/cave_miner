.PHONY: install publish
install:
	pip install -e $(pwd)/
publish:
	python setup.py sdist bdist_wininst upload
	rm -fr build dist .egg requests.egg-info