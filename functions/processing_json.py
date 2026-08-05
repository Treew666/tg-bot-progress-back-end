import json
import os
from datetime import date
from typing import NewType


def read_vault_json() -> dict:
    """Получаем БД из json

    Raises:
        ValueError: если url БД не существует
    """
    url_vault = os.getenv("URL_VAULT")
    if url_vault is None:
        raise ValueError("The url vault is None")
    with open(file=url_vault, encoding="utf-8") as file:
        vault = json.load(file)
    return vault


def is_user_id_in_vault(user_id: str) -> bool:
    """Провка есть ли пользователь в БД

    Raises:
        ValueError: если url БД не существует
    """
    vault = read_vault_json()  # raise ValueError при пустой ссылки на БД
    return user_id in vault


def is_progress_in_user_id(user_id: str, progress_name: str) -> bool:
    """Проверка есть ли прогрегресс у пользователя

    Raises:
        ValueError: если пользователь не найден
        ValueError: если url БД не существует
    """
    vault = read_vault_json()  # raise ValueError при пустой ссылки на БД
    if is_user_id_in_vault(user_id=user_id):
        return progress_name in vault[user_id]
    else:
        raise ValueError(f"user id, {user_id}, not found")


def write_vault_json(vault: dict) -> None:
    """Записать данные в БД json

    Raises:
        ValueError: если url БД не существует
    """
    url_vault = os.getenv("URL_VAULT")
    if url_vault is None:
        raise ValueError("The url vault is None")
    with open(file=url_vault, encoding="UTF-8", mode="w") as file:
        json.dump(vault, file, indent=4, ensure_ascii=False)


def add_progress_user(user_id: str, progress_name: str) -> None:
    """Создание записи о новом пользователе и прогрессе

    Raises:
        ValueError: если у пользователя уже есть этот прогресс
        ValueError: если url БД не существует
        ValueError: если url БД не существует
    """
    vault = read_vault_json()  # raise ValueError при пустой ссылки на БД

    if user_id not in vault:
        vault[user_id] = {progress_name: []}
    elif progress_name not in vault[user_id]:
        vault[user_id][progress_name] = []
    else:
        raise ValueError(f"the user, {user_id}, already has progress, {progress_name}")

    write_vault_json(vault)  # raise ValueError при пустой ссылки на БД


def delete_progress_user(user_id: str, progress_name: str) -> None:
    """Удаление прогресса у пользователя

    Raises:
        ValueError: прогресс не найден у пользователя
        ValueError: пользователь не найден
        ValueError: если url БД не существует
        ValueError: если url БД не существует
    """
    vault = read_vault_json()  # raise ValueError при пустой ссылки на БД

    if is_progress_in_user_id(
        user_id=user_id, progress_name=progress_name
    ):  # raise ValueError при отсутствии пользователя
        del vault[user_id][progress_name]
        write_vault_json(vault=vault)  # raise ValueError при пустой ссылки на БД
    else:
        raise ValueError(f"the progress, {progress_name}, not found for the user, {user_id}")


DateString = NewType("DateString", str)


def add_ready_user_progress(user_id: str, progress_name: str) -> DateString:
    """Добавляем отметку (сегодняшнию дату) в список прогресса

    Args:
        user_id: id пользователя в БД.
        progress_name: название прогресса в БД.

    Returns:
        DateString: сегодняшняя дата в формате DD.MM.YYYY, которая была добавлена в список прогресса.

    Raises:
        ValueError: если url БД не существует.
        ValueError: пользователь не найден.
        ValueError: сегодяншяя дату уже добалена.
    """
    vault = read_vault_json()  # raise ValueError при пустой ссылки на БД
    if user_id not in vault:
        raise ValueError(f"user id, {user_id}, not found")
    if progress_name not in vault[user_id]:
        raise ValueError(f"the progress, {progress_name}, not found for the user, {user_id}")

    today = date.today().strftime("%d.%m.%Y")
    if today in vault[user_id][progress_name]:
        raise ValueError(
            f"Today's progress, {progress_name}, is already marked for user, {user_id}"
        )

    vault[user_id][progress_name].append(today)
    write_vault_json(vault=vault)
    return DateString(today)
