import logging
import allure
from requests import Session
import curlify

class BaseSession(Session):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, **kwargs):
        full_url = f'{self.base_url}{url}'
        with allure.step(f'{method} {full_url}'):
            response = super().request(method, url=full_url, **kwargs)
            msg = curlify.to_curl(response.request)
            logging.info(f'{response.status_code} {msg}')
            allure.attach(
                body=msg.encode('utf-8'),
                name=f'Request {method} {response.status_code}',
                attachment_type=allure.attachment_type.TEXT,
                extension='txt'
            )
        return response

def url_generate_palindrome() -> BaseSession:
    return BaseSession(base_url='https://www.generate_palindrome.com/')
