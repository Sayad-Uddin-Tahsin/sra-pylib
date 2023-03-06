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


class CanvasFilter():
    """
    The Main Class of Canvas/Filter. Filter APIs are available as Sub-Class.
    """

    class Blue():
        """
        Blueify your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/blue?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Blurple():
        """
        Blurplify your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/blurple?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Blurple2():
        """
        Blurplify your Avatar (New Discord blurple). Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/blurple2?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Brightness():
        """
        Brighten your Avatar. Use filter() with Avatar URL, Brightness Power (Optional) and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, brightness: int=30, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param brightness: The Brightness power (0 - 255)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/brightness?avatar={avatar_url}&brightness={brightness}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Color():
        """
        Tint your Avatar a certain color. Use filter() with Avatar URL, Color code in HEX and Name to Filter and Save the Image. An alias of Tint
        """

        @classmethod
        def filter(cls, avatar_url: str, color: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param color: The Color Code in HEX without #
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/color?color={color}&avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Tint():
        """
        Tint your Avatar a certain color. Use filter() with Avatar URL, Color code in HEX and Name to Filter and Save the Image.
        """

        @classmethod
        def filter(cls, avatar_url: str, color: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param color: The Color Code in HEX without #
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/color?color={color}&avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Green():
        """
        Make your Avatar green like the Hulk. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/green?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Greyscale():
        """
        Greyscale your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/greyscale?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class InvertGrayscale():
        """
        Invert and grayscale your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/invertgreyscale?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Red():
        """
        Redify your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/red?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Sepia():
        """
        Apply a sepia filter to your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/filter/sepia?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Threshold():
        """
        Threshold your Avatar. Use filter() with Avatar URL, Threshold (Optional) and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, threshold: int=100, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param threshold: Enter the Threshold integer
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/threshold?avatar={avatar_url}&threshold={threshold}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")



class CanvasMisc():
    """
        The Main Class of Canvas/Misc. Misc APIs are available as Sub-Class.
    """

    class BisexualBorder():
        """
        Add a bisex flag border to your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/bisexual?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Blur():
        """
        Blur your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/blur?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class CircleCrop():
        """
        Crop an image to a Circle. Use save() with Image URL and Name to Crop and Save the Image
        """

        @classmethod
        def save(cls, image_url: str, name: str="image.png"):
            """
            Save the Cropped Image

            :param image_url: The URL of the Image
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/crop?avatar={image_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class ColorViewer():
        """
        View a color. Use save() with Hex Color Code and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, hex: str, name: str="image.png"):
            """
            Saves the Color into Image

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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/colorviewer?hex={hex}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class HeartCrop():
        """
        Crop an image to a heart shape. Use save() with Image URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, image_url: str, name: str="image.png"):
            """
            Crop and Save the cropped Image.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/heart?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class RGBtoHEX():
        """
        Converts RGB code to HEX code. Use convert() for the conversion.
        """

        @classmethod
        def convert(cls, rgb: str):
            """
            Converts RGB to HEX

            :param rgb: Enter the RGB Code
            :return: HEX Code
            """
            codes = rgb.split(",")
            if len(codes) != 3:
                raise exceptions.InvalidRGBCode(f"RGB Color Code must contains 3 blocks!")

            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/hex?rgb={rgb}")

            if __resp.status_code == 200:
                hex = __resp.json()['hex']
                return hex
            else:
                raise exceptions.InvalidResponse(
                    f"API is maybe Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")


    class Horny():
        """
        Makes Horny card with the Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/horny?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class ItsSoStupid():
        """
        Make an "Its so stupid" meme with your Avatar. Use filter() with Avatar URL and Name to make and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/its-so-stupid?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")




    class Jpg():
        """
        Blur your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image. An alias of Blur
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/jpg?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class LesbianBorder():
        """
        Add a lesbian flag border to your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/lesbian?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class LGBTBorder():
        """
        Add a lgbt flag border to your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/lgbt?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Lolice():
        """
        Make Loli police to your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/lolice?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class GenshinNamecard():
        """
        Make Genshin Namecard. Use save() with Avatar URL, Username, Birthday and Description (Optional) to Save the Image
        """

        @classmethod
        def save(cls, avatar_url: str, username: str, birthday: str, description: typing.Optional[str]=None, name: str="image.png"):
            """
            Make and Save a Namecard.

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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/namecard?avatar={avatar_url}&birthday={birthday}&username={username}{'&description=' + description if description != None else ''}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class NoBitches():
        """
        Make No Bitches Meme. Use save() with a text to Save the Image
        """

        @classmethod
        def save(cls, text, name: str="image.png"):
            """
            Make and Save a Namecard.

            :param text: The Text on the Meme
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/nobitches?no={urllib.parse.quote_plus(text)}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class NonbinaryBorder():
        """
        Make Nonbinary Bordered Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/nonbinary?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Oogway():
        """
        Make Oogway meme with custom quote. Use save() with Custom Quote and Name to Filter and Save the meme
        """

        @classmethod
        def filter(cls, quote: str, name: str="image.png"):
            """
            Make and Save.

            :param quote: The Custom Quote
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/oogway?quote={urllib.parse.quote_plus(quote)}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Oogway2():
        """
        Make Oogway meme with custom quote (Updated). Use save() with Custom Quote and Name to Filter and Save the meme
        """

        @classmethod
        def filter(cls, quote: str, name: str="image.png"):
            """
            Make and Save.

            :param quote: The Custom Quote
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/oogway2?quote={urllib.parse.quote_plus(quote)}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class PansexualBorder():
        """
        Make Pansexual Bordered Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/pansexual?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Pixelate():
        """
        Make your Pixelated Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/pixelate?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class HEXtoRGB():
        """
        Converts HEX code to RGB code. Use convert() for the conversion.
        """

        @classmethod
        def convert(cls, hex: str):
            """
            Converts HEX to RGB

            :param hex: Enter the RGB Code
            :return: RGB Code
            """
            if hex.startswith("#"):
                hex = hex.replace("#", "", 1)

            if len(hex) not in [6, 8]:
                raise exceptions.InvalidHEXColor(f"Given HEX Color Code must be 6 or 8 in length, but given code is {len(hex)} in length")

            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/rgb?hex={hex}")

            if __resp.status_code == 200:
                __resp = __resp.json()
                rgb = f"{__resp['r']}, {__resp['g']}, {__resp['b']}"
                return rgb
            else:
                raise exceptions.InvalidResponse(
                    f"API is maybe Down now, Please try again later!\nStatus Code: {__resp.status_code} returned, 200 expected!")


    class SimpCard():
        """
        Make Simp Card with your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/simpcard?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Tonikawa():
        """
        Make Tonikawa with your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/tonikawa?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class TransgenderBorder():
        """
        Make Transgender Border with your Avatar. Use filter() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def filter(cls, avatar_url: str, name: str="image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL("Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/misc/transgender?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Tweet():
        """
        Make Fake Tweet. Use save() with Display Name, Username, Avatar URL, Comment, Number of Reply, Number of Like, Number of Retweet, Theme and Name for file to Filter and Save the Image
        """

        themes = typing.Literal['light', 'dim', 'dark']
        @classmethod
        def save(cls, display_name: str, username:str, avatar_url: str, comment: str, replyNumber: typing.Optional[int]=None, likeNumber: typing.Optional[int]=None, retweetNumber: typing.Optional[int]=None, theme: themes='light', name: str="image.png"):
            """
            Save the Fake Tweet Image.

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
            __resp = requests.get(f"https://some-random-api.ml/canvas/tweet?avatar={avatar_url}&displayname={urllib.parse.quote_plus(display_name)}&username={urllib.parse.quote_plus(username)}&comment={urllib.parse.quote_plus(comment)}{'&replies=' + str(replyNumber) if replyNumber != None else ''}{'&likes=' + str(likeNumber) if likeNumber != None else ''}{'&retweets=' + str(retweetNumber) if retweetNumber != None else ''}&theme={theme.lower()}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class YoutubeComment():
        """
        Make Fake Youtube Comment. Use save() with Username, Avatar URL, Comment and Name for file to Filter and Save the Image
        """

        @classmethod
        def save(cls, username: str, avatar_url: str, comment: str, name: str="image.png"):
            """
            Save the Fake Tweet Image.

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
            if not avatar_url.endswith(".jpg") or not avatar_url.endswith(".png"):
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
            __resp = requests.get(
                f"https://some-random-api.ml/canvas/youtube-comment?avatar={avatar_url}&username={urllib.parse.quote_plus(username)}&comment={urllib.parse.quote_plus(comment)}",
                stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


class CanvasOverlay():
    """
    The Main Class of Canvas/Overlay. Overlay APIs are available as Sub-Class.
    """

    class Comrade():
        """
        Make Comraded Avatar. Use overlay() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def overlay(cls, avatar_url: str, name: str = "image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL(
                    "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
            if not avatar_url.endswith(".jpg") or not avatar_url.endswith(".png"):
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/comrade?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Gay():
        """
        Give your Avatar a rainbow overlay. Use overlay() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def overlay(cls, avatar_url: str, name: str = "image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL(
                    "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
            if not avatar_url.endswith(".jpg") or not avatar_url.endswith(".png"):
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/gay?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Glass():
        """
        Give your Avatar a glass effect overlay. Use overlay() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def overlay(cls, avatar_url: str, name: str = "image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL(
                    "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
            if not avatar_url.endswith(".jpg") or not avatar_url.endswith(".png"):
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/glass?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Jail():
        """
        Make your Avatar Jailed. Use overlay() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def overlay(cls, avatar_url: str, name: str = "image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL(
                    "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
            if not avatar_url.endswith(".jpg") or not avatar_url.endswith(".png"):
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/jail?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Passed():
        """
        Mission passed overlay to your Avatar. Use overlay() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def overlay(cls, avatar_url: str, name: str = "image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL(
                    "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
            if not avatar_url.endswith(".jpg") or not avatar_url.endswith(".png"):
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/passed?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Triggered():
        """
        Get a Triggered GIF with your Avatar. Use overlay() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def overlay(cls, avatar_url: str, name: str = "image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL(
                    "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
            if not avatar_url.endswith(".jpg") or not avatar_url.endswith(".png"):
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/triggered?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")


    class Wasted():
        """
        Give your Avatar a Wasted overlay. Use overlay() with Avatar URL and Name to Filter and Save the Image
        """

        @classmethod
        def overlay(cls, avatar_url: str, name: str = "image.png"):
            """
            Filter and Save the Filtered Avatar.

            :param avatar_url: The URL of the Avatar (Format must be: .jpg or .png)
            :param name: Image Name/PATH (Optional)
            :return: Image, bool
            :raise InvalidFileFormat: When an unsupported file format is given
            :raise ImageNotFound: When failed to save Image
            """
            if not is_valid_url(avatar_url):
                raise exceptions.InvalidAvatarURL(
                    "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
            if not avatar_url.endswith(".jpg") or not avatar_url.endswith(".png"):
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
            __resp = requests.get(f"https://some-random-api.ml/canvas/wasted?avatar={avatar_url}", stream=True)
            if __resp.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(__resp.content)
                    return True
            else:
                raise exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")
