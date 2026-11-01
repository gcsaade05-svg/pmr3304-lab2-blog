# Blog em Django (PMR3304, 2ª entrega de laboratório)

Blog com CRUD de posts, comentários e categorias, feito em Django para a segunda entrega de laboratório de PMR3304.

## Como rodar

```bash
python -m venv ./.virtualenvs/djangodev
./.virtualenvs/djangodev/Scripts/Activate.ps1      # Windows (Linux/macOS: source ./.virtualenvs/djangodev/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ para o blog e http://127.0.0.1:8000/admin/ para o administrador. Usuários (autores de comentários) e categorias são criados pelo administrador.

## Estrutura da entrega

1. **Parte 1:** CRUD de posts. As três versões das views estão em commits separados: views funcionais sem forms, views funcionais com `PostForm` e views com classes genéricas.
2. **Parte 2:** comentários, desenvolvidos no branch `comments`.
3. **Parte 3:** categorias, desenvolvidas no branch `categories`.

## Implantação no Render

- Build Command: `./build.sh`
- Start Command: `gunicorn blogsite.wsgi`
- Variáveis de ambiente: `DATABASE_URL` (Internal Database URL do PostgreSQL do Render), `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL` e `DJANGO_SUPERUSER_PASSWORD`.
- A versão do Python é definida no arquivo `.python-version`.
