import os
import json


def read_vault_json() -> dict:
    '''Получаем БД из json'''
    url_vault = os.getenv('URL_VAULT')
    with open(file=url_vault, encoding='utf-8') as file:
        vault = json.load(file)
    return vault


def is_user_id_in_vault(user_id: str) -> bool:
    '''Провка есть ли пользователь в БД'''
    vault = read_vault_json()
    return user_id in vault


def is_progress_in_user_id(user_id: str, progress_name: str) -> bool:
    '''Проверка есть ли прогрегресс у пользователя
    
    Raises:
        ValueError: если пользователь не найден
    '''
    vault = read_vault_json()
    if is_user_id_in_vault(user_id=user_id):
        return progress_name in vault[user_id]
    else:
        raise ValueError(f'user id, {user_id}, not found')


def write_vault_json(vault: dict) -> None:
    '''Записать данные в БД json'''
    url_vault = os.getenv('URL_VAULT')
    with open(file=url_vault, encoding='UTF-8', mode='w') as file:
        json.dump(vault, file, indent=4, ensure_ascii=False)


def add_progress_user(user_id: str, progress_name: str) -> None:
    '''Создание записи о новом пользователе и прогрессе
    
    Raises:
        ValueError: если у пользователя уже есть этот прогресс
    '''
    vault = read_vault_json()
    
    if user_id not in vault:
        vault[user_id] = {progress_name: []}
    elif progress_name not in vault[user_id]:
        vault[user_id][progress_name] = []
    else:
        raise ValueError(f'the user, {user_id}, already has progress, {progress_name}')
    
    write_vault_json(vault)

