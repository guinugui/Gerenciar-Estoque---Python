
Como rodar o projeto?
    Clone esse repositório.
    Crie um virtualenv com Python 3.
    Ative o virtualenv.
    Instale as dependências.
    Rode as migrações.

git clone git@github.com:guinugui/Gerenciar-Estoque-Python.git
cd C:\Users\guilherme.siqueira\Desktop\python\Gerencia Estoque\Gerenciar-Estoque-Python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver