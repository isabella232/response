release_test:
	rm -rf build dist
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*




.PHONY: release_test
