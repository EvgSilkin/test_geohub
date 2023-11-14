import requests
import allure

from utils.logger.logger import Logger


class HttpMethods:

    @staticmethod
    def get(url, headers):
        Logger.add_request(url, method="GET")
        response = requests.get(url, headers=headers)
        Logger.add_response(response)
        return response

    @staticmethod
    def post(url, headers, body):
        with allure.step("GET"):
            Logger.add_request(url, method="POST")
            response = requests.post(url, headers=headers, data=body)
            Logger.add_response(response)
            return response

    @staticmethod
    def patch(url, headers, body):
        Logger.add_request(url, method="PATCH")
        response = requests.post(url, headers=headers, data=body)
        Logger.add_response(response)
        return response


