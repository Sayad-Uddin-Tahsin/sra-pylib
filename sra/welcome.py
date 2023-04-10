import urllib.parse
import sra
import requests
import re
import shutil


def is_valid_url(url):
    pattern = re.compile(
        r'^https?://'
        r'(?:[a-z0-9]+(?:\.[a-z0-9]+)*/)*'
        r'[a-z0-9]+\.[a-z]+/?$'
    )
    return bool(pattern.match(url))

def get_exact_avatar_url(url):
    if "?" in str(url):
        url = (str(url).split("?"))[0]
    return url

class WelcomeLeaveFree:
    """
    Generates Welcome and Leave image (Free Version)
    """

    def __init__(self, template_no: int, background: str, type: str, username: str, avatar_url: str, discriminator: str, guildName: str, memberCount: int, textcolor: str, key: str, font_no: int = None, Filename: str = None):
        if template_no not in range(1, 8):
            raise sra.exceptions.InvalidTemplate("Template Number must be within 1 - 7!")
        backgrounds = ['stars', 'stars2', 'rainbowgradient', 'rainbow', 'sunset', 'night', 'blobday', 'blobnight', 'space', 'gaming1', 'gaming2', 'gaming3', 'gaming4']
        if background not in backgrounds:
            raise sra.exceptions.InvalidBackground(f"Invalid Background! Background must be one of these: {', '.join(backgrounds)}")
        if font_no != None and font_no not in range(1, 11):
            raise sra.exceptions.InvalidFont("Font Number must be within 1 - 10!")
        if type not in ['join', 'leave']:
            raise sra.exceptions.InvalidType("Invalid Type! Type must be 'join' or 'leave'")
        textcolors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'pink', 'black', 'white']
        if textcolor not in textcolors:
            raise sra.exceptions.InvalidTextColor(f"Invalid Text Color! Text Color must be one of these: {', '.join(textcolors)}")

        username = urllib.parse.quote_plus(username)
        guildName = urllib.parse.quote_plus(guildName)
        self.__get(template=template_no, background=background, type=type, username=username, avatar_url=avatar_url, discriminator=discriminator, guildName=guildName, memberCount=memberCount, textcolor=textcolor, key=key, font=font_no, name=Filename)

    def __get(self, template, background, type, username, avatar_url, discriminator, guildName, memberCount, textcolor, key, font, name):
        if not is_valid_url(avatar_url):
            raise sra.exceptions.InvalidAvatarURL(
                "Seems the Avatar URL is Invalid. Please recheck it and make sure it startswith http or https")
        avatar_url = get_exact_avatar_url(avatar_url)
        if not str(avatar_url).endswith(".jpg") and not str(avatar_url).endswith(".png"):
            raise sra.exceptions.InvalidAvatarURL(
                "Avatar Format must be '.jpg' or '.png'"
            )

        if name == None:
            name = f'{str(type).title()} {username}.png'
        else:
            formats = ['.png', '.jpg', '.jpeg']
            validFormat = False
            for f in formats:
                if str(name).endswith(f):
                    validFormat = True
                    break

            if not validFormat:
                raise sra.exceptions.InvalidFileFormat(
                    'Invalid File Format given. File Format must be ".png", ".jpg" or "jpeg"!')
        path = name

        try:
            __resp = requests.get(f"https://some-random-api.ml/welcome/img/{str(template)}/{str(background)}?type={type}&username={username}&avatar={avatar_url}&discriminator={discriminator}&guildName={guildName}&memberCount={memberCount}&textcolor={textcolor}&key={key}{'&font=' + str(font) if font != None else ''}", stream=True)
        except requests.exceptions.ConnectionError:
            raise sra.exceptions.ImageRetrieveError("Unable to Load the Image!")
        if __resp.status_code == 200:
            with open(path, 'wb') as f:
                __resp.raw.decode_content = True
                shutil.copyfileobj(__resp.raw, f)
            return True
        else:
            raise sra.exceptions.ImageNotFound(f"Couldn't save the Image. Status Code: {__resp.status_code} returned")
