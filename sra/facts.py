import requests
import sra


class Bird:
    """
    Returns a random Fact about Bird by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/facts/bird")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    fact = __resp['fact']


class Cat:
    """
    Returns a random Fact about Cat by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/facts/cat")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    fact = __resp['fact']


class Dog:
    """
    Returns a random Fact about Dog by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/facts/dog")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    fact = __resp['fact']


class Fox:
    """
    Returns a random Fact about Fox by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/facts/fox")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    fact = __resp['fact']


class Koala:
    """
    Returns a random Fact about Koala by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/facts/koala")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    fact = __resp['fact']


class Panda:
    """
    Returns a random Fact about Panda by attributes


    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/facts/panda")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    fact = __resp['fact']
