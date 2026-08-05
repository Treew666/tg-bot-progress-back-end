import datetime
import json
import os

import pytest

TEST_VAULT = {
    "1101": {"progress1": ["20.06.2020", "21.06.2020"], "progress2": [datetime.date.today().strftime("%d.%m.%Y")]},
    "1102": {"progress1": []},
}


@pytest.fixture(autouse=True)
def request_add_progress(tmp_path):
    """Создаем тестувую БД и загружаем в environ путь к этой БД, в переменную URL_VAULT"""
    vault_path = tmp_path / "test_vault.json"
    vault_path.write_text(json.dumps(TEST_VAULT), encoding="utf-8")
    os.environ["URL_VAULT"] = str(vault_path)
    yield
