from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sra-Py',
    version='1.0.0',
    author='Sayad Uddin Tahsin',
    author_email='mr.pluto012@gmail.com',
    description='A Wrapper of some-random-api for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sayad-Uddin-Tahsin/sra-Py',
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.2'
    ],
    dependency_links=[
        'https://pypi.org/project/sra-Py/'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.7'
)
