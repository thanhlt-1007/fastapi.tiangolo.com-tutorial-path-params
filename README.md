# fastapi.tiangolo.com-tutorial-path-params

- Path Parameters

- Reference: https://fastapi.tiangolo.com/tutorial/path-params/

## pyenv

```sh
pyenv install 3.13.0
pyenv global 3.13.0
```

## venv

```sh
python -m venv .venv
source .venv/bin/activate
```

## pip

```sh
python -m pip install -r requirements.txt
```

## fastapi

```sh
fastapi dev main.py
```

## cURL

### Get item:

```sh
curl --location 'http://127.0.0.1:8000/items/1'
```

### Get user:

```sh
curl --location 'http://127.0.0.1:8000/users/1'
```

### Get current user:

```sh
curl --location 'http://127.0.0.1:8000/users/me'
```

## API doc

- [Swagger](http://127.0.0.1:8000/docs)

- [Redoc](http://127.0.0.1:8000/redoc)
