import json
from typing import Any, Tuple
import requests


def auth(login: str, password: str) -> Tuple[int, Any]:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-ADMIN-WEB",
        "X-APP-VERSION": "999999",
    }

    response = requests.post(
        'https://kis-marm.mos.ru/api/login',
        headers=headers,
        json={'login': login, 'password': password},
        timeout=35,
    )
    result = json.loads(response.text)

    return response.status_code, result['token']
