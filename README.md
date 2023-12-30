# noxtwitter

## Начало работы

Для успешного запуска необходимо создать файл `.env` в корне проекта.

Пример файла `.env`: [.env.example](docker/.env.example).

### Для ветки dev

При установке значения `DEV_MODE=True` для всех эндпоинтов добавляется префикс /dev/.

.env:
```
DEV_MODE=True
```

Запуск проекта:

```shell
docker-compose -f docker/docker-compose.yml up -d
```

Для разработки:

```shell
docker-compose -f docker/docker-compose.dev.yml up -d
```

Создание суперпользователя:

```shell
python manage.py createsuperuser
```

##  Тестирование

Автоматическое тестирование:

```shell
python manage.py tests noxtwitter
```

Для ручного тестирования воспользуйтесь коллекцией: [Bashurina_ex.postman_collection.json](Bashurina_ex.postman_collection.json)
