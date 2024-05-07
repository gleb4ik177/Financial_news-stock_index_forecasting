# Stock indexes prediction using news
## About
The goal of this project is to predict the IMOEX and SPBIRUS2 indexes based on the time series and news from finam.ru analisys.
### Project architecture
<p align="center">
  <img width="600" height="450" src="https://sun9-15.userapi.com/impg/8bmRZ3ZBF-z2GakolAZ47gjrgXqYdCJrxXw6pg/OAxO30BUNRA.jpg?size=1451x1105&quality=96&sign=3978262b45c79a9b15f9603c14b3560a&type=album">
</p>

## Backend
Backend is implemented using FastAPI

### Деплой бэкенда

#### Development

Для запуска приложения в среде разработки доступны варианты запуска напрямую через `python` и
через `docker-compose`. Оба варианта используют для конфигурации переменные окружения, которые
описаны в файле `app/settings/settings.py`. В данных режимах запуска доступно обновление кода приложения
на лету, без перезапуска (кроме случаев добавления новых зависимостей).

##### Python Runner

```bash
python -m fastapi_service
```

##### Docker runner

Перед запуском docker-compose необходимо :

```bash
make build
```

Команда создаст .env из .env.example и сделает "билд" контейнеров.

```bash
make run_build
```

```bash
docker compose up -d
```


#### Разработка

"Линтинг" проекта :

```bash
make lint 
```

#### Зависимости

Управлением зависимостями занимается утилита `poetry`. \
Перечень зависимостей находится в файле `pyproject.toml`. \
Инструкция по настройке poetry-окружения для
pyCharm [здесь](https://www.jetbrains.com/help/pycharm/poetry.html).

Для добавления зависимости достаточно написать `poetry add requests`, утилита сама подберёт версию,
не конфликтующую с текущими зависимостями. \
Зависимости с точными версиями фиксируются в файл `poetry.lock`. \
Для получения дерева зависимостей можно воспользоваться командой `poetry show --tree`. Остальные
команды доступны в официальной документации к утилите.

### Deploy S3

1. Create bucket
1. Create service account with role storage.admin
1. Create static key. Create file ~/.aws/credentials with the following content:
```[default]
  aws_access_key_id = <access-key-id>
  aws_secret_access_key = <secret-access-key>
```
Then create file ~/.aws/config with the following content:
```[default]
  region=ru-central1
```
### Важно!

Модели должны быть загружены на S3.
Путь до модели в S3 указывается в переменных окружения описанных в `app/settings/settings.py`.


