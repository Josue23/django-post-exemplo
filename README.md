## Como desenvolver?

* Clone o repositório.
* Crie um virtualenv com Python 3.5.
* Ative o virtualenv.
* Instale as dependências.
* Execute as migrações no banco de dados.

```console
git clone https://github.com/Josue23/django-post-exemplo.git
cd django-post-exemplo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
