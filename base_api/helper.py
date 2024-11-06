import uuid

def check_valid_uuid(uuid_str: str):
    try:
        uuid.UUID(uuid_str)
    except ValueError:
        assert False, f"Некорректный формат UUID: {uuid_str}"


def check_str_is_palindrome(str_palindrome: str, is_palindrome: bool):
    if is_palindrome:
        assert str_palindrome == str_palindrome[::-1], f"Ожидалось, что строка '{str_palindrome}' является палиндромом, но это не так."
    else:
        assert str_palindrome != str_palindrome[::-1], f"Ожидалось, что строка '{str_palindrome}' не является палиндромом, но она является."
