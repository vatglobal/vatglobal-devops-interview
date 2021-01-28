
## Recommendations
### Use poetry 

https://python-poetry.org/docs/

Once you have installed poetry you can run poetry install in the project dir

To enable poetry pyenv
```buildoutcfg
poetry shell
```

## Dependencies
    Python 3.6  >= (Preferaably 3.7/3.8)
    SQLITE3
    Poetry (We default to poetry, you can use pip if you like)
    Django
    Django-Rest
    Django-Q


## Project specifics
* Django Rest
* Basic auth
* Can use postman/insomnia to test rest api
* Has admin panel, user created during  migration
* Both openapi and redoc

## Recommendations
* Use tools like terraform, serverless, etc.
* Minikube for k8s
* Use AWS


## Tasks

1. Install dependencies

2. Get django to run

3. Check django rest docs

4. Check all dependencies correct and endpoints working

5. Make collectstatic work with s3

6. Make django-q work (python manage.py qcluster)
    * You can enqueue a task with
    ```buildoutcfg
   curl --request POST \
          --url http://127.0.0.1:8000/event/djangoq \
          --header 'Authorization: Basic <password base64>' \
          --header 'Content-Type: application/json' \
          --data '{}'```

7. Add the following CI to the project.
    1.  Tox to run the rest of the automation
        1. Black formatting
        2. Flake8 lint checking
        3. Bandit static analysis
        4. Welcome to add any other online or cli based tools
    2. Deal with any issue from automation. ex. black, bandit, etc.

8. Deployment (choose one)
    Use endpoint /health to check that server is up
* Either deploy api and worker/queue system in k8s with postgres container

* or either deploy API to lambda with  RDS (postgres) and ec2 worker/queue system.

9. Upload to github/gitlab (perferabbly  private and invite the interviewer to the project).
    * worst case scenario zip the files up but please exclude the .venv/



## Any questions during
email -> christo.goosen@vatglobal.com

## Links with docs on the tech used
* https://www.djangoproject.com/
* https://www.django-rest-framework.org/
* https://www.postgresql.org/
* https://www.sqlite.org/index.html