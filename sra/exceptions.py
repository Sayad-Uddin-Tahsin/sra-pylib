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


class InvalidImageURL(Exception):
    """
    raises when the Image URL is Invalid
    """


class InvalidHEXColor(Exception):
    """
    raises when given HEX Color Code in Invalid
    """


class InvalidBrightnessPower(Exception):
    """
    raises when the Brightness Power is greater than 255 or lesser than 0
    """


class InvalidRGBCode(Exception):
    """
    raises when RGB Code is Invalid
    """


class DisplayNameError(Exception):
    """
    raises when Display name don't meet conditions
    """


class UsernameError(Exception):
    """
    raises when Username don't meet conditions
    """


class CommentError(Exception):
    """
    raises when Comment don't meet conditions
    """


class ThemeError(Exception):
    """
    raises when Theme is Invalid
    """


class APIError(Exception):
    """
    raises when API responses an error!
    """


class APITimeout(Exception):
    """
    raises when API responses an error!
    """


class ImageRetrieveError(Exception):
    """
    raises when API responses an error!
    """


class InvalidTemplate(Exception):
    """
    raises when the Template is Invalid
    """


class InvalidBackground(Exception):
    """
    raises when the Background is Invalid
    """


class InvalidFont(Exception):
    """
    raises when the Font is Invalid
    """


class InvalidType(Exception):
    """
    raises when the Type is Invalid
    """


class InvalidTextColor(Exception):
    """
    raises when the Text Color is Invalid
    """


class ThresholdError(Exception):
    """
    raises when the Threshold Power is Invalid
    """
