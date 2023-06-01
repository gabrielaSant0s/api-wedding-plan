## Django Rest Framework

1 - Crie um projeto

``` django-admin startproject <project> ```

2 - Crie um app

``` python manage.py startapp <app> ```

3 - Configure o django rest framework no project/settings.py

```
INSTALLED_APPS = [
    # ...
    'rest_framework',
    # ...
]
```

4 - Crie um View no arquivo app/views.py

5 - Crie uma url no arquivo app/urls.py

6 - No diretório /project crie um requiriments.txt com as dependencias do projeto

- Se você estiver dentro de uma venv pode utilizar o comando 

``` pip freeze > requirements.txt ```

- Se não estiver dentro de uma venv adicione 

```
Django==3.2.4
djangorestframework==3.12.4
```

7 - Dentro do diretório project construa a imagem
``` docker build -t app . ```

e para subir a imagem pode utilizar o comando 

``` docker run -p 8000:8000 app```

