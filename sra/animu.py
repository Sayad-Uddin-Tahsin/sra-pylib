import requests
from sra import exceptions


class FacePalm():
    """
    Returns the GIF Link of a Face Palm by attributes

    Attributes:
        gif_link (str):
            The link to the Face Palm GIF.
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animu/face-palm")
    except requests.exceptions.ConnectionError:
            raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    gif_link = __resp['link']

    @classmethod
    def save_gif(cls, name: str='face palm.gif'):
        """
        Saves the Face Palm GIF

        :param name: Image Name/PATH (Optional)
        :returns: GIF, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        if not str(name).endswith(".gif"):
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".gif"!')
        path = name
        try:
            r = requests.get(cls.gif_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the GIF. Status Code: {r.status_code} returned")


class Hug():
    """
    Returns the GIF Link of a Hug by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animu/hug")
    except requests.exceptions.ConnectionError:
            raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    gif_link = __resp['link']

    @classmethod
    def save_gif(cls, name: str='hug.gif'):
        """
        Saves the Hug GIF

        :param name: Image Name/PATH (Optional)
        :returns: GIF, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        if not str(name).endswith(".gif"):
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".gif"!')
        path = name
        try:
            r = requests.get(cls.gif_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the GIF. Status Code: {r.status_code} returned")


class Pat():
    """
    Returns the GIF Link of a Pat by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animu/pat")
    except requests.exceptions.ConnectionError:
            raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    gif_link = __resp['link']

    @classmethod
    def save_gif(cls, name: str='pat.gif'):
        """
        Saves the Pat GIF

        :param name: Image Name/PATH (Optional)
        :returns: GIF, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        if not str(name).endswith(".gif"):
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".gif"!')
        path = name
        try:
            r = requests.get(cls.gif_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the GIF. Status Code: {r.status_code} returned")


class Wink():
    """
    Returns the GIF Link of a Wink by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animu/wink")
    except requests.exceptions.ConnectionError:
            raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    gif_link = __resp['link']

    @classmethod
    def save_gif(cls, name: str='wink.gif'):
        """
        Saves the Wink GIF

        :param name: Image Name/PATH (Optional)
        :returns: GIF, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        if not str(name).endswith(".gif"):
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".gif"!')
        path = name
        try:
            r = requests.get(cls.gif_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the GIF. Status Code: {r.status_code} returned")


class Quote():
    """
    Returns a random Quote from Anime by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animu/quote").json()
    except requests.exceptions.ConnectionError:
            raise exceptions.APITimeout("API taken too long to respond!")
    quote = __resp['sentence']
    character = __resp['character']
    anime_name = __resp['anime']

    @classmethod
    def structured(cls):
        """
        Returns a random Quote in a structured Way

        :returns: str
        """

        return f"{cls.quote}\n-: {cls.character}/{cls.anime_name}"
