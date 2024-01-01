
```
📂flask-backed
|
|---📂server                     #primary server modules
|    |----__init__.py            #server module main initial
|    |----server_config.py       #server module main configuration
|    |----📂models
|    |     |----__init__.py  
|    |  
|    |----📂routes
|    |
|    |   
|    |----📂services
|
|---📂flask-backend-env          #venv
|---.gitignore                   #gitignore file
|---app.py                       # import app,import blue print and blue print register
|---requirements.txt
|---wsgi.py                      #wsgi for production environment for nginx proxy pass deploy
```