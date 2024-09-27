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

    return response.status_code, result


def check_app() -> int:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-SGTN-ANDROID",
    }

    response = requests.head(
        'https://kis-marm.mos.ru/api/checkServer',
        headers=headers,
        timeout=35,
    )

    return response.status_code


def actual_version(token: str) -> int:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-SGTN-ANDROID",
        "X-API-KEY": token,
        "X-APP-VERSION": "999999",
    }

    response = requests.get(
        'https://kis-marm.mos.ru/api/updates/check',
        headers=headers,
        timeout=35,
    )

    return response.status_code


def old_version(token: str) -> dict:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-SGTN-ANDROID",
        "X-API-KEY": token,
        "X-APP-VERSION": "1",
    }

    response = requests.get(
        'https://kis-marm.mos.ru/api/updates/check',
        headers=headers,
        timeout=35,
    )
    result = json.loads(response.text)

    return result


def get_apk_file() -> int:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-SGTN-ANDROID",
    }

    response = requests.get(
        'https://kis-marm.mos.ru/api/updates/apk',
        headers=headers,
        timeout=35,
    )

    return response.status_code


def get_version_dk() -> dict:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-SGTN-ANDROID",
    }

    response = requests.get(
        'https://kis-marm.mos.ru/api/sgtn/getDiagnosticMap/version',
        headers=headers,
        timeout=35,
    )
    result = json.loads(response.text)

    return result


def get_json_file_dk() -> dict:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-SGTN-ANDROID",
    }

    response = requests.get(
        'https://kis-marm.mos.ru/api/sgtn/getDiagnosticMap',
        headers=headers,
        timeout=35,
    )
    result = json.loads(response.text)

    return result


def check_file(token: str) -> int:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-ADMIN-WEB",
        "X-API-KEY": token,
        "X-APP-VERSION": "999999",
    }

    response = requests.get(
        'https://kis-marm.mos.ru/api/files/4cc9f14f-4442-4f0e-85bc-276f6e326c21',
        headers=headers,
        timeout=35,
    )

    return response.status_code


def delete_file(token: str) -> int:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-ADMIN-WEB",
        "X-API-KEY": token,
        "X-APP-VERSION": "999999",
    }

    response = requests.delete(
        'https://kis-marm.mos.ru/api/files/4cc9f14f-4442-4f0e-85bc-276f6e326c21',
        headers=headers,
        timeout=35,
    )

    return response.status_code


def download_file(token: str) -> dict:
    headers = {
        "Content-Type": "application/json",
        "X-APP": "MARM-ADMIN-WEB",
        "X-API-KEY": token,
        "X-APP-VERSION": "999999",
    }

    data = {"extension": "jpg", "location": {"longitude": "55.55", "latitude": 37.4354}, "length": 1861}

    response = requests.post(
        'https://kis-marm.mos.ru/api/files/4cc9f14f-4442-4f0e-85bc-276f6e326c21/meta',
        headers=headers,
        timeout=35,
        json=data,
    )
    result = json.loads(response.text)

    return result


def transfer_file(token: str) -> Tuple[int, Any]:
    headers = {
        "Content-Type": "application/octet-stream",
        "X-APP": "MARM-ADMIN-WEB",
        "X-API-KEY": token,
        "X-APP-VERSION": "999999",
        "X-CONTENT-TYPE": "base64' -d '/9j/4AAQSkZJRgABAQAAAQABAAD"
        "/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABWAFYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAoorP1nWbXQ9Pa7um46Ig6u3oKaTbshN21ZoUVi+G/ECeIrCS5WBoGjfYyk5HTPBrYDoSQGGR1GaGmnZgndXQ6iuS8S+Mn8P6vBafY/MhZA7uWwcEkYH5V0mn39",
    }

    response = requests.post(
        'https://kis-marm.mos.ru/api/files/4cc9f14f-4442-4f0e-85bc-276f6e326c21',
        headers=headers,
        timeout=35,
    )
    result = json.loads(response.text)

    return response.status_code, result


def get_file(token: str) -> int:
    headers = {"X-APP": "MARM-ADMIN-WEB", "X-API-KEY": token, "X-APP-VERSION": "999999"}

    response = requests.get(
        'https://kis-marm.mos.ru/api/files/4cc9f14f-4442-4f0e-85bc-276f6e326c21',
        headers=headers,
        timeout=35,
    )

    return response.status_code


def deleted_files(token: str) -> int:
    headers = {"X-APP": "MARM-ADMIN-WEB", "X-API-KEY": token, "X-APP-VERSION": "999999"}

    response = requests.delete(
        'https://kis-marm.mos.ru/api/files/4cc9f14f-4442-4f0e-85bc-276f6e326c21',
        headers=headers,
        timeout=35,
    )

    return response.status_code


def get_print_pattern(token: str) -> dict:
    headers = {"X-APP": "MARM-ADMIN-WEB", "X-API-KEY": token, "X-APP-VERSION": "999999"}

    response = requests.get(
        'https://kis-marm.mos.ru/api/templates',
        headers=headers,
        timeout=35,
    )
    result = json.loads(response.text)
    print(result)

    return result


def get_print_pattern_docx(token: str) -> int:
    headers = {"X-APP": "MARM-ADMIN-WEB", "X-API-KEY": token, "X-APP-VERSION": "999999"}

    data = {"format": "docx", "params": {}}

    response = requests.post(
        'https://kis-marm.mos.ru/api/templates/name/%D0%A1%D0%93%D0%A2%D0%9D.%20%D0%94%D0%B8%D0%B0%D0%B3%D0%BD%D0%BE'
        '%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BA%D0%B0%D1%80%D1%82%D0%B0/print',
        headers=headers,
        json=data,
        timeout=35,
    )

    return response.status_code
