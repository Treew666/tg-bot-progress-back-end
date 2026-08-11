# tg-bot-progress-back-end
<h2>Проект бэкенд части для бота по отслеживанию прогресса на питоне.</h2>
<div align="center">
<h3>Использовались технологии</h3>
  <div>
    <!--Python-->
    <img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=FFD700" alt="Python" />
    <!--UV-->
    <img src="https://img.shields.io/badge/uv-9ACD32?style=for-the-badge&logo=uv&logoColor=white" alt="uv" />
    <!--FastAPI-->
    <img src="https://img.shields.io/badge/FASTAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
    <!--Pytest-->
    <img src="https://img.shields.io/badge/Pytest-0A9EC0?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
    <!--Docker-->
    <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
    <!--Git-Actions-->
    <img src="https://img.shields.io/badge/GITHUB_Actions-red?style=for-the-badge&logo=github&logoColor=white" alt="GitHubActions" />
  </div>
</div>
<hr>
<div>
<b>Бэкенд часть имеет следующие ручки(endpoins):</b> <br>
<ul>
<li> POST /progress/{user_id} тело запроса {progress_name: string} </li>
<li> DELETE /progress/{user_id}/{progress_name} </li>
<li> POST /progress/ready/{user_id} тело запроса {progress_name: string}</li>
<li> DELETE /progress/ready/{user_id}/{progress} </li>
<li> GET /remind/{user_id|"all"} </li>
<li> GET /progress/{user_id}/{progress} </li>
<li> GET /progress/{user_id} </li>
</ul>
</div>

## Запуск через Docker
### Через GitHub Packages
`docker pull ghcr.io/Treew666/tg-bot-progress-back-end`
### Через .tar из релиза
1) Скачиваем архив .tar
2) Запускаем `docker load -i tg-bot-progress.tar`

## Запуск проекта
### Копируем проект
**Через Git**
1) Открываем консоль/терминал и заходим в нем в папку, куда хотите разместить проект
2) Если у вас установлен только *Git* то прописываем `git clone https://github.com/Treew666/tg-bot-progress-back-end.git` или если у вас установлен *GitHubCLI* то `gh repo clone Treew666/tg-bot-progress-back-end`

**Через архив**
1) Скачиваем архив
2) Разархивируем в нужном месте

### Перед запуском
1) Нужно создать файл с расширением json, который будет БД \
Рекомендую создать папку `vaults` в папке проекта и в ней создать файл `vault.json`
2) Нужно создать файл `.env` в папке проекта и прописать путь к файлу БД в константе \
Например создали БД по рекомендации то нужно прописать `URL_VAULT=./vaults/vault.json`

Структура примера выглядит так
project\
├...\
├.env\
└vaults\
\  └vault.json

### Запуск
`uvicorn main:app --reload`
- `main` – имя файла `main.py`
- `app` – имя переменной `FastAPI()` внутри файла
- `--reload` – автоперезагрузка при изменении кода (только для разработки, для продакшена без этого флага)

## После запуска:
- API работает на http://127.0.0.1:8000
- Автодокументация на http://127.0.0.1:8000/docs или http://127.0.0.1:8000/redoc

## Перед коммитом лучше
### Запускаем линтер
`uv run ruff check .` \
Для исправления некоторых ошибок, которые можно исправть автоматически используем \
`uv run ruff check --fix .` \
Проверяем еще раз и вносим изменения, которые не исправляются автоматически

### Запускаем проверку форматирования
`uv run ruff format --check .` \
Смотрим, что не соответсвует правилам форматирования \
`uv run ruff format --diff .` \
Если предлагаемые изменения подходят то используем \
`uv run ruff format .` \
Проверяем еще раз и вносим изменения, которые не исправляются автоматически

### Запускаем статический анализатор типов
`uv run mypy .` \
Вносим изменения и проверяем еще раз

### Запускаем тесты
`uv run pytest -v` \
Если тест полностью не пройден, то исправляем и проверяем еще раз

