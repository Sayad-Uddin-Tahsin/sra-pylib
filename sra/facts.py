import requests
import sra


class Bird:
    """
    Returns a random Fact about Bird by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self):
        self.__resp = None
        try:
            self.__resp = requests.get("https://some-random-api.ml/facts/bird")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")

        self.__resp = self.__resp.json()

        self.fact = self.__resp['fact']
        self.raw = self.__resp


class Cat:
    """
    Returns a random Fact about Cat by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self):
        self.__resp = None
        try:
            self.__resp = requests.get("https://some-random-api.ml/facts/cat")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")

        self.__resp = self.__resp.json()

        self.fact = self.__resp['fact']
        self.raw = self.__resp


class Dog:
    """
    Returns a random Fact about Dog by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self):
        self.__resp = None
        try:
            self.__resp = requests.get("https://some-random-api.ml/facts/dog")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")

        self.__resp = self.__resp.json()

        self.fact = self.__resp['fact']
        self.raw = self.__resp


class Fox:
    """
    Returns a random Fact about Fox by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self):
        self.__resp = None
        try:
            self.__resp = requests.get("https://some-random-api.ml/facts/fox")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")

        self.__resp = self.__resp.json()

        self.fact = self.__resp['fact']
        self.raw = self.__resp


class Koala:
    """
    Returns a random Fact about Koala by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self):
        self.__resp = None
        try:
            self.__resp = requests.get("https://some-random-api.ml/facts/koala")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")

        self.__resp = self.__resp.json()

        self.fact = self.__resp['fact']
        self.raw = self.__resp


class Panda:
    """
    Returns a random Fact about Panda by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self):
        self.__resp = None
        try:
            self.__resp = requests.get("https://some-random-api.ml/facts/panda")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")

        self.__resp = self.__resp.json()

        self.fact = self.__resp['fact']
        self.raw = self.__resp
