# sra-pylib

`sra-pylib` is a Python wrapper for some-random-api.

```py
import sra

>>> print(sra.animal.Panda.image_link)  # Prints a Panda Image link
"https://i.imgur.com/YVLrUO9.jpg"
>>> print(sra.animal.Panda.fact)  # Prints a Panda Fact
"Giant pandas have been driven out of the lowland areas where they used to live and now are found only in the Chinese provinces of Sichuan, Gansu, and Shaanxi. The forests in these provinces are very damp and rainy. In one year, a forest may receive up to 50 inches of rain and snow."
>>> sra.animal.Panda.save_image()  # Saves the Image
```

With sra-pylib, you can easily access the various endpoints of some-random-api in your Python projects, making it a powerful tool for working with image, fact, and other types of data.
