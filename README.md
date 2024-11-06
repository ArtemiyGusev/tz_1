# Generate Palindrome API Testing Project

## Описание проекта

Проект для тестирования API, которое генерирует строки-палиндромы или случайные строки на основе входного параметра. Используются **Python**, **pytest** и **Allure** для написания тестов и генерации отчётов.

## Структура проекта

- `base_api/` - API-классы и вспомогательные функции для выполнения запросов.
  - `generate_palindrome_api.py` - класс `GeneratePalindrome` с методами `POST` и `GET`.
  - `requests_helper.py` - вспомогательные классы и функции для HTTP-запросов.
- `tests/` - тестовые кейсы для API.
  - `test_generate_palindrome.py` - тесты для проверки генерации палиндромов и случайных строк.
- `requirements.txt` - зависимости проекта.

## Запуск тестов

#### pip install -r requirements.txt
#### python -m pytest tests .
#### Дождаться завершения тестов
#### allure serve allure-results
