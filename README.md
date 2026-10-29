# Blog em Django (PMR3304, 2ª entrega de laboratório)

Aplicação CRUD de posts feita em Django para a segunda entrega de laboratório de PMR3304.

## Como rodar

```bash
python -m venv ./.virtualenvs/djangodev
./.virtualenvs/djangodev/Scripts/Activate.ps1      # Windows (Linux/macOS: source ./.virtualenvs/djangodev/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ para o blog e http://127.0.0.1:8000/admin/ para o administrador.

## Histórico da Parte 1

As três versões das views estão em commits separados:

1. views funcionais sem Django forms e sem validação;
2. views funcionais com `PostForm` (ModelForm);
3. views com `generic.ListView`, `DetailView`, `CreateView`, `UpdateView` e `DeleteView`.
