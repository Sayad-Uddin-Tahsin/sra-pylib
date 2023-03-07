import typing
import urllib.parse
import requests
from sra import exceptions
import re


def is_valid_url(url):
    pattern = re.compile(
        r'^https?://'
        r'([a-z0-9]+\.)*[a-z0-9]+\.[a-z]+/?'
        r'([^\s/]+/?)+$'
    )
    return bool(pattern.match(url))


class Filter():
    """
    The Main Class of Canvas/Filter. Filter APIs are available as Sub-Class.
    """

    @classmethod
    def Blue(cls, avatar_url: str, name: str="image.png"):
        """
        Blueify your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/blue?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Blurple(cls, avatar_url: str, name: str="image.png"):
        """
        Blurplify your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/blurple?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Blurple2(cls, avatar_url: str, name: str="image.png"):
        """
        Blurplify your Avatar (New Discord blurple).

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/blurple2?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Brightness(cls, avatar_url: str, brightness: int=30, name: str="image.png"):
        """
        Brighten your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param brightness: The Brightness power (0 - 255)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
        if not 0 <= brightness <= 255:
            raise exceptions.InvalidBrightnessPower("Brightness Power must be 0 - 255!")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/brightness?avatar={avatar_url}&brightness={brightness}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Color(cls, avatar_url: str, color: str, name: str="image.png"):
        """
        Tint your Avatar a certain color. An alias of Tint

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param color: The Color Code in HEX without #
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
        if color.startswith("#"):
            color = color.replace("#", "", 1)
        if len(color) not in [6, 8]:
            raise exceptions.InvalidHEXColor(f"Given HEX Color Code must be 6 or 8 in length, but given code is {len(color)} in length")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/color?color={color}&avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Tint(cls, avatar_url: str, color: str, name: str="image.png"):
        """
        Tint your Avatar a certain color.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param color: The Color Code in HEX without #
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
        if color.startswith("#"):
            color = color.replace("#", "", 1)
        if len(color) not in [6, 8]:
            raise exceptions.InvalidHEXColor(f"Given HEX Color Code must be 6 or 8 in length, but given code is {len(color)} in length")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/color?color={color}&avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def filter(cls, avatar_url: str, name: str="image.png"):
        """
        Make your Avatar green like the Hulk.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/green?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Greyscale(cls, avatar_url: str, name: str="image.png"):
        """
        Greyscale your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/greyscale?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def InvertGrayscale(cls, avatar_url: str, name: str="image.png"):
        """
        Invert and grayscale your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/invertgreyscale?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Red(cls, avatar_url: str, name: str="image.png"):
        """
        Redify your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/red?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Sepia(cls, avatar_url: str, name: str="image.png"):
        """
        Apply a sepia filter to your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/sepia?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Threshold(cls, avatar_url: str, threshold: int=100, name: str="image.png"):
        """
        Threshold your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param threshold: Enter the Threshold integer
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/threshold?avatar={avatar_url}&threshold={threshold}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")



