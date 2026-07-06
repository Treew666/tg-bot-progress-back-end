import os
import json
import jsonschema

from dotenv import load_dotenv


load_dotenv()


def read_vault_json() -> dict:
    '''Получаем БД из json'''
    url_vault = os.getenv('URL_VAULT')
    with open(file=url_vault, encoding='utf-8') as file:
        vault = json.load(file)
    return vault


def is_user_id_in_vault(user_id: str) -> bool:
    '''Провка есть ли пользователь в БД'''
    vault = read_vault_json()
    list_user_id = [user_id for user_id in vault.keys()]
    if user_id in list_user_id:
        return True
    else:
        return False

def is_progress_in_user_id(user_id: str, progress: str) -> bool:
    '''Проверка есть ли прогрегресс у пользователя'''
    vault = read_vault_json()
    if is_user_id_in_vault(user_id=user_id):
        list_progress_user = [progress for progress in vault[user_id]]
        if progress in list_progress_user:
            return True
        else:
            return False
    else:
        raise ValueError(f'user id, {user_id}, not found')
    
    

if __name__ == '__main__':
    # print(read_vault_json())
    print(is_progress_in_user_id('1101', 'progress2'))
