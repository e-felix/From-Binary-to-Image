# From Binary to Image

Desktop application allowing one to create image files from a bytea data stored in a Postgresql database.

[WORK IN PROGRESS]

## Prerequisite

We use the package `psycopg2` which requires the following dependencies:
- A C compiler
- The Python header files (`python-dev` or `python3-dev`)
- The libpq header files (`libpq-dev`)
- The pg_config program (`libpq-dev` should be enough)

For more informations: [psycopg installation](https://www.psycopg.org/docs/install.html)

## Create the ENV file

The `.env` file must have the following environment variables:
```sh
DATABASE_NAME=db
DATABASE_HOST=host
DATABASE_PORT=5432
DATABASE_USER=user
DATABASE_PASSWORD=password
```

## Virtual Environment Setup

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the script

```sh
python3 main.py
```

## Licences

 * psycopg2 - GNU Library or Lesser General Public License (LGPL), Zope Public License (LGPL with exceptions) - ([https://pypi.org/project/psycopg2/](https://pypi.org/project/psycopg2/))
 * python-dotenv - BSD License ([https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/))
  * Pillow - PIL Software License ([https://raw.githubusercontent.com/python-pillow/Pillow/master/LICENSE](https://raw.githubusercontent.com/python-pillow/Pillow/master/LICENSE))
