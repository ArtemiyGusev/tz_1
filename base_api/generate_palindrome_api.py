from requests import Response
from base_api.requests_helper import url_generate_palindrome

class GeneratePalindrome:
    def __init__(self, url: str = "/api/v1/generate_palindrome"):
        self.url = url

    def post_generate_palindrome(self, json=None) -> Response:
        session = url_generate_palindrome()
        return session.post(self.url, json={} if json is None else json)

    def get_generate_palindrome(self, params: dict = None) -> Response:
        session = url_generate_palindrome()
        return session.get(self.url, params={} if params is None else params)
