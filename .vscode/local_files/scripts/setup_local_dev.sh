pyenv local 3.10.0
sudo apt install graphviz-dev -y
pip install -r requirements_dev.txt

ln -f .vscode/local_files/git/info/exclude.sh .git/info/exclude