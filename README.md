# sra-pylib
`sra-pylib` is a Python wrapper for [some-random-api](https://some-random-api.ml).

```python
import sra

>>> print(sra.animal.Panda.image_link)  # Prints a Panda Image link
"https://i.imgur.com/YVLrUO9.jpg"
>>> print(sra.animal.Panda.fact)  # Prints a Panda Fact
"Giant pandas have been driven out of the lowland areas where they used to live and now are found only in the Chinese provinces of Sichuan, Gansu, and Shaanxi. The forests in these provinces are very damp and rainy. In one year, a forest may receive up to 50 inches of rain and snow."
>>> sra.animal.Panda.save_image()  # Saves the Image
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

## Cloning the Repository
You also can install sra-pylib directly from Github, by using this pip command:
```console
pip install git+https://github.com/Sayad-Uddin-Tahsin/sra-pylib.git
```
This will install the package directly from the repository.

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSayad-Uddin-Tahsin%2Fsra-pylib.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSayad-Uddin-Tahsin%2Fsra-pylib?ref=badge_large)
