import json
import os
from datetime import date
from typing import NewType

UrlValutString = NewType("UrlValutString", str)


def get_url_vault() -> UrlValutString:
    """Получения ссылки на БД.

    Returns:
        UrlValutString: строковоа ссылка на json БД.

    Raises:
        ValueError: ссылка пустая.
        ValueError: ссылка ведет на не существующий файл.
    """
    url_vault = os.getenv("URL_VAULT")
    if url_vault is None:
        raise ValueError("The url vault is None.")
    try:
        with open(file=url_vault, encoding="utf-8"):
            pass
    except (FileNotFoundError, OSError) as error:
        raise ValueError(f"The value not found by url, {str(url_vault)}.") from error
    return UrlValutString(url_vault)


Vault = dict[str, dict[str, list[str]]]


def read_vault_json() -> Vault:
    """Получаем БД из json.

    Returns:
        Vault: словарь вида {"user_id": {"progress_name": ["DD.MM.YYYY"]}}.

    Raises:
        ValueError: url БД пустой или не правильный.
    """
    url_vault = get_url_vault()  # raise ValueError
    with open(file=url_vault, encoding="utf-8") as file:
        vault = json.load(file)
    return vault


def write_vault_json(vault: dict) -> None:
    """Записать данные в БД json.

    Args:
        vault: словарь вида {"user_id": {"progress_name": ["DD.MM.YYYY"]}}.

    Raises:
        ValueError: url БД пустой или не правильный.
    """
    url_vault = get_url_vault()  # raise ValueError
    with open(file=url_vault, encoding="UTF-8", mode="w") as file:
        json.dump(vault, file, indent=4, ensure_ascii=False)


def is_user_id_in_vault(user_id: str) -> bool:
    """Провка есть ли пользователь в БД.

    Args:
        user_id: строковое значение id пользователя из БД.

    Returns:
        bool: user_id in vault.

    Raises:
        ValueError: url БД пустой или не правильный.
    """
    vault = read_vault_json()  # raise ValueError
    return user_id in vault


def is_progress_in_user_id(user_id: str, progress_name: str) -> bool:
    """Проверка есть ли прогрегресс у пользователя.

    Args:
        user_id: строковое значение id пользователя.
        progress_name: строковое значение имени прогресса.

    Returns:
        bool: progress_name in vault[user_id].

    Raises:
        ValueError: url БД пустой или не правильный.
        ValueError: пользователь не найден.
    """
    vault = read_vault_json()  # raise ValueError
    if is_user_id_in_vault(user_id=user_id):
        return progress_name in vault[user_id]
    else:
        raise ValueError(f"User id, {user_id}, not found.")


def add_progress_user(user_id: str, progress_name: str) -> None:
    """Создание записи о новом пользователе и прогрессе.

    Args:
        user_id: строковое значение id пользователя.
        progress_name: строковое значение имени прогресса.

    Raises:
        ValueError: url БД пустой или не правильный.
        ValueError: пользователя уже есть этот прогресс.
    """
    vault = read_vault_json()  # raise ValueError

    if user_id not in vault:
        vault[user_id] = {progress_name: []}
    elif progress_name not in vault[user_id]:
        vault[user_id][progress_name] = []
    else:
        raise ValueError(f"The user, {user_id}, already has progress, {progress_name}.")

    write_vault_json(vault)  # raise ValueError


def delete_progress_user(user_id: str, progress_name: str) -> None:
    """Удаление прогресса у пользователя.

    Args:
        user_id: строковое значение id пользователя.
        progress_name: строковое значение имени прогресса.

    Raises:
        ValueError: url БД пустой или не правильный.
        ValueError: пользователь не найден.
        ValueError: прогресс не найден у пользователя.
    """
    vault = read_vault_json()  # raise ValueError

    if is_progress_in_user_id(user_id=user_id, progress_name=progress_name):  # raise ValueError
        del vault[user_id][progress_name]
        write_vault_json(vault=vault)  # raise ValueError
    else:
        raise ValueError(f"The progress, {progress_name}, not found for the user, {user_id}.")


DateString = NewType("DateString", str)


def add_ready_user_progress(user_id: str, progress_name: str) -> DateString:
    """Добавляем отметку (сегодняшнию дату) в список прогресса.

    Args:
        user_id: строковое значение id пользователя.
        progress_name: строковое значение имени прогресса.

    Returns:
        DateString: сегодняшняя дата в формате DD.MM.YYYY, которая была добавлена в список прогресса.

    Raises:
        ValueError: url БД пустой или не правильный.
        ValueError: пользователь не найден.
        ValueError: сегодяншяя дату уже добалена.
    """
    vault = read_vault_json()  # raise ValueError
    if user_id not in vault:
        raise ValueError(f"User id, {user_id}, not found.")
    if progress_name not in vault[user_id]:
        raise ValueError(f"The progress, {progress_name}, not found for the user, {user_id}.")

    today = date.today().strftime("%d.%m.%Y")
    if today in vault[user_id][progress_name]:
        raise ValueError(
            f"Today's progress, {progress_name}, is already marked for user, {user_id}."
        )

    vault[user_id][progress_name].append(today)
    write_vault_json(vault=vault)
    return DateString(today)
