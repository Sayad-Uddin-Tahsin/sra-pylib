import requests
import sra

class Bird():
    """
    Returns an Image Link and a Fact about Bird

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/bird")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="bird.png"):
        """
        Saves the Bird Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Cat():
    """
    Returns an Image Link and a Fact about Cat

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/cat")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="cat.png"):
        """
        Saves the Cat Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Dog():
    """
    Returns an Image Link and a Fact about Dog

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/dog")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="dog.png"):
        """
        Saves the Dog Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Fox():
    """
    Returns an Image Link and a Fact about Fox

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/fox")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="fox.png"):
        """
        Saves the Fox Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Kangaroo():
    """
    Returns an Image Link and a Fact about Kangaroo

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/kangaroo")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="kangaroo.png"):
        """
        Saves the Kangaroo Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Koala():
    """
    Returns an Image Link and a Fact about Koala

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/koala")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="koala.png"):
        """
        Saves the Koala Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Panda():
    """
    Returns an Image Link and a Fact about Panda

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/panda")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="panda.png"):
        """
        Saves the Panda Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Raccoon():
    """
    Returns an Image Link and a Fact about Raccoon

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/raccoon")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="raccoon.png"):
        """
        Saves the Raccoon Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class RedPanda():
    """
    Returns an Image Link and a Fact about Red Panda

    :raise APITimeout: API taken too long to respond!
    :raise APIError: Error Returned by API
    """
    try:
        __resp = requests.get("https://some-random-api.ml/animal/red_panda")
    except requests.exceptions.ConnectionError:
            raise sra.exceptions.APITimeout("API taken too long to respond!")
    if __resp.status_code != 200:
        if 'error' in __resp.json():
            raise sra.exceptions.APIError(__resp.json()['error'])
        else:
            raise sra.exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")

    __resp = __resp.json()

    image_link = __resp['image']
    fact = __resp['fact']

    @classmethod
    def save_image(cls, name: str="red panda.png"):
        """
        Saves the Red Panda Image

        :param name: Image Name/PATH (Optional)
        :returns: Image, bool
        :raise InvalidFileFormat: When an unsupported file format given
        :raise ImageNotFound: When failed to save Image
        """
        formats = ['.png', '.jpg', '.jpeg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break
        if not validFormat:
            raise sra.exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        try:
            __r = requests.get(cls.image_link, stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")
