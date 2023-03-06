class ImageNotFound(Exception):
    """
    raises when it fails to save the Image from URL
    """

class InvalidFileFormat(Exception):
    """
    raises when Invalid File Format is Given
    """

class InvalidAvatarURL(Exception):
    """
    raises when the Avatar URL is Invalid
    """

class InvalidBrightnessPower(Exception):
    """
    raises when the Brightness Power is greater than 255 or lesser than 0
    """