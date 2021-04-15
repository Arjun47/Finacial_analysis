# Staring a Django project

- inititate project [django-admin startproject <project_name> .](does not create another directory)
- add apps in the project [manage.py startapp <app_name>]
- add app in installed apps list in settings.py file
- add <rest_framwork> in intsalled app list for djangorestframework

    "dev": "webpack --mode development ./frontend/src/index.js --output-path ./frontend/static/frontend/main.js",
    "build": "webpack --mode production ./frontend/src/index.js --output-path ./frontend/static/frontend/main.js"