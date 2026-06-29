import json
import jsonschema


def read_vault_json() -> dict:
    '''Получаем БД из json'''
    with open(file='./vaults/vault.json', encoding='utf-8') as file:
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
    
    

if __name__ == '__main__':
    pass
