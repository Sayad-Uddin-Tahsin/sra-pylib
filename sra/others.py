import urllib.parse
import requests
import sra


class Base64:
    def __init__(self):
        __resp = None
    """
    Encode and Decode Base64 Code.
    """

    @classmethod
    def encode(cls, text: str):
        """
        Encode a Text to Base64 code

        :param text: The Human Readable text
        :return: str
        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
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
        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
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
        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
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
        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
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


class BotToken:
    """
    Generates Fake Discord Bot Token

    :param id: ID of the Bot (Optional)
    :return: str
    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self, id: str = None):
        self.__resp = None
        try:
            self.__resp = requests.get(f"https://some-random-api.ml/bottoken?id={urllib.parse.quote_plus(id)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")
        self.__resp = self.__resp.json()

        self.token = self.__resp['token']
        self.raw = self.__resp


class Dictionary:
    """
    Get the Definition of any Word!

    :param word: The word you want to find
    :return: str
    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self, word: str):
        self.__resp = None
        try:
            self.__resp = requests.get(f"https://some-random-api.ml/dictionary?word={urllib.parse.quote_plus(word)}")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")
        self.__resp = self.__resp.json()

        self.definition = self.__resp['definition']
        self.raw = self.__resp


class Joke:
    """
    Get a random Jokes

    :return: str
    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    def __init__(self):
        self.__resp = None
        try:
            self.__resp = requests.get(f"https://some-random-api.ml/joke")
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
        if self.__resp.status_code != 200:
            if 'error' in self.__resp.json():
                raise sra.exceptions.APIError(self.__resp.json()['error'])
            else:
                raise sra.exceptions.APIError(
                    f"API is  Down now, Please try again later!\nStatus Code: {self.__resp.status_code} returned, 200 expected!")
        self.__resp = self.__resp.json()

        self.joke = self.__resp['joke']
        self.raw = self.__resp


class Lyrics:
    """
    Get Lyrics by Name

    :return: str
    """

    def __init__(self, name: str):
        """
        :returns: title, author, lyrics, thumbnail, link, disclaimer, structured and raw response by attributes
        :param name: Song Name

        :raise APITimeout: API taken too long to respond!
        :raise APIError: Error Returned by API
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
