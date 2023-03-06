import requests
from sra import exceptions


class Bird():
    """
    Returns an Image Link and a Fact about Bird
    """
    __resp = requests.get("https://some-random-api.ml/animal/bird").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Cat():
    """
    Returns an Image Link and a Fact about Cat
    """
    __resp = requests.get("https://some-random-api.ml/animal/cat").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Dog():
    """
    Returns an Image Link and a Fact about Dog
    """
    __resp = requests.get("https://some-random-api.ml/animal/dog").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Fox():
    """
    Returns an Image Link and a Fact about Fox
    """
    __resp = requests.get("https://some-random-api.ml/animal/fox").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Kangaroo():
    """
    Returns an Image Link and a Fact about Kangaroo
    """
    __resp = requests.get("https://some-random-api.ml/animal/kangaroo").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Koala():
    """
    Returns an Image Link and a Fact about Koala
    """
    __resp = requests.get("https://some-random-api.ml/animal/koala").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Panda():
    """
    Returns an Image Link and a Fact about Panda
    """
    __resp = requests.get("https://some-random-api.ml/animal/panda").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class Raccoon():
    """
    Returns an Image Link and a Fact about Raccoon
    """
    __resp = requests.get("https://some-random-api.ml/animal/raccoon").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")


class RedPanda():
    """
    Returns an Image Link and a Fact about Red Panda
    """
    __resp = requests.get("https://some-random-api.ml/animal/red_panda").json()
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
            raise exceptions.InvalidFileFormat('Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name
        __r = requests.get(cls.image_link, stream=True)
        if __r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__r.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__r.status_code} returned")
