import json
from typing import Any, Tuple
import requests


def auth(login: str, password: str) -> Tuple[int, Any]:
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(
        'https://kis-marm.mos.ru/api/login',
        headers=headers,
        data={'username': login, 'password': password},
        timeout=35,
    )

    return response.status_code, json.loads(response.text)['token']
