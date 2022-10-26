## Step 0
Make sure you have installed `Python 3`, and `python3` is on the environment variable `PATH`.

## Step 1
Create a virtual environment,

```sh
python3 -m venv env
```

and then activate it according to the [guide](https://docs.python.org/3/library/venv.html).

Install `psycopg2` driver, which allows connection to PostgreSQL:

```sh
pip3 install psycopg2
```

## Step 2
Run `python3 main.py`.