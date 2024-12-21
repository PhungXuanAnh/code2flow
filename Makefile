build:
	rm -rf dist
	python3 setup.py sdist

test:
	pytest -n=4 --cov-report=html --cov-report=term --cov=code2flow -x

clean:
	rm -rf build
	rm -rf dist
	rm -f out.*
	rm -rf *.egg-info
	rm -rf htmlcov

rebase:
	git remote add upstream https://github.com/scottrogowski/code2flow.git ||:
	git checkout master
	git clean -fd
	git pull upstream master
	git push origin master
	git checkout -
	git rebase origin/master