class Misc():
    """
        The Main Class of Canvas/Misc. Misc APIs are available as Sub-Class.
    """


    @classmethod
    def BisexualBorder(cls, avatar_url: str, name: str="image.png"):
        """
        Add a bisex flag border to your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/bisexual?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Blur(cls, avatar_url: str, name: str="image.png"):
        """
        Blur your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/blur?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def CircleCrop(cls, image_url: str, name: str="image.png"):
        """
        Crop an image to a Circle.

        :param image_url: The URL of the Image
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/crop?avatar={image_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def ColorViewer(cls, hex: str, name: str="image.png"):
        """
        View a color.

        :param hex: The Color Code in HEX without #
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if hex.startswith("#"):
            hex = hex.replace("#", "", 1)
        if len(hex) not in [6, 8]:
            raise exceptions.InvalidHEXColor(f"Given HEX Color Code must be 6 or 8 in length, but given code is {len(hex)} in length")

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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/colorviewer?hex={hex}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def HeartCrop(cls, image_url: str, name: str="image.png"):
        """
        Crop an image to a heart shape

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/heart?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def RGBtoHEX(cls, rgb: str):
        """
        Converts RGB code to HEX code

        :param rgb: Enter the RGB Code
        :return: HEX Code
        """
        codes = rgb.split(",")
        if len(codes) != 3:
            raise exceptions.InvalidRGBCode(f"RGB Color Code must contains 3 blocks!")


        try:
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/hex?rgb={rgb}")
        except requests.exceptions.ConnectionError:
            raise exceptions.APITimeout("API taken too long to respond!")

        if __resp.status_code == 200:
            hex = __resp.json()['hex']
            return hex
        else:
            raise exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")


    @classmethod
    def Horny(cls, avatar_url: str, name: str="image.png"):
        """
        Makes Horny card with the Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/horny?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def ItsSoStupid(cls, avatar_url: str, name: str="image.png"):
        """
        Make an "Its so stupid" meme with your Avatar

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/its-so-stupid?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Jpg(cls, avatar_url: str, name: str="image.png"):
        """
        Blur your Avatar. An alias of Blur

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/jpg?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def LesbianBorder(cls, avatar_url: str, name: str="image.png"):
        """
        Add a lesbian flag border to your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/lesbian?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def LGBTBorder(cls, avatar_url: str, name: str="image.png"):
        """
        Add a lgbt flag border to your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/lgbt?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Lolice(cls, avatar_url: str, name: str="image.png"):
        """
        Make Loli police to your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/lolice?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def GenshinNamecard(cls, avatar_url: str, username: str, birthday: str, description: typing.Optional[str]=None, name: str="image.png"):
        """
        Make Genshin Namecard

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param username: A Username
        :param birthday: A Birthday
        :param description: A description (Optional)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/namecard?avatar={avatar_url}&birthday={birthday}&username={username}{'&description=' + description if description != None else ''}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def NoBitches(cls, text, name: str="image.png"):
        """
        Make No Bitches Meme.

        :param text: The Text on the Meme
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/nobitches?no={urllib.parse.quote_plus(text)}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def NonbinaryBorder(cls, avatar_url: str, name: str="image.png"):
        """
        Make Nonbinary Bordered Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/nonbinary?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Oogway(cls, quote: str, name: str="image.png"):
        """
        Make Oogway meme with custom quote.

        :param quote: The Custom Quote
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/oogway?quote={urllib.parse.quote_plus(quote)}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Oogway2(cls, quote: str, name: str="image.png"):
        """
        Make Oogway meme with custom quote (Updated).

        :param quote: The Custom Quote
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/oogway2?quote={urllib.parse.quote_plus(quote)}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def PansexualBorder(cls, avatar_url: str, name: str="image.png"):
        """
        Make Pansexual Bordered Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/pansexual?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Pixelate(cls, avatar_url: str, name: str="image.png"):
        """
        Make your Pixelated Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/pixelate?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def HEXtoRGB(cls, hex: str):
        """
        Converts HEX code to RGB code.

        :param hex: Enter the RGB Code
        :return: RGB Code
        """
        if hex.startswith("#"):
            hex = hex.replace("#", "", 1)

        if len(hex) not in [6, 8]:
            raise exceptions.InvalidHEXColor(f"Given HEX Color Code must be 6 or 8 in length, but given code is {len(hex)} in length")


        try:
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/rgb?hex={hex}")
        except requests.exceptions.ConnectionError:
            raise exceptions.APITimeout("API taken too long to respond!")

        if __resp.status_code == 200:
            __resp = __resp.json()
            rgb = f"{__resp['r']}, {__resp['g']}, {__resp['b']}"
            return rgb
        else:
            raise exceptions.APIError(
                f"API is  Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")


    @classmethod
    def SimpCard(cls, avatar_url: str, name: str="image.png"):
        """
        Make Simp Card with your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/simpcard?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Tonikawa(cls, avatar_url: str, name: str="image.png"):
        """
        Make Tonikawa with your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/tonikawa?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def TransgenderBorder(cls, avatar_url: str, name: str="image.png"):
        """
        Make Transgender Border with your Avatar

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/transgender?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    themes = typing.Literal['light', 'dark', 'dim']
    @classmethod
    def Tweet(cls, display_name: str, username:str, avatar_url: str, comment: str, replyNumber: typing.Optional[int]=None, likeNumber: typing.Optional[int]=None, retweetNumber: typing.Optional[int]=None, theme: themes='light', name: str="image.png"):
        """
        Make Fake Tweet

        :param display_name: The Display Name
        :param username: The Username
        :param avatar_url: URL of the Avatar
        :param comment: Comment for Fake Tweet
        :param replyNumber: Number of Replies will there be (Optional)
        :param likeNumber: Number of Likes will there be (Optional)
        :param retweetNumber: Number of retweets (Optional)
        :param theme: The Theme (Optional)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if len(display_name) > 32:
            raise exceptions.DisplayNameError("Display name length must be lesser than 32 characters!")
        if len(username) > 15:
            raise exceptions.UsernameError("Username length must be lesser than 15 characters!")
        if len(comment) > 1000:
            raise exceptions.CommentError("Comment length must be lesser than 1000 characters!")
        if theme.lower() not in ['light', 'dark', 'dim']:
            raise exceptions.ThemeError("Invalid Theme! Theme must be light, dark or dim!")
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )

        formats = ['.png', '.jpg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break

        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png" or ".jpg"!')

        path = name

        try:
            __resp = requests.get(f"https://some-random-api.ml/canvas/tweet?avatar={avatar_url}&displayname={urllib.parse.quote_plus(display_name)}&username={urllib.parse.quote_plus(username)}&comment={urllib.parse.quote_plus(comment)}{'&replies=' + str(replyNumber) if replyNumber != None else ''}{'&likes=' + str(likeNumber) if likeNumber != None else ''}{'&retweets=' + str(retweetNumber) if retweetNumber != None else ''}&theme={theme.lower()}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def YoutubeComment(cls, username: str, avatar_url: str, comment: str, name: str="image.png"):
        """
        Make Fake Youtube Comment.

        :param username: The Username
        :param avatar_url: URL of the Avatar
        :param comment: Comment for Fake Tweet
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if len(username) > 25:
            raise exceptions.UsernameError("Username length must be lesser than 15 characters!")
        if len(comment) > 1000:
            raise exceptions.CommentError("Comment length must be lesser than 1000 characters!")

        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
        formats = ['.png', '.jpg']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break

        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".png" or ".jpg"!')

        path = name

        try:
            __resp = requests.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={avatar_url}&username={urllib.parse.quote_plus(username)}&comment={urllib.parse.quote_plus(comment)}",
            stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")

        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


class Overlay():
    """
    The Main Class of Canvas/Overlay. Overlay APIs are available as function.
    """
    @classmethod
    def Comrade(cls, avatar_url: str, name: str = "image.png"):
        """
        Make Comraded Avatar

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/comrade?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Gay(cls, avatar_url: str, name: str = "image.png"):
        """
        Give your Avatar a rainbow overlay.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/gay?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Glass(cls, avatar_url: str, name: str = "image.png"):
        """
        Give your Avatar a glass effect overlay

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/glass?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Jail(cls, avatar_url: str, name: str = "image.png"):
        """
        Make your Avatar Jailed

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/jail?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Passed(cls, avatar_url: str, name: str = "image.png"):
        """
        Mission passed overlay to your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/passed?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Triggered(cls, avatar_url: str, name: str = "image.png"):
        """
        Get a Triggered GIF with your Avatar.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
        formats = ['.gif']
        validFormat = False
        for f in formats:
            if str(name).endswith(f):
                validFormat = True
                break

        if not validFormat:
            raise exceptions.InvalidFileFormat(
                'Invalid File Format given. File Format must be ".gif"!')

        path = name

        try:
            __resp = requests.get(f"https://some-random-api.ml/canvas/triggered?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    @classmethod
    def Wasted(cls, avatar_url: str, name: str = "image.png"):
        """
        Give your Avatar a Wasted overlay.

        :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
        :param name: Image Name/PATH (Optional)
        :return: Image, bool
        :raise InvalidFileFormat: When an unsupported file format is given
        :raise ImageNotFound: When failed to save Image
        """
        if not is_valid_url(avatar_url):
            raise exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/wasted?avatar={avatar_url}", stream=True)
        except requests.exceptions.ConnectionError:
            raise exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                f.write(__resp.content)
                return True
        else:
            raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")
