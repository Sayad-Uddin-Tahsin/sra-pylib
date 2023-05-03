# sra-pylib
`sra-pylib` is a Python wrapper for [some-random-api](https://some-random-api.com).

```python
import sra
from sra import animal

# Create a new instance of the Panda class
panda = animal.Panda()

>>> print(panda.image_link)  # Prints a Panda Image link
"https://i.imgur.com/YVLrUO9.jpg"
>>> print(panda.fact)  # Prints a Panda Fact
"From 1974-1989, half of the panda’s habitat in China’s Sichuan areas was destroyed by human activity."
>>> panda.save_image("Cool Panda.png")  # Saves the Image
```
With `sra-pylib`, you can easily access the various endpoints of `some-random-api` in your Python projects, making it a powerful tool for working with image, fact, and other types of data.

<a href="https://pypi.org/project/sra-pylib"><img src="https://img.shields.io/pypi/status/sra-pylib?label=Status&logo=pypi&logoColor=ffffff" height=22></a>
<a href="https://pypi.org/project/sra-pylib"><img src="https://img.shields.io/pypi/v/sra-pylib?label=PyPI Version&logo=pypi&logoColor=ffffff" height=22></a>
<a href="https://app.fossa.com/projects/git%2Bgithub.com%2FSayad-Uddin-Tahsin%2Fsra-pylib?ref=badge_shield" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2FSayad-Uddin-Tahsin%2Fsra-pylib.svg?type=shield" height=22></a>
<a href="https://python.org"><img src="https://img.shields.io/pypi/pyversions/sra-pylib?label=Python&logo=python&logoColor=ffdd54" height=22></a>

## Installation
You can install `sra-pylib` using `pip`:
```console
python -m pip install sra-pylib
```
`sra-pylib` requires Python 3.7 or later.

## Endpoints
`sra-pylib` is synced with some-random-api. It has all the Endpoints provided by some-random-api except the Premium ones.

## Documentation
Full documentation for the sra-pylib module can be found on [Wiki](https://github.com/Sayad-Uddin-Tahsin/sra-pylib/wiki). The documentation includes detailed information on how to use the module, including examples and reference documentation for all classes and methods.

If you have any questions or issues with the module, please refer to the documentation or submit a bug report on the [GitHub issues page](https://github.com/Sayad-Uddin-Tahsin/sra-pylib/issues).


## Bug Report
If you encounter any bugs while using sra-pylib, please report them by opening a new issue on the [GitHub repository](https://github.com/Sayad-Uddin-Tahsin/sra-pylib/issues). When reporting a bug, please include the following information:

- A detailed description of the issue, including what you were trying to do when the bug occurred
- The full traceback or error message, if applicable
- Steps to reproduce the bug, if possible
- Any additional information or context that might be relevant to the issue

By reporting bugs, you can help improve the quality and reliability of sra-pylib for all user


## Cloning the Repository
You can easily clone this repository by executing the following command:
```console
git clone https://github.com/Sayad-Uddin-Tahsin/sra-pylib.git
```
This will clone the whole repository in your computer.

You can also download the repository as a `zip` file: [Download as zip](https://github.com/Sayad-Uddin-Tahsin/sra-pylib/archive/refs/heads/main.zip)

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSayad-Uddin-Tahsin%2Fsra-pylib.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSayad-Uddin-Tahsin%2Fsra-pylib?ref=badge_large)
