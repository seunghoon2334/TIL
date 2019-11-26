git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
python -V
pip install --upgrade pip
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
flask db init

flask db upgrade
flask db migrate
flask db upgrade
sqlite3 db_flask.sqlite3 
flask shell
python
sqlite db_flask.sqlite3
sqlite3 db_flask.sqlite3
flask db init
flask db migrate
flask db upgrade
python
