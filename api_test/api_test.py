import requests
import logging
from http.client import HTTPConnection
import allure


log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)
fh = logging.FileHandler("requests.log")
log.addHandler(fh)


@allure.story("Получить headers")
def test_get_headers_host():
    response = requests.get("http://httpbin.org/headers")
    with allure.step(
         "Запрос отправлен. Десериализируем ответ из json в словарь."):
        response_body = dict(response.json())
    assert response_body["headers"]["Host"] == "httpbin.org"


@allure.story("Получить код ответа")
def test_get_code():
    code = 200
    response = requests.get(f"http://httpbin.org/status/{code}")
    assert response.status_code == code


@allure.story(
    "Сделать запрос с n редиректами и получить соответсвующий код ответа")
def test_get_redirects():
    redirects = 2
    response = requests.get(f"https://nghttp2.org/httpbin/redirect/{redirects}",
                               allow_redirects=False)
    codes=[]
    with allure.step("Добавляем полученный код после редиректа в массив"):
        for i in range(redirects):
            codes.append(response.status_code)
    print(codes)
    assert len(codes) == redirects
    assert response.status_code == 302
      
       

