from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sra-pylib',
    version='1.4.1',
    author='Sayad Uddin Tahsin',
    author_email='mr.pluto012@gmail.com',
    description='A Wrapper of some-random-api for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sayad-Uddin-Tahsin/sra-pylib',
    packages=find_packages(),
    install_requires=[
        'requests>=2.28.2'
    ],
    license='MIT',
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
    python_requires='>=3.7',
    project_urls={
        'Documentation': 'https://github.com/Sayad-Uddin-Tahsin/sra-pylib/wiki',
        'Bug Tracker': 'https://github.com/Sayad-Uddin-Tahsin/sra-pylib/issues',
        'PyPI': 'https://pypi.org/project/sra-pylib/'
    },
    keywords=['some-random-api', 'sra', 'api-wrapper', 'sra-pylib', 'sra-wrapper', 'tahsin-project']
)
