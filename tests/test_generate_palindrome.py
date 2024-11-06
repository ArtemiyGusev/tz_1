import allure
import pytest
from base_api.generate_palindrome_api import GeneratePalindrome
from base_api.helper import check_valid_uuid, check_str_is_palindrome


@allure.suite('GeneratePalindrome')
class TestGeneratePalindrome:

    @allure.sub_suite('PostGeneratePalindrome')
    @allure.title("Проверка генерации палиндрома или случайной строки через POST запрос")
    @pytest.mark.parametrize("palindrome", [True, False])
    def test_post_generate_palindrome(self, palindrome):
        json = {"palindrome": palindrome}
        response = GeneratePalindrome().post_generate_palindrome(json=json)
        assert response.status_code == 200, f"Неожиданный статус-код: {response.status_code}"

        response_json = response.json()
        uuid_value = response_json.get('id')
        result_value = response_json.get('result')

        assert uuid_value is not None, "Поле 'id' отсутствует в ответе"
        check_valid_uuid(uuid_value)

        assert result_value is not None, "Поле 'result' отсутствует в ответе"
        check_str_is_palindrome(result_value, is_palindrome=palindrome)

    @allure.sub_suite('PostGeneratePalindrome')
    @allure.title("Проверка обработки отсутствующего параметра palindrome в POST запросе")
    def test_post_generate_palindrome_missing_palindrome_param(self):
        response = GeneratePalindrome().post_generate_palindrome(json={})
        assert response.status_code in [400, 422], f"Ожидался код ошибки для запроса без параметра 'palindrome', получен: {response.status_code}"

    @allure.sub_suite('GetGeneratePalindrome')
    @allure.title("Проверка получения строки по валидному UUID через GET запрос")
    def test_get_generate_palindrome_valid_id(self):
        json = {"palindrome": True}
        post_response = GeneratePalindrome().post_generate_palindrome(json=json)
        assert post_response.status_code == 200, "Не удалось создать строку через POST"

        response_json = post_response.json()
        uuid_value = response_json.get('id')
        result_value = response_json.get('result')
        assert uuid_value is not None, "Поле 'id' отсутствует в ответе"
        assert result_value is not None, "Поле 'result' отсутствует в ответе"

        get_response = GeneratePalindrome().get_generate_palindrome(params={"id": uuid_value})
        assert get_response.status_code == 200, f"Неожиданный статус-код для GET запроса: {get_response.status_code}"

        get_response_json = get_response.json()
        assert get_response_json.get('result') == result_value, "Поле 'result' в ответе GET не совпадает с POST"

    @allure.sub_suite('GetGeneratePalindrome')
    @allure.title("Проверка обработки невалидного UUID при GET запросе")
    def test_get_generate_palindrome_invalid_id(self):
        invalid_uuid = "12345-invalid-uuid"
        response = GeneratePalindrome().get_generate_palindrome(params={"id": invalid_uuid})
        assert response.status_code in [400, 404], f"Ожидался код ошибки для невалидного UUID, получен: {response.status_code}"

    @allure.sub_suite('GetGeneratePalindrome')
    @allure.title("Проверка обработки GET запроса без обязательного параметра id")
    def test_get_generate_palindrome_without_id(self):
        response = GeneratePalindrome().get_generate_palindrome(params={})
        assert response.status_code == 400, f"Ожидался код ошибки 400 для запроса без параметра 'id', получен: {response.status_code}"
