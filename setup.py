import setuptools
from utils import version
reqs = open('requirements.txt', 'r+').read().split()

setuptools.setup(
    name='utils-S',
    version=version,
    author="Sal Faris",
    description="Utility functions",
    packages=setuptools.find_packages(),
    license='MIT',
    author_email='salmanfaris2005@hotmail.com',
    url='https://github.com/The-Sal/utils/',
    download_url='https://github.com/The-Sal/utils/archive/refs/tags/v1.6.5.tar.gz',
    install_requires=reqs
)
