python-V
python -V
python3 -V
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
python -V
git config global --user.name seunghoon2334
pyenv virtualenv django-venv
git clone https://github.com/pyenv/pyenv-virtualenv.git
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
git config global --user.name seunghoon2334
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
exec "$SHELL"
mkdir first_workshop
cd first_workshop
django-admin first_workshop
django-admin startproject first_workshop
python manage.py reunserver 0.0.0.0:8080
~/workspace/first_workshop $python manage.py runserver 0.0.0.0:8080
ls
python manage.py runserver 00.0.0:8080
django-admin startproject first_workshop2
cd first_workshop2/
ls
python manage.py startapp home
clear
python manage.py runserver 0.0.0.0:8080
cd 장고CRUD
python manage.py runserver 0.0.0.0:8080
git add .
git commit -m '05_CRUD_CREATE'
python manage.py runserver 0.0.0.0:8080
git add .
git commit -m '06_CRUD_READ'
python manage.py runserver 0.0.0.0:8080
git add .
git commit -m '07_CRUD_DELETE'
python manage.py runserver 0.0.0.0:8080
git add .
git commit -m '08_CRUD_EDIT'
git push origin master
python manage.py startapp jobs
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
pip install faker
python
python manage.py runserver 0.0.0.0:8080
vi ~/.bashrc
cd django-intro
django-admin startproject workshop19
cd workshop19
python manage.py startapp student
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
python manage.py makemigrations
cd django_recrud
python manage.py shell_plus
cd PROJECT7
python manage.py startapp movies
django-admin startproject project7
python manage.py startapp movies
cd relations
cd relationship
python manage.py shell_plus
