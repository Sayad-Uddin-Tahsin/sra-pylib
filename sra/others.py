import urllib.parse
import requests
import sra


class Base64:
    """
    Encode and Decode Base64 Code.
    """

    @classmethod
    def encode(cls, text: str):
        """
        Encode a Text to Base64 code

        :param text: The Human Readable text
        :return: str
        """

        try:
            __resp = requests.get(f"https://some-random-api.ml/base64?encode={urllib.parse.quote_plus(text)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            try:
                __resp = __resp.json()
                if 'error' in __resp:
                    raise sra.exceptions.APIError(__resp['error'])
            except:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        encoded = __resp['base64']
        return encoded

    @classmethod
    def decode(cls, base64: str):
        """
        Encode a Base64 code to Human Readable text

        :param base64: The Base64 Encoded Text
        :return: str
        """

        try:
            __resp = requests.get(f"https://some-random-api.ml/base64?decode={urllib.parse.quote_plus(base64)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            try:
                __resp = __resp.json()
                if 'error' in __resp:
                    raise sra.exceptions.APIError(__resp['error'])
            except:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        decoded = __resp['text']
        return decoded


class Binary:
    """
    Encode and Decode Binary Code.
    """

    @classmethod
    def encode(cls, text: str):
        """
        Encode a Text to Binary code

        :param text: The Human Readable text
        :return: str
        """

        try:
            __resp = requests.get(f"https://some-random-api.ml/binary?encode={urllib.parse.quote_plus(text)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            try:
                __resp = __resp.json()
                if 'error' in __resp:
                    raise sra.exceptions.APIError(__resp['error'])
            except:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        encoded = __resp['binary']
        return encoded

    @classmethod
    def decode(cls, binary: str):
        """
        Encode a Binary code to Human Readable text

        :param binary: The Binary Code
        :return: str
        """

        try:
            __resp = requests.get(f"https://some-random-api.ml/binary?decode={urllib.parse.quote_plus(binary)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            try:
                __resp = __resp.json()
                if 'error' in __resp:
                    raise sra.exceptions.APIError(__resp['error'])
            except:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        decoded = __resp['text']
        return decoded


def BotToken(id: str = None):
    """
    Generates Fake Discord Bot Token

    :param id: ID of the Bot (Optional)
    :return: str
    """
    try:
        __resp = requests.get(f"https://some-random-api.ml/bottoken?id={urllib.parse.quote_plus(id)}")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
    __resp = __resp.json()

    token = __resp['token']
    return token


def Dictionary(word: str):
    """
    Get the Definition of any Word!

    :param word: The word you want to find
    :return: str
    """
    try:
        __resp = requests.get(f"https://some-random-api.ml/dictionary?word={urllib.parse.quote_plus(word)}")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
    __resp = __resp.json()

    definition = __resp['definition']
    return definition


def Joke():
    """
    Get a random Jokes

    :return: str
    """
    try:
        __resp = requests.get(f"https://some-random-api.ml/joke")
    except requests.exceptions.ConnectionError:
        raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
    __resp = __resp.json()

    joke = __resp['joke']
    return joke


class Lyrics:
    """
    Get Lyrics by Name

    :return: str
    """

    def __init__(self, name: str):
        """
        Returns title, author, lyrics, thumbnail, link, disclaimer, structured and raw response by attributes
        :param name: Song Name
        """
        self.title, self.author, self.lyrics, self.thumbnail, self.link, self.disclaimer, self.raw = self.__search(name)
        self.structured = self.__structured(name)

    @staticmethod
    def __search(name: str):
        try:
            __resp = requests.get(f"https://some-random-api.ml/others/lyrics?title={name}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if __resp.status_code != 200:
            if 'error' in __resp.json():
                raise sra.exceptions.APIError(__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")
        __resp = __resp.json()

        title = str(__resp['title']).title()
        author = __resp['author']
        lyrics = __resp['lyrics']
        thumbnail = __resp['thumbnail']['genius']
        link = __resp['links']['genius']
        disclaimer = __resp['disclaimer']
        return title, author, lyrics, thumbnail, link, disclaimer, __resp

    def __structured(self, name: str):
        title, author, lyrics, thumbnail, link, disclaimer, raw = self.__search(name=name)
        return f"Title: {title}\nAuthor: {author}\nThumbnail: {thumbnail}\nLink: {link}\n\nLyrics:\n{lyrics}\n*{disclaimer}*"
