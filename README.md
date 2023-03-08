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

<a href="https://pypi.org/project/sra-pylib"><img src="https://img.shields.io/pypi/status/sra-pylib?label=Status&logo=pypi&logoColor=ffffff" height=22></a> <a href="https://pypi.org/project/sra-pylib"><img src="https://img.shields.io/pypi/v/sra-pylib?label=PyPI Version&logo=pypi&logoColor=ffffff" height=22></a> <a href="https://python.org"><img src="https://img.shields.io/pypi/pyversions/sra-pylib?label=Python&logo=python&logoColor=ffdd54" height=22></a>

## Installation
You can install `sra-pylib` using `pip`:
```console
python -m pip install sra-pylib
```
`sra-pylib` requires Python 3.7 or later.

## Endpoints
`sra-pylib` is currently under development. Currently, only the `animal`, `animu`, `canvas`, `fact`, `image`, `others` and `pokemon` categories of APIs are available in stable version, but we're working to add more.

## Cloning the Repository
If you want to work with the development version of sra-pylib, you can clone the repository and install it using pip:
```console
pip install git+https://github.com/Sayad-Uddin-Tahsin/sra-pylib.git
```
This will install the package from the cloned repository.
