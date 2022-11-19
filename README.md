# Dockerised Django

This is a Dockerised Django Project template

## Getting started

1. Clone this repo, cd into it, and copy the `.env` file:

```sh
git clone https://github.com/user/repo
cd repo
cp .env.example .env
```

2. Start up the Docker environment:

```
docker compose up -f docker-compose.dev.yml -d
```

3. Log into admin console at http://localhost:8000/admin as `root`/`root`.

## Getting things going

### Initialise an app

1. Identify the container ID and attach a bash shell for the container:

> Use `docker ps` to display a list of containers and their relevant IDs.
```
docker exec -it <container-d> /bin/bash
```

2. Initialise the app:

```
python manage.py startapp <app_name>
```
This will register a new app with Django, and create <app_name> folder for your app files.

### Modify or make views

6. Modify existing views or create brand new ones. You can do this by editing the commented files shown below:

```
django
- <app>
| - migrations
| - __init__.py
| - admin.py
| - apps.py
| - models.py
| - tests.py
| - urls.py         # This file maps URLs to views. It will need to be created if you have not already made one.
| - views.py        # This file lists views relevant to the app
- myproject
| - __init__.py
| - asgi.py
| - settings.py
| - urls.py         # This file maps urls to the app         
| - wsgi.py

```
> If you don't have an existing view, you can create a simple HttpRequest view [using the Django tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/#write-your-first-view). Help is also available at this resource.

You should now get a simple `Hello, World!` message when you navigate to the url you just created (usually `http://localhost:$APP_PORT/<app-name>`) if you followed the Django tutorial precisely.

### Building a model, activating a model, and making migrations

[Creating Models](https://docs.djangoproject.com/en/4.1/intro/tutorial02/#creating-models)

## Notes

By default there is no `docker-compose.yml`, so `docker compose up` won't work without specifying one of the other files.

`docker-compose.dev.yml` is designed for use during development. You probably also want to uncomment the `DEBUG` line in the `.env` file in this case.

`docker-compose.prod.yml` is designed for production.

For convenience, either of these files could be copied to `docker-compose.yml` so you don't need to specify the file with `docker compose -f file.yml`.
