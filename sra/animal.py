import requests

class Bird():
    """
    :return: image_link and fact about Bird
    :rtype: str
    """
    __resp = requests.get("https://some-random-api.ml/animal/bird").json()
    image_link = __resp['image']
    fact = __resp['fact']





























