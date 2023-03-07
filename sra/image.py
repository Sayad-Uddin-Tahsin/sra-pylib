import requests
from sra import exceptions


class Bird():
    """
    Returns a random Image Link about Bird by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/bird")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="bird.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Cat():
    """
    Returns a random Image Link about Cat by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/cat")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="cat.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Dog():
    """
    Returns a random Image Link about Dog by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/dog")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="dog.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Fox():
    """
    Returns a random Image Link about Fox by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/fox")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="fox.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Kangaroo():
    """
    Returns a random Image Link about Kangaroo by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/kangaroo")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="kangaroo.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Koala():
    """
    Returns a random Image Link about Koala by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/koala")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="koala.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Panda():
    """
    Returns a random Image Link about Panda by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/panda")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="panda.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Pikachu():
    """
    Returns a random Image Link about Pikachu by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/pikachu")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="pikachu.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Raccoon():
    """
    Returns a random Image Link about Raccoon by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/raccoon")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="raccoon.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class RedPanda():
    """
    Returns a random Image Link about Red Panda by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/red_panda")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="red panda.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Whale():
    """
    Returns a random Image Link about Whale by attributes
    """
    try:
        __resp = requests.get("https://some-random-api.ml/img/whale")
    except requests.exceptions.ConnectionError:
        raise exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        raise exceptions.APIError(
            f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['link']

    @classmethod
    def save_image(cls, name: str="whale.png"):
        """
        Saves the Image

        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")
