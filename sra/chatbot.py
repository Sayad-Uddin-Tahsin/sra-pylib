import urllib.parse
import sra
import requests


def get_response(key: str, prompt: str):
    """
    Get ChatBot Response

    :param key: API Key (at least tier 1)
    :param prompt: The Prompt (Message that will be sent to the chatbot)
    :return: Chatbot Response
    """
    try:
        __resp = requests.get(
            f"https://some-random-api.ml/chatbot?message={urllib.parse.quote_plus(prompt)}&key={key}")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
    __resp = __resp.json()
    response = __resp['response']

    return response